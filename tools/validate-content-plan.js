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
const campaignPostIdsByLang = {
  ko: new Set(),
  en: new Set(),
};
const postCategories = new Set();
const adEligiblePosts = [];
const siteUrls = new Map();
const internalLinksToCheck = [];

function readText(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

function exists(relativePath) {
  return fs.existsSync(path.join(root, relativePath));
}

function sitePathToRelativePath(sitePath) {
  return sitePath.split("#")[0].split("?")[0].replace(/^\//, "");
}

function imageExists(sitePath) {
  return exists(sitePathToRelativePath(sitePath));
}

function readPngDimensions(sitePath) {
  const relativePath = sitePathToRelativePath(sitePath);
  const buffer = fs.readFileSync(path.join(root, relativePath));
  const pngSignature = "89504e470d0a1a0a";

  if (buffer.length < 24 || buffer.subarray(0, 8).toString("hex") !== pngSignature) {
    return null;
  }

  return {
    width: buffer.readUInt32BE(16),
    height: buffer.readUInt32BE(20),
  };
}

function isCampaignPost(relativePath) {
  return path.basename(relativePath).startsWith("2026-05-23-");
}

function normalizeInternalPostUrl(url) {
  const cleanUrl = url.split("#")[0].split("?")[0];
  return cleanUrl.endsWith("/") ? cleanUrl : `${cleanUrl}/`;
}

function collectInternalLinks(relativePath, text) {
  [...text.matchAll(/\]\((\/[A-Za-z0-9_~./%-]+\/?(?:#[^) \t]+)?)\)/g)].forEach((match) => {
    const url = match[1];
    if (url.startsWith("/images/") || url.startsWith("/assets/")) return;

    internalLinksToCheck.push({
      source: relativePath,
      target: normalizeInternalPostUrl(url),
    });
  });
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

function readFrontMatterText(relativePath) {
  const text = readText(relativePath).replace(/^\uFEFF/, "");
  const lines = text.split(/\r?\n/);
  const endIndex = lines.findIndex((line, index) => index > 0 && line === "---");
  return endIndex === -1 ? "" : lines.slice(1, endIndex).join("\n");
}

function extractYamlList(frontMatterText, key) {
  const lines = frontMatterText.split(/\n/);
  const keyIndex = lines.findIndex((line) => new RegExp(`^${key}:\\s*$`).test(line));
  if (keyIndex === -1) return [];

  const values = [];
  for (let index = keyIndex + 1; index < lines.length; index += 1) {
    const line = lines[index];
    if (/^[A-Za-z0-9_-]+:\s*/.test(line)) break;

    const match = line.match(/^\s+-\s*(.+)$/);
    if (match) values.push(match[1].trim());
  }

  return values;
}

function extractYamlScalarOrBlock(frontMatterText, key) {
  const lines = frontMatterText.split(/\n/);
  const keyIndex = lines.findIndex((line) => new RegExp(`^${key}:\\s*`).test(line));
  if (keyIndex === -1) return "";

  const inline = lines[keyIndex].replace(new RegExp(`^${key}:\\s*`), "").trim();
  if (inline && ![">", "|", ">-", "|-"].includes(inline)) {
    return normalizeYamlValue(inline);
  }

  const values = [];
  for (let index = keyIndex + 1; index < lines.length; index += 1) {
    const line = lines[index];
    if (/^[A-Za-z0-9_-]+:\s*/.test(line)) break;
    const value = line.trim();
    if (value) values.push(value);
  }

  return values.join(" ").trim();
}

function normalizeYamlValue(value) {
  if (!value) return "";
  return value
    .replace(/\s+#.*$/, "")
    .replace(/^["']|["']$/g, "")
    .trim();
}

function parseScalarConfigValue(text, key) {
  const match = text.match(new RegExp(`^\\s*${key}\\s*:\\s*(.*)$`, "m"));
  return match ? normalizeYamlValue(match[1]) : "";
}

function parseSectionScalarConfigValue(text, section, key) {
  const lines = text.split(/\r?\n/);
  let inSection = false;

  for (const line of lines) {
    if (new RegExp(`^${section}\\s*:\\s*$`).test(line)) {
      inSection = true;
      continue;
    }

    if (!inSection) continue;
    if (/^\S/.test(line) && !line.startsWith("#")) break;

    const match = line.match(new RegExp(`^\\s+${key}\\s*:\\s*(.*)$`));
    if (match) return normalizeYamlValue(match[1]);
  }

  return "";
}

function isConfigEnabled(value) {
  return normalizeYamlValue(value).toLowerCase() === "true";
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
    "planning/100-post-multidomain-queue.md",
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
    "planning/100-post-multidomain-queue.md",
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

  const multidomainQueue = readText("planning/100-post-multidomain-queue.md");
  const multidomainRows = multidomainQueue
    .split(/\r?\n/)
    .filter((line) => /^\| (todo|draft|review|published|refresh) \|/.test(line));

  if (multidomainRows.length < 50) {
    errors.push(`100 post multidomain queue should contain at least 50 topic rows, found ${multidomainRows.length}`);
  }

  ["AI Trends", "Study", "Economy", "Image Checklist", "AdSense Checklist"].forEach((term) => {
    if (!multidomainQueue.includes(term)) {
      errors.push(`100 post multidomain queue is missing required term: ${term}`);
    }
  });
}

function validateSearchAndMonetizationFiles() {
  requireFile("robots.txt");
  requireFile("ads.txt");
  requireFile("_config.yml");
  requireFile("Gemfile");
  requireFile("_includes/head.html");
  requireFile("_includes/seo.html");
  requireFile("_includes/article-schema.html");
  requireFile("_includes/faq-schema.html");
  if (errors.length > 0) return;

  const robots = readText("robots.txt");
  const ads = readText("ads.txt");
  const config = readText("_config.yml");
  const gemfileLock = exists("Gemfile.lock") ? readText("Gemfile.lock") : "";
  const head = readText("_includes/head.html");
  const seo = readText("_includes/seo.html");
  const articleSchema = readText("_includes/article-schema.html");
  const faqSchema = readText("_includes/faq-schema.html");
  const siteUrl = parseScalarConfigValue(config, "url");
  const adsenseClient = parseSectionScalarConfigValue(config, "adsense", "client");
  const publisherId = adsenseClient.replace(/^ca-/, "");

  if (siteUrl !== "https://mouseball54.github.io") {
    errors.push(`_config.yml: expected url to be https://mouseball54.github.io, found ${siteUrl || "(empty)"}`);
  }

  if (!robots.includes("User-agent: *")) {
    errors.push("robots.txt: missing User-agent: *");
  }

  if (!robots.includes("Allow: /")) {
    errors.push("robots.txt: missing Allow: /");
  }

  if (!robots.includes(`${siteUrl}/sitemap.xml`)) {
    errors.push(`robots.txt: missing sitemap URL ${siteUrl}/sitemap.xml`);
  }

  if (!config.includes("- jekyll-sitemap")) {
    errors.push("_config.yml: missing jekyll-sitemap plugin");
  }

  if (!config.includes("- jekyll-seo-tag")) {
    errors.push("_config.yml: missing jekyll-seo-tag plugin");
  }

  if (!gemfileLock.includes("jekyll-sitemap")) {
    errors.push("Gemfile.lock: missing jekyll-sitemap dependency");
  }

  if (!gemfileLock.includes("jekyll-seo-tag")) {
    errors.push("Gemfile.lock: missing jekyll-seo-tag dependency");
  }

  if (!head.includes("{% include seo.html %}")) {
    errors.push("_includes/head.html: missing seo.html include");
  }

  if (!seo.includes("page.seo_description")) {
    errors.push("_includes/seo.html: seo_description front matter is not used for meta description");
  }

  if (!seo.includes("{% include faq-schema.html %}")) {
    errors.push("_includes/seo.html: missing faq-schema.html include");
  }

  if (!seo.includes("{% include article-schema.html %}")) {
    errors.push("_includes/seo.html: missing article-schema.html include");
  }

  [
    ["_includes/article-schema.html", articleSchema, 'type="application/ld+json"'],
    ["_includes/article-schema.html", articleSchema, "BlogPosting"],
    ["_includes/article-schema.html", articleSchema, "mainEntityOfPage"],
    ["_includes/article-schema.html", articleSchema, "datePublished"],
    ["_includes/article-schema.html", articleSchema, "dateModified"],
    ["_includes/article-schema.html", articleSchema, "publisher"],
    ["_includes/article-schema.html", articleSchema, "jsonify"],
  ].forEach(([relativePath, text, term]) => {
    if (!text.includes(term)) {
      errors.push(`${relativePath}: missing required article schema term "${term}"`);
    }
  });

  [
    ["_includes/faq-schema.html", faqSchema, 'type="application/ld+json"'],
    ["_includes/faq-schema.html", faqSchema, "FAQPage"],
    ["_includes/faq-schema.html", faqSchema, "Question"],
    ["_includes/faq-schema.html", faqSchema, "acceptedAnswer"],
    ["_includes/faq-schema.html", faqSchema, "jsonify"],
  ].forEach(([relativePath, text, term]) => {
    if (!text.includes(term)) {
      errors.push(`${relativePath}: missing required FAQ schema term "${term}"`);
    }
  });

  if (!publisherId || !ads.includes(`google.com, ${publisherId}, DIRECT`)) {
    errors.push("ads.txt: missing Google AdSense DIRECT publisher entry matching _config.yml");
  }
}

function validatePosts() {
  const koFiles = listMarkdownFiles("_posts/ko");
  const enFiles = listMarkdownFiles("_posts/en");
  const postsByLang = {
    ko: new Map(),
    en: new Map(),
  };
  const outputUrls = new Map();
  const campaignInternalLinksToCheck = [];

  const requiredFields = [
    "title",
    "date",
    "lang",
    "translation_id",
    "header",
    "excerpt",
    "seo_description",
    "categories",
    "tags",
  ];

  [...koFiles, ...enFiles].forEach((relativePath) => {
    const frontMatter = parseFrontMatter(relativePath);
    if (!frontMatter) return;
    const frontMatterText = readFrontMatterText(relativePath);

    requiredFields.forEach((field) => {
      if (!(field in frontMatter)) {
        errors.push(`${relativePath}: missing front matter field "${field}"`);
      }
    });

    const expectedLang = relativePath.includes("/ko/") ? "ko" : "en";
    const campaignPost = isCampaignPost(relativePath);
    const lang = normalizeYamlValue(frontMatter.lang);
    if (lang !== expectedLang) {
      errors.push(`${relativePath}: expected lang "${expectedLang}", found "${lang}"`);
    }

    const text = readText(relativePath);
    const expectedCategory = expectedLang === "ko" ? "ko_" : "en_";
    if (!text.includes(`- ${expectedCategory}`)) {
      errors.push(`${relativePath}: category should include "${expectedCategory}..."`);
    }

    const tags = extractYamlList(frontMatterText, "tags");
    if (tags.length < 3 || tags.length > 5) {
      errors.push(`${relativePath}: tags should contain 3-5 English tags, found ${tags.length}`);
    }

    tags.forEach((tag) => {
      if (/[가-힣]/.test(tag)) {
        errors.push(`${relativePath}: tag should be English-only: ${tag}`);
      }
    });

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
    if (campaignPost) {
      campaignPostIdsByLang[expectedLang].add(translationId);
    }

    const permalink = normalizeYamlValue(frontMatter.permalink);
    const slug = path.basename(relativePath, ".md").replace(/^\d{4}-\d{2}-\d{2}-/, "");
    const categoryMatch = text.match(/categories:\s*\r?\n\s*-\s*([A-Za-z0-9_-]+)/);
    const category = categoryMatch ? categoryMatch[1] : "";
    if (category) {
      postCategories.add(category);
    }
    const outputUrl = permalink || (category ? `/${category}/${slug}/` : "");
    if (outputUrl) {
      if (outputUrls.has(outputUrl)) {
        errors.push(`${relativePath}: output URL collides with ${outputUrls.get(outputUrl)} at ${outputUrl}`);
      }
      outputUrls.set(outputUrl, relativePath);
      siteUrls.set(outputUrl, relativePath);
    }

    collectInternalLinks(relativePath, text);

    const headerImagePaths = [...text.matchAll(/^\s*(?:teaser|overlay_image):\s*(\/images\/[^\s#]+)/gm)].map(
      (match) => match[1],
    );
    const bodyImageMatches = [...text.matchAll(/!\[([^\]]*)\]\((\/images\/[^)\s]+)\)/g)].map((match) => ({
      alt: match[1].trim(),
      path: match[2],
    }));
    const bodyImagePaths = bodyImageMatches.map((match) => match.path);
    const imagePaths = [...headerImagePaths, ...bodyImagePaths];

    if (imagePaths.length === 0) {
      warnings.push(`${relativePath}: no local image path found; every new post should include a meaningful image`);
    }

    if (campaignPost) {
      if (!("seo_title" in frontMatter)) {
        errors.push(`${relativePath}: campaign post must include seo_title`);
      }

      if (!("last_modified_at" in frontMatter)) {
        errors.push(`${relativePath}: campaign post must include last_modified_at`);
      } else {
        const publishedAt = Date.parse(normalizeYamlValue(frontMatter.date));
        const modifiedAt = Date.parse(normalizeYamlValue(frontMatter.last_modified_at));
        if (Number.isNaN(modifiedAt)) {
          errors.push(`${relativePath}: campaign last_modified_at should be a valid ISO date`);
        } else if (!Number.isNaN(publishedAt) && modifiedAt < publishedAt) {
          errors.push(`${relativePath}: campaign last_modified_at should not be earlier than date`);
        }
      }

      const seoTitle = extractYamlScalarOrBlock(frontMatterText, "seo_title");
      const seoDescription = extractYamlScalarOrBlock(frontMatterText, "seo_description");
      const seoTitleMin = expectedLang === "ko" ? 10 : 20;
      const seoDescriptionMin = expectedLang === "ko" ? 60 : 80;

      if (seoTitle.length < seoTitleMin || seoTitle.length > 70) {
        errors.push(`${relativePath}: campaign seo_title should be ${seoTitleMin}-70 characters, found ${seoTitle.length}`);
      }

      if (seoDescription.length < seoDescriptionMin || seoDescription.length > 170) {
        errors.push(
          `${relativePath}: campaign seo_description should be ${seoDescriptionMin}-170 characters, found ${seoDescription.length}`,
        );
      }

      const faqHeading = expectedLang === "ko" ? "자주 묻는 질문" : "FAQ";
      const faqHeadingMatch = text.match(new RegExp(`^##\\s+${faqHeading}\\s*$`, "m"));
      if (!faqHeadingMatch) {
        errors.push(`${relativePath}: campaign post must include a ${faqHeading} section`);
      } else {
        const faqStart = faqHeadingMatch.index + faqHeadingMatch[0].length;
        const remainingText = text.slice(faqStart);
        const nextHeadingMatch = remainingText.match(/\n##\s+/);
        const faqText = nextHeadingMatch ? remainingText.slice(0, nextHeadingMatch.index) : remainingText;
        const faqQuestionCount = [...faqText.matchAll(/^###\s+/gm)].length;
        if (faqQuestionCount < 3) {
          errors.push(`${relativePath}: campaign ${faqHeading} section should include at least three questions`);
        }
      }

      const relatedHeadingPattern =
        expectedLang === "ko"
          ? /^##\s+(함께 보면 좋은 글|관련 글)\s*$/m
          : /^##\s+(Related Reading|Related Posts|Related Articles)\s*$/m;
      const relatedHeadingMatch = text.match(relatedHeadingPattern);
      if (!relatedHeadingMatch) {
        errors.push(`${relativePath}: campaign post must include a related reading section`);
      } else {
        const relatedStart = relatedHeadingMatch.index + relatedHeadingMatch[0].length;
        const remainingText = text.slice(relatedStart);
        const nextHeadingMatch = remainingText.match(/\n##\s+/);
        const relatedText = nextHeadingMatch ? remainingText.slice(0, nextHeadingMatch.index) : remainingText;
        const relatedLinkCount = [...relatedText.matchAll(/\]\(\/(?:ko|en)_[^)#?\s]+\/\)/g)].length;
        if (relatedLinkCount < 2) {
          errors.push(`${relativePath}: campaign related reading section should include at least two internal links`);
        }
      }

      const campaignHeaderImagePaths = headerImagePaths.filter((imagePath) => imagePath.startsWith("/images/2026-05-23-"));
      const campaignBodyImagePaths = bodyImagePaths.filter((imagePath) => imagePath.startsWith("/images/2026-05-23-"));

      if (campaignHeaderImagePaths.length === 0) {
        errors.push(`${relativePath}: campaign post must include a campaign-specific local header image`);
      }

      if (campaignBodyImagePaths.length === 0) {
        errors.push(`${relativePath}: campaign post must include a campaign-specific local body image`);
      }

      const campaignBodyImageMatches = bodyImageMatches.filter((match) => match.path.startsWith("/images/2026-05-23-"));
      campaignBodyImageMatches.forEach((match) => {
        if (match.alt.length < 12) {
          errors.push(`${relativePath}: campaign body image alt text is too short for ${match.path}`);
        }
      });

      [...new Set([...campaignHeaderImagePaths, ...campaignBodyImagePaths])].forEach((imagePath) => {
        if (!imageExists(imagePath)) return;
        const dimensions = readPngDimensions(imagePath);
        if (!dimensions) {
          errors.push(`${relativePath}: campaign image should be a valid PNG: ${imagePath}`);
          return;
        }

        if (dimensions.width < 1000 || dimensions.height < 500) {
          errors.push(
            `${relativePath}: campaign image is too small: ${imagePath} (${dimensions.width}x${dimensions.height})`,
          );
        }
      });

      const internalLinks = [...text.matchAll(/\]\((\/(?:ko|en)_[^)#?\s]+(?:[?#][^)]*)?)\)/g)].map(
        (match) => match[1],
      );
      if (internalLinks.length < 2) {
        errors.push(`${relativePath}: campaign post should include at least two internal links`);
      }

      internalLinks.forEach((url) => {
        campaignInternalLinksToCheck.push({
          source: relativePath,
          target: normalizeInternalPostUrl(url),
        });
      });

      if (category.includes("easy_labeling")) {
        if (!text.includes("https://mouseball54.github.io/easy_labeling/")) {
          errors.push(`${relativePath}: Easy Labeling campaign post must include the launch link`);
        }

        if (!text.includes("/images/easy_labeling_sample.png")) {
          errors.push(`${relativePath}: Easy Labeling campaign post must include the Easy Labeling sample screen`);
        }
      }

      if (category.includes("Economy")) {
        const hasEnglishDisclaimer = /not investment advice|not financial advice|personal financial advice/i.test(text);
        const hasKoreanDisclaimer = /(투자 권유|투자 조언|재무 조언|금융 조언)/.test(text);
        if (!hasEnglishDisclaimer && !hasKoreanDisclaimer) {
          errors.push(`${relativePath}: Economy campaign post must include an educational/non-advice disclaimer`);
        }
      }
    }

    imagePaths.forEach((imagePath) => {
      if (!imageExists(imagePath)) {
        errors.push(`${relativePath}: referenced image does not exist: ${imagePath}`);
      }
    });

    const content = text.split(/^---\s*$/m).slice(2).join("---");
    const wordCount = content.replace(/<[^>]*>/g, " ").trim().split(/\s+/).filter(Boolean).length;
    if (campaignPost && wordCount < 450) {
      errors.push(`${relativePath}: campaign post should contain at least 450 words, found ${wordCount}`);
    }

    if (wordCount >= 700 && !/^\s*ads\s*:\s*false\s*$/m.test(text)) {
      adEligiblePosts.push(relativePath);
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

  const campaignPairs = [...campaignPostIdsByLang.en].filter((translationId) =>
    campaignPostIdsByLang.ko.has(translationId),
  );
  const campaignPostCount = campaignPostIdsByLang.ko.size + campaignPostIdsByLang.en.size;
  if (campaignPostCount < 100) {
    errors.push(`Campaign should contain at least 100 new post files, found ${campaignPostCount}`);
  }

  if (campaignPairs.length < 50) {
    errors.push(`Campaign should contain at least 50 paired topic IDs, found ${campaignPairs.length}`);
  }

  campaignInternalLinksToCheck.forEach(({ source, target }) => {
    if (!outputUrls.has(target)) {
      errors.push(`${source}: campaign internal link does not resolve to a known post URL: ${target}`);
    }
  });
}

function validatePages() {
  listMarkdownFiles("_pages").forEach((relativePath) => {
    const frontMatter = parseFrontMatter(relativePath);
    if (!frontMatter) return;

    const permalink = normalizeYamlValue(frontMatter.permalink);
    if (permalink) {
      siteUrls.set(normalizeInternalPostUrl(permalink), relativePath);
    }

    collectInternalLinks(relativePath, readText(relativePath));
  });
}

function validateInternalLinks() {
  internalLinksToCheck.forEach(({ source, target }) => {
    if (!siteUrls.has(target)) {
      errors.push(`${source}: internal link does not resolve to a known site URL: ${target}`);
    }
  });
}

function validateCategoryNavigation() {
  requireFile("_data/navigation.yml");
  if (errors.length > 0) return;

  const navigation = readText("_data/navigation.yml");

  [...postCategories].sort().forEach((category) => {
    const pagePath = `_pages/category-${category}.md`;
    requireFile(pagePath);
    if (!exists(pagePath)) return;

    const page = readText(pagePath);
    [
      [`permalink: /${category}/`, "permalink"],
      'nav: "sidebar-category"',
      `site.categories.${category}`,
    ].forEach((term) => {
      const text = Array.isArray(term) ? term[0] : term;
      const label = Array.isArray(term) ? term[1] : term;
      if (!page.includes(text)) {
        errors.push(`${pagePath}: missing category archive ${label}`);
      }
    });

    if (!navigation.includes(`url: /${category}/`)) {
      errors.push(`_data/navigation.yml: missing sidebar URL for category ${category}`);
    }

    if (!navigation.includes(`category: "${category}"`)) {
      errors.push(`_data/navigation.yml: missing sidebar category binding for ${category}`);
    }
  });
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
  const adsenseClient = parseSectionScalarConfigValue(config, "adsense", "client");
  const adsenseEnabled = isConfigEnabled(parseSectionScalarConfigValue(config, "adsense", "enabled"));
  const autoAdsEnabled = isConfigEnabled(parseSectionScalarConfigValue(config, "adsense", "auto_ads"));
  const inArticleSlot = parseSectionScalarConfigValue(config, "adsense", "in_article_slot");
  const postBottomSlot = parseSectionScalarConfigValue(config, "adsense", "post_bottom_slot");
  const minWordsForAds = Number(parseSectionScalarConfigValue(config, "adsense", "min_words_for_ads") || "700");

  const publisherMatch = adsText.match(/google\.com,\s*(pub-\d+),\s*DIRECT/);
  const clientMatch = adsenseClient.match(/^ca-(pub-\d+)$/);

  if (!publisherMatch) {
    errors.push("ads.txt does not contain a valid Google publisher line");
  }

  if (!clientMatch) {
    errors.push("_config.yml does not contain adsense.client in ca-pub format");
  }

  if (publisherMatch && clientMatch && publisherMatch[1] !== clientMatch[1]) {
    errors.push(`AdSense publisher mismatch: ads.txt=${publisherMatch[1]}, _config.yml=ca-${clientMatch[1]}`);
  }

  if (Number.isNaN(minWordsForAds) || minWordsForAds < 300) {
    errors.push("_config.yml adsense.min_words_for_ads should be a number >= 300");
  }

  if (adsenseEnabled && !autoAdsEnabled) {
    if (!inArticleSlot) {
      errors.push("AdSense is enabled but adsense.in_article_slot is empty");
    }

    if (!postBottomSlot) {
      errors.push("AdSense is enabled but adsense.post_bottom_slot is empty");
    }
  } else if (adsenseEnabled && autoAdsEnabled && (!inArticleSlot || !postBottomSlot)) {
    warnings.push("AdSense Auto ads are enabled; manual post ad slots remain inactive until slot IDs are configured");
  } else if (!inArticleSlot || !postBottomSlot) {
    warnings.push("AdSense is disabled or slot IDs are empty; ads will not render on posts until enabled and slots are configured");
  }

  if (adEligiblePosts.length === 0) {
    warnings.push("No posts currently meet the automatic ad eligibility threshold");
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
validateSearchAndMonetizationFiles();
validatePosts();
validatePages();
validateQueuePostState();
validateCategoryNavigation();
validateInternalLinks();
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
