---
title: "Easy Labeling"
layout: single
permalink: /easy_labeling_intro/
header:
  overlay_image: /images/easy_labeling_sample.png
  overlay_filter: 0.6
  caption: "Easy Labeling"
  actions:
    - label: "<strong>Go to Easy Labeling</strong>"
      url: "https://mouseball54.github.io/easy_labeling/"
sidebar:
  nav: "sidebar-category"
---

## Easy Labeling: 웹 기반 YOLO 데이터 라벨링 도구

Easy Labeling은 객체 탐지(Object Detection) 모델, 특히 YOLO 계열 모델 학습에 필요한 데이터셋을 구축하는 과정을 간소화하기 위해 탄생했습니다.

가장 큰 특징은 **설치가 필요 없는 웹 기반**이라는 점과, 사용자의 **로컬 파일을 직접 처리**한다는 점입니다. File System Access API를 활용하여 이미지와 라벨 파일을 서버에 업로드하는 과정 없이 작업하므로, 민감한 데이터를 안전하게 다룰 수 있고 속도도 매우 빠릅니다.

<br/>

<a href="https://mouseball54.github.io/easy_labeling/" class="btn btn--success btn--large">Easy Labeling 실행하기</a>

---

## Easy Labeling: Web-Based YOLO Data Labeling Tool

Easy Labeling was created to streamline the process of building datasets for object detection models, especially for the YOLO family.

Its biggest features are that it is **web-based with no installation required** and that it **processes the user's local files directly**. By using the File System Access API, it works without uploading images and label files to a server, allowing you to handle sensitive data securely and work at a very high speed.

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
