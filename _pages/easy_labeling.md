---
title: "Easy Labeling"
layout: single_wide
permalink: /easy_labeling_intro/
header:
  overlay_image: /images/easy_labeling_sample.png
  overlay_filter: 0.6
  caption: "Easy Labeling"
  actions:
    - label: "<strong>Go to Easy Labeling</strong>"
      url: "https://mouseball54.github.io/easy_labeling/"

---

## Easy Labeling

YOLO 학습 데이터 라벨링을 손쉽게 진행할 수 있는 웹 도구입니다.

- 웹 기반이라 설치가 필요 없습니다.  
- 로컬 파일을 직접 처리합니다.  
- File System Access API로 안전하고 빠르게 작업합니다.
  
<br/>

<a href="https://mouseball54.github.io/easy_labeling/" class="btn btn--success btn--large">Easy Labeling 실행하기</a>

---

## Easy Labeling: Web-Based YOLO Data Labeling Tool

A simple, installation-free tool to label YOLO datasets in your browser.

- Web-based: no installation required.  
- Processes local files directly.  
- Utilizes the File System Access API for secure, high-speed operation.
  
<br/>

<a href="https://mouseball54.github.io/easy_labeling/" class="btn btn--success btn--large">Launch Easy Labeling</a>

---
<figure>
  <img src="/images/easy_labeling_sample.png" alt="Easy Labeling sample">
  <figcaption>Easy Labeling sample image</figcaption>
</figure>

### 관련 포스트 / Related Posts
{% assign posts = site.categories.ko_easy_labeling | concat: site.categories.en_easy_labeling | sort: "date" | reverse %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
