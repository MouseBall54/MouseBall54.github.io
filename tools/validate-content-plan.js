const fs = require("fs");
const path = require("path");

const root = process.cwd();
const errors = [];
const warnings = [];
const queueStatusById = new Map();
const postIdsByLang = {
  ko: new Set(),
  en: new Set(),
};

function readText(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function exists(relativePath) {
  return fs.existsSync(path.join(root, relativePath));
}

function listMarkdownFiles(relativeDir) {
  const dir = path.join(root, relativeDir);
  return fs
    .readdirSync(dir)
    .filter((name) => name.endsWith(".md"))
    .map((name) => path.join(relativeDir, name).replace(/\\/g, "/"));
}

function parseFrontMatter(relativePath) {
  const text = readText(relativePath).replace(/^\uFEFF/, "");
  const lines = text.split(/\r?\n/);

  if (lines[0] !== "---") {
    errors.push(`${relativePath}: missing opening front matter delimiter`);
    return null;
  }

  const endIndex = lines.findIndex((line, index) => index > 0 && line === "---");
  if (endIndex === -1) {
    errors.push(`${relativePath}: missing closing front matter delimiter`);
    return null;
  }

  const frontMatter = {};
  for (let index = 1; index < endIndex; index += 1) {
    const line = lines[index];
    const match = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (match) {
      frontMatter[match[1]] = match[2].trim();
    }
  }

  return frontMatter;
}

function normalizeYamlValue(value) {
  if (!value) return "";
  return value.replace(/^["']|["']$/g, "").trim();
}

function requireFile(relativePath) {
  if (!exists(relativePath)) {
    errors.push(`Missing required file: ${relativePath}`);
  }
}

function validatePlanningDocs() {
  const requiredFiles = [
    "planning/weekly-100k-traffic-master-plan.md",
    "planning/p0-content-queue.md",
    "planning/p0-content-briefs.md",
    "planning/post-production-template.md",
  ];

  requiredFiles.forEach(requireFile);
  if (errors.length > 0) return;

  const masterPlan = readText("planning/weekly-100k-traffic-master-plan.md");
  const requiredMasterPlanTerms = [
    "주간 조회 수 100,000회",
    "키워드 마스터 리스트",
    "AdSense 배치 계획",
    "측정 지표",
    "planning/p0-content-queue.md",
    "planning/p0-content-briefs.md",
    "planning/post-production-template.md",
  ];

  requiredMasterPlanTerms.forEach((term) => {
    if (!masterPlan.includes(term)) {
      errors.push(`Master plan is missing required term: ${term}`);
    }
  });

  const queue = readText("planning/p0-content-queue.md");
  const queueRows = queue
    .split(/\r?\n/)
    .filter((line) => /^\| (todo|draft|review|published|refresh) \|/.test(line));

  if (queueRows.length < 45) {
    errors.push(`P0 queue should contain at least 45 rows, found ${queueRows.length}`);
  }

  const queueIds = new Set();
  const draftQueueIds = new Set();
  queueRows.forEach((line) => {
    const columns = line.split("|").map((column) => column.trim());
    const status = columns[1];
    const translationId = columns[2];
    if (queueIds.has(translationId)) {
      errors.push(`Duplicate translation_id in P0 queue: ${translationId}`);
    }
    queueIds.add(translationId);
    queueStatusById.set(translationId, status);
    if (status === "draft") {
      draftQueueIds.add(translationId);
    }
  });

  const briefs = readText("planning/p0-content-briefs.md");
  const briefIds = [...briefs.matchAll(/Translation ID:\s*`([^`]+)`/g)].map((match) => match[1]);
  const uniqueBriefIds = new Set(briefIds);

  if (briefIds.length < 10) {
    errors.push(`P0 content briefs should contain at least 10 briefs, found ${briefIds.length}`);
  }

  briefIds.forEach((translationId) => {
    if (!queueIds.has(translationId)) {
      errors.push(`P0 content brief references an ID not in queue: ${translationId}`);
    }
  });

  draftQueueIds.forEach((translationId) => {
    if (!uniqueBriefIds.has(translationId)) {
      errors.push(`P0 queue marks "${translationId}" as draft but no brief exists`);
    }
  });

  const template = readText("planning/post-production-template.md");
  [
    "Korean Front Matter",
    "English Front Matter",
    "Quality Checklist",
    "Ad Placement Notes",
    "translation_id",
  ].forEach((term) => {
    if (!template.includes(term)) {
      errors.push(`Post template is missing required section or field: ${term}`);
    }
  });
}

function validatePosts() {
  const koFiles = listMarkdownFiles("_posts/ko");
  const enFiles = listMarkdownFiles("_posts/en");
  const postsByLang = {
    ko: new Map(),
    en: new Map(),
  };
  const outputUrls = new Map();

  const requiredFields = ["title", "lang", "translation_id", "header", "excerpt", "categories", "tags"];

  [...koFiles, ...enFiles].forEach((relativePath) => {
    const frontMatter = parseFrontMatter(relativePath);
    if (!frontMatter) return;

    requiredFields.forEach((field) => {
      if (!(field in frontMatter)) {
        errors.push(`${relativePath}: missing front matter field "${field}"`);
      }
    });

    const expectedLang = relativePath.includes("/ko/") ? "ko" : "en";
    const lang = normalizeYamlValue(frontMatter.lang);
    if (lang !== expectedLang) {
      errors.push(`${relativePath}: expected lang "${expectedLang}", found "${lang}"`);
    }

    const text = readText(relativePath);
    const expectedCategory = expectedLang === "ko" ? "ko_" : "en_";
    if (!text.includes(`- ${expectedCategory}`)) {
      errors.push(`${relativePath}: category should include "${expectedCategory}..."`);
    }

    const translationId = normalizeYamlValue(frontMatter.translation_id);
    if (!translationId) {
      errors.push(`${relativePath}: empty translation_id`);
      return;
    }

    if (postsByLang[expectedLang].has(translationId)) {
      errors.push(`${relativePath}: duplicate ${expectedLang} translation_id "${translationId}"`);
    }
    postsByLang[expectedLang].set(translationId, relativePath);
    postIdsByLang[expectedLang].add(translationId);

    const permalink = normalizeYamlValue(frontMatter.permalink);
    const slug = path.basename(relativePath, ".md").replace(/^\d{4}-\d{2}-\d{2}-/, "");
    const categoryMatch = text.match(/categories:\s*\r?\n\s*-\s*([A-Za-z0-9_-]+)/);
    const category = categoryMatch ? categoryMatch[1] : "";
    const outputUrl = permalink || (category ? `/${category}/${slug}/` : "");
    if (outputUrl) {
      if (outputUrls.has(outputUrl)) {
        errors.push(`${relativePath}: output URL collides with ${outputUrls.get(outputUrl)} at ${outputUrl}`);
      }
      outputUrls.set(outputUrl, relativePath);
    }

    if (!("seo_description" in frontMatter)) {
      warnings.push(`${relativePath}: missing seo_description; excerpt fallback may be used`);
    }
  });

  for (const [translationId, relativePath] of postsByLang.en) {
    if (!postsByLang.ko.has(translationId)) {
      errors.push(`${relativePath}: missing Korean pair for translation_id "${translationId}"`);
    }
  }

  for (const [translationId, relativePath] of postsByLang.ko) {
    if (!postsByLang.en.has(translationId)) {
      errors.push(`${relativePath}: missing English pair for translation_id "${translationId}"`);
    }
  }
}

function validateQueuePostState() {
  for (const [translationId, status] of queueStatusById) {
    if (status === "review" || status === "published") {
      if (!postIdsByLang.ko.has(translationId) || !postIdsByLang.en.has(translationId)) {
        errors.push(`P0 queue marks "${translationId}" as ${status} but the paired posts do not both exist`);
      }
    }
  }
}

function validateAdsense() {
  requireFile("ads.txt");
  requireFile("_config.yml");
  requireFile("_includes/head/custom.html");
  requireFile("_includes/ad-content.html");
  requireFile("_includes/ad-inarticle.html");
  requireFile("_layouts/single.html");

  if (errors.length > 0) return;

  const adsText = readText("ads.txt");
  const config = readText("_config.yml");
  const headCustom = readText("_includes/head/custom.html");
  const adContent = readText("_includes/ad-content.html");
  const adInArticle = readText("_includes/ad-inarticle.html");
  const singleLayout = readText("_layouts/single.html");

  const publisherMatch = adsText.match(/google\.com,\s*(pub-\d+),\s*DIRECT/);
  const clientMatch = config.match(/client\s*:\s*["']ca-(pub-\d+)["']/);

  if (!publisherMatch) {
    errors.push("ads.txt does not contain a valid Google publisher line");
  }

  if (!clientMatch) {
    errors.push("_config.yml does not contain adsense.client in ca-pub format");
  }

  if (publisherMatch && clientMatch && publisherMatch[1] !== clientMatch[1]) {
    errors.push(`AdSense publisher mismatch: ads.txt=${publisherMatch[1]}, _config.yml=ca-${clientMatch[1]}`);
  }

  [
    ["_includes/head/custom.html", headCustom, "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"],
    ["_includes/ad-content.html", adContent, "min_words_for_ads"],
    ["_includes/ad-content.html", adContent, "page.id"],
    ["_includes/ad-content.html", adContent, "page.ads != false"],
    ["_includes/ad-inarticle.html", adInArticle, "Advertisements"],
    ["_includes/ad-inarticle.html", adInArticle, "adsbygoogle"],
    ["_layouts/single.html", singleLayout, "{% include ad-content.html %}"],
  ].forEach(([relativePath, text, term]) => {
    if (!text.includes(term)) {
      errors.push(`${relativePath}: missing required AdSense guard or markup "${term}"`);
    }
  });
}

validatePlanningDocs();
validatePosts();
validateQueuePostState();
validateAdsense();

warnings.slice(0, 20).forEach((warning) => {
  console.warn(`WARN ${warning}`);
});

if (warnings.length > 20) {
  console.warn(`WARN ${warnings.length - 20} additional warnings hidden`);
}

if (errors.length > 0) {
  errors.forEach((error) => {
    console.error(`ERROR ${error}`);
  });
  process.exit(1);
}

console.log("Content plan validation passed.");
console.log(`Warnings: ${warnings.length}`);
