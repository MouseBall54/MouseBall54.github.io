---
title: "Easy Labeling"
layout: archive
permalink: /ko_easy_labeling/
lang: ko
seo_description: >
  Easy Labeling, YOLO 라벨 포맷, COCO 변환, 클래스 관리, 라벨 검수, 데이터셋 분할, 로컬 이미지 라벨링 워크플로우를 정리한 실무 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Easy Labeling 카테고리는 이미지 라벨링 작업을 더 빠르고 일관되게 만드는 방법을 다룹니다. YOLO 라벨 포맷, COCO 변환, 클래스 사전, bounding box 품질, train/val/test 분할, 데이터셋 QA, active learning 루프, 로컬 우선 작업처럼 모델 학습 전 데이터 품질을 좌우하는 주제를 모았습니다.

각 글은 단순한 도구 소개보다 실제 데이터셋이 깨지는 지점을 중심으로 설명합니다. 작은 샘플 세트로 클래스 기준을 먼저 맞추고, Easy Labeling에서 라벨을 저장한 뒤, 폴더 구조와 `data.yaml`까지 검수하는 흐름을 권장합니다.

처음에는 로컬 라벨링 워크플로우와 YOLO 포맷을 읽고, 이후 bounding box 품질, 라벨 지침서, train/val/test 분할, QA 루틴으로 확장하면 좋습니다.

## 먼저 읽기

- [로컬 이미지 라벨링 워크플로우](/ko_easy_labeling/local-image-labeling-workflow/)
- [Easy Labeling으로 YOLO 데이터셋 만들기](/ko_easy_labeling/easy-labeling-yolo-dataset/)
- [YOLO 라벨 포맷 이해하기](/ko_easy_labeling/yolo-label-format/)
- [Bounding Box 품질 체크리스트](/ko_easy_labeling/bounding-box-quality-checklist/)
- [Train, Val, Test 데이터셋 분할](/ko_easy_labeling/dataset-split-train-val-test/)

## 최신 글

{% assign posts = site.categories["ko_easy_labeling"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
