---
layout: single
title: >
  가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기
seo_title: >
  가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기
date: 2026-05-23T11:34:00+09:00
last_modified_at: 2026-05-23T23:59:00+09:00
lang: ko
translation_id: occlusion-truncation-labeling
header:
  teaser: /images/2026-05-23-occlusion-truncation-labeling/hero.png
  overlay_image: /images/2026-05-23-occlusion-truncation-labeling/hero.png
  overlay_filter: 0.36
  image_description: >
    가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기의 이미지 라벨링 흐름과 검수 기준을 요약한 이미지입니다.
excerpt: >
  가려진 객체와 화면 밖으로 잘린 객체는 프로젝트마다 다르게 처리되므로 라벨링 전에 포함 기준과 박스 범위를 문서화해야 한다.
seo_description: >
  가려진 객체와 화면 밖으로 잘린 객체는 프로젝트마다 다르게 처리되므로 라벨링 전에 포함 기준과 박스 범위를 문서화해야 한다.
categories:
  - ko_easy_labeling
tags:
  - Occlusion
  - Truncation
  - Annotation
  - Dataset
---

이미지 라벨링은 박스를 많이 그리는 일이 아니라 **나중에 학습 가능한 기준을 남기는 일**입니다. 이 글은 **가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기** 주제를 Easy Labeling 작업 흐름과 YOLO 데이터셋 검수 관점에서 정리합니다.

가려진 객체와 화면 밖으로 잘린 객체는 프로젝트마다 다르게 처리되므로 라벨링 전에 포함 기준과 박스 범위를 문서화해야 한다.

도구 실행: [Easy Labeling](https://mouseball54.github.io/easy_labeling/)

![가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 라벨링 품질 흐름도](/images/2026-05-23-occlusion-truncation-labeling/hero.png)

## 이 작업이 줄이는 문제

애매한 객체를 그때그때 판단하면 검수자는 틀린 라벨과 다른 기준의 라벨을 구분할 수 없습니다.

이 주제는 라벨을 더 많이 그리는 방법보다 **가림 비율**와 **보이는 박스**를 안정적으로 남기는 방법에 가깝습니다. 객체 탐지 프로젝트에서는 작은 좌표 오류, 클래스 순서 변경, 폴더 구조 실수가 학습 실패처럼 보일 수 있습니다. 그래서 작업자는 도구 사용법과 함께 데이터셋 계약을 문서로 남겨야 합니다.

## 먼저 확인할 품질 신호

- **가림 비율**: 가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **보이는 박스**: 가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **추정 박스**: 가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.
- **예외 예시**: 가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 작업에서 이 항목을 기록하면 라벨 기준이 흔들렸는지 나중에 확인할 수 있습니다.

![가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기 라벨링 검수 체크리스트](/images/2026-05-23-occlusion-truncation-labeling/checklist.png)

## Easy Labeling 적용 흐름

작업은 작은 파일럿 배치에서 시작합니다. 먼저 가림 비율이 어느 정도면 라벨링할지 정합니다. 그 다음 보이는 부분만 그릴지 전체 추정 박스를 그릴지 정합니다. 20~50장 정도의 샘플을 Easy Labeling에서 열어 실제 박스를 그려 보면 지침서의 빈칸이 빨리 드러납니다. 이 단계에서 나온 질문은 채팅으로 흘려보내지 말고 클래스 사전이나 edge case gallery에 반영해야 합니다.

Easy Labeling은 브라우저에서 로컬 이미지 폴더를 열어 YOLO 박스를 작성하는 흐름에 맞춰져 있습니다. 업로드 기반 도구가 부담스러운 파일, 빠르게 확인해야 하는 샘플 배치, 클래스 기준을 실험하는 초기 데이터셋에 특히 잘 맞습니다. 다만 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다.

![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면](/images/easy_labeling_sample.png)

## 검수 예시

검수자는 전체 이미지를 다시 라벨링하지 않아도 됩니다. 샘플을 열고 **가림 비율** 기준이 지켜졌는지, 그리고 **추정 박스**가 프로젝트 규칙과 맞는지 먼저 봅니다. 문제가 반복되면 해당 라벨러의 전체 배치를 의심하기보다 지침서가 충분히 구체적인지, 예시 이미지가 부족한지, 도구 저장 설정이 헷갈리게 되어 있는지 순서대로 확인합니다.

## 실무 체크리스트

- 작업 전 **가림 비율** 기준을 문서에서 확인합니다.
- 파일 저장 후 **보이는 박스**가 실제 라벨 파일에 반영됐는지 샘플로 확인합니다.
- 라벨링 중 생긴 질문은 다음 배치 전에 지침서로 되돌립니다.
- 학습팀에 넘기기 전 이미지, 라벨, 클래스 파일, 검수 기록을 같은 버전으로 묶습니다.

## 자주 묻는 질문

### 가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기는 Easy Labeling만 쓰면 해결되나요?

아닙니다. Easy Labeling은 로컬 이미지와 YOLO 박스를 다루는 작업을 빠르게 만들 수 있지만, **가림 비율** 기준은 프로젝트가 직접 정해야 합니다. 도구와 지침서를 같이 써야 재작업이 줄어듭니다.

### 작은 데이터셋도 이런 검수가 필요한가요?

작은 데이터셋일수록 한두 개 오류가 결과에 크게 보일 수 있습니다. 최소한 **보이는 박스**와 클래스 순서는 샘플로 확인한 뒤 학습으로 넘기는 편이 안전합니다.

### 언제 다시 라벨링해야 하나요?

같은 유형의 오류가 여러 이미지에서 반복되거나 모델 오류 분석에서 특정 클래스가 계속 흔들리면 다시 라벨링해야 합니다. 단순히 박스 하나를 고치는 수준이 아니라 기준 문서를 고친 뒤 같은 기준으로 배치를 다시 보는 것이 좋습니다.


## 참고할 자료

- [Label Studio Bounding Box Template](https://labelstud.io/templates/image_bbox)
- [CVAT Dataset Formats](https://docs.cvat.ai/docs/dataset_management/formats/)
- [FiftyOne Annotation Guide](https://docs.voxel51.com/getting_started/annotation/index.html)

## 함께 보면 좋은 글

- [객체가 없는 이미지도 필요한 이유: YOLO negative sample 설계](/ko_easy_labeling/negative-images-for-detection/)
- [라벨 버전 관리: 데이터셋 v1, v2를 되돌릴 수 있게 만드는 방법](/ko_easy_labeling/label-version-control/)
