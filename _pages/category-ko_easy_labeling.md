---
title: "Easy Labeling"
layout: archive
permalink: /ko_easy_labeling/
lang: ko
seo_description: >
  Easy Labeling, 이미지 라벨링, YOLO 데이터셋, COCO 변환, 클래스 관리와 로컬 검수 워크플로우를 정리한 실무 글 모음입니다.
sidebar:
    nav: "sidebar-category"
---

Easy Labeling 카테고리는 이미지 라벨링 작업을 더 빠르고 일관되게 만드는 방법을 다룹니다. 클래스 정의, YOLO 데이터셋, COCO 변환, 로컬 검수 흐름처럼 모델 학습 전 데이터 품질을 좌우하는 주제를 모았습니다.

처음에는 로컬 라벨링 워크플로우를 읽고, 이후 YOLO 포맷과 클래스 관리 글로 데이터셋 기준을 정리하면 좋습니다.

각 글은 라벨링 도구 사용법뿐 아니라 데이터셋이 깨지는 지점과 검수 기준을 함께 설명합니다. 작은 샘플 세트로 클래스 기준을 먼저 맞춘 뒤 전체 이미지 작업으로 확장하는 흐름을 권장합니다.

## 먼저 읽기

- [로컬 이미지 라벨링 워크플로우](/ko_easy_labeling/local-image-labeling-workflow/)
- [Easy Labeling으로 YOLO 데이터셋 만들기](/ko_easy_labeling/easy-labeling-yolo-dataset/)
- [YOLO 라벨 포맷 이해하기](/ko_easy_labeling/yolo-label-format/)

## 최신 글

{% assign posts = site.categories.ko_easy_labeling %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
