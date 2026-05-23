---
layout: single
title: >
  Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법
seo_title: >
  Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법
date: 2025-09-20T08:29:00+09:00
last_modified_at: 2026-05-23T23:59:00+09:00
lang: ko
translation_id: edge-case-gallery-dataset
header:
  teaser: /images/2026-05-23-edge-case-gallery-dataset/hero.png
  overlay_image: /images/2026-05-23-edge-case-gallery-dataset/hero.png
  overlay_filter: 0.36
  image_description: >
    Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법의 이미지 라벨링 흐름과 검수 기준을 요약한 이미지입니다.
excerpt: >
  Edge case gallery는 애매한 객체, 가림, 작은 물체, 클래스 혼동 사례를 모아 라벨러와 검수자가 같은 기준을 보게 하는 자료다.
seo_description: >
  Edge case gallery는 애매한 객체, 가림, 작은 물체, 클래스 혼동 사례를 모아 라벨러와 검수자가 같은 기준을 보게 하는 자료다.
categories:
  - ko_easy_labeling
tags:
  - EdgeCases
  - Instructions
  - Annotation
  - Review
---

이미지 라벨링은 박스를 많이 그리는 일이 아니라 **나중에 학습 가능한 기준을 남기는 일**입니다. 이 글은 **Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법** 주제를 Easy Labeling 작업 흐름과 YOLO 데이터셋 검수 관점에서 정리합니다.

Edge case gallery는 애매한 객체, 가림, 작은 물체, 클래스 혼동 사례를 모아 라벨러와 검수자가 같은 기준을 보게 하는 자료다.

도구 실행: [Easy Labeling](https://mouseball54.github.io/easy_labeling/)

![Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 라벨링 품질 흐름도](/images/2026-05-23-edge-case-gallery-dataset/hero.png)

## 이 작업이 줄이는 문제

애매한 기준은 문장만으로 전달하기 어렵습니다. 실제 이미지를 붙이면 다음 작업에서 같은 질문이 반복되는 비용이 줄어듭니다.

이 주제는 라벨을 더 많이 그리는 방법보다 **애매한 이미지**와 **결정 메모**를 안정적으로 남기는 방법에 가깝습니다. 객체 탐지 프로젝트에서는 작은 좌표 오류, 클래스 순서 변경, 폴더 구조 실수가 학습 실패처럼 보일 수 있습니다. 그래서 작업자는 도구 사용법과 함께 데이터셋 계약을 문서로 남겨야 합니다.

## 먼저 확인할 품질 신호

- **애매한 이미지**: Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **결정 메모**: Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **갤러리 버전**: Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **검수 교육**: Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.

![Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법 라벨링 검수 체크리스트](/images/2026-05-23-edge-case-gallery-dataset/checklist.png)

## Easy Labeling 적용 흐름

작업은 작은 파일럿 배치에서 시작합니다. 먼저 질문이 나온 이미지를 따로 저장합니다. 그 다음 결정된 기준을 이미지 아래 한 문장으로 씁니다. 20~50장 정도의 샘플을 Easy Labeling에서 열어 실제 박스를 그려 보면 지침서의 빈칸이 빨리 드러납니다. 이 단계에서 나온 질문은 채팅으로 흘려보내지 말고 클래스 사전이나 edge case gallery에 반영해야 합니다.

Easy Labeling은 브라우저에서 로컬 이미지 폴더를 열어 YOLO 박스를 작성하는 흐름에 맞춰져 있습니다. 업로드 기반 도구가 부담스러운 파일, 빠르게 확인해야 하는 샘플 배치, 클래스 기준을 실험하는 초기 데이터셋에 특히 잘 맞습니다. 다만 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다.

![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면](/images/easy_labeling_sample.png)

## 검수 예시

검수자는 전체 이미지를 다시 라벨링하지 않아도 됩니다. 샘플을 열고 **애매한 이미지** 기준이 지켜졌는지, 그리고 **갤러리 버전**가 프로젝트 규칙과 맞는지 먼저 봅니다. 문제가 반복되면 해당 라벨러의 전체 배치를 의심하기보다 지침서가 충분히 구체적인지, 예시 이미지가 부족한지, 도구 저장 설정이 헷갈리게 되어 있는지 순서대로 확인합니다.

## 실무 체크리스트

- 작업 전 **애매한 이미지** 기준을 문서에서 확인합니다.
- 파일 저장 후 **결정 메모**가 실제 라벨 파일에 반영됐는지 샘플로 확인합니다.
- 라벨링 중 생긴 질문은 다음 배치 전에 지침서로 되돌립니다.
- 학습팀에 넘기기 전 이미지, 라벨, 클래스 파일, 검수 기록을 같은 버전으로 묶습니다.

## 자주 묻는 질문

### Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법는 Easy Labeling만 쓰면 해결되나요?

아닙니다. Easy Labeling은 로컬 이미지와 YOLO 박스를 다루는 작업을 빠르게 만들 수 있지만, **애매한 이미지** 기준은 프로젝트가 직접 정해야 합니다. 도구와 지침서를 같이 써야 재작업이 줄어듭니다.

### 작은 데이터셋도 이런 검수가 필요한가요?

작은 데이터셋일수록 한두 개 오류가 결과에 크게 보일 수 있습니다. 최소한 **결정 메모**와 클래스 순서는 샘플로 확인한 뒤 학습으로 넘기는 편이 안전합니다.

### 언제 다시 라벨링해야 하나요?

같은 유형의 오류가 여러 이미지에서 반복되거나 모델 오류 분석에서 특정 클래스가 계속 흔들리면 다시 라벨링해야 합니다. 단순히 박스 하나를 고치는 수준이 아니라 기준 문서를 고친 뒤 같은 기준으로 배치를 다시 보는 것이 좋습니다.


## 참고할 자료

- [Label Studio Bounding Box Template](https://labelstud.io/templates/image_bbox)
- [FiftyOne Annotation Guide](https://docs.voxel51.com/getting_started/annotation/index.html)
- [CVAT Dataset Formats](https://docs.cvat.ai/docs/dataset_management/formats/)

## 함께 보면 좋은 글

- [YOLO 학습 전 QA 루틴: 데이터 오류를 모델 문제로 착각하지 않기](/ko_easy_labeling/qa-before-yolo-training/)
- [로컬 이미지 라벨링 워크플로우: 이미지, 클래스, 라벨, 검수 정리법](/ko_easy_labeling/local-image-labeling-workflow/)
