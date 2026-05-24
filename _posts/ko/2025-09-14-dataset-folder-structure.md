---
layout: single
title: >
  객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기
seo_title: >
  객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기
date: 2025-09-14T08:23:00+09:00
last_modified_at: 2026-05-24T00:00:00+09:00
lang: ko
translation_id: dataset-folder-structure
header:
  teaser: /images/2026-05-23-dataset-folder-structure/hero.png
  overlay_image: /images/2026-05-23-dataset-folder-structure/hero.png
  overlay_filter: 0.36
  image_description: >
    객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기의 이미지 라벨링 흐름과 검수 기준을 요약한 이미지입니다.
excerpt: >
  객체 탐지 데이터셋은 이미지와 라벨의 상대 위치가 맞아야 하며 train, val, test 폴더가 서로 섞이지 않아야 한다.
seo_description: >
  객체 탐지 데이터셋은 이미지와 라벨의 상대 위치가 맞아야 하며 train, val, test 폴더가 서로 섞이지 않아야 한다.
categories:
  - ko_easy_labeling
tags:
  - FolderStructure
  - YOLO
  - Dataset
  - Validation
---
이 글은 **객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기**를 라벨링 속도가 아니라 데이터셋 품질 기준으로 정리합니다. Easy Labeling은 작업을 빠르게 만들 수 있지만, 학습 가능한 데이터는 클래스 규칙과 검수 루틴이 함께 있을 때 만들어집니다.

객체 탐지 데이터셋은 이미지와 라벨의 상대 위치가 맞아야 하며 train, val, test 폴더가 서로 섞이지 않아야 한다.

도구 실행: [Easy Labeling](https://mouseball54.github.io/easy_labeling/)

![객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기 라벨링 품질 흐름도](/images/2026-05-23-dataset-folder-structure/hero.png)

## 이 작업이 줄이는 문제

폴더 구조 오류는 모델 코드 문제가 아니라 데이터 패키징 문제인 경우가 많습니다.

이 주제는 라벨을 더 많이 그리는 방법보다 **images 폴더**와 **labels 폴더**를 안정적으로 남기는 방법에 가깝습니다. 객체 탐지 프로젝트에서는 작은 좌표 오류, 클래스 순서 변경, 폴더 구조 실수가 학습 실패처럼 보일 수 있습니다. 그래서 작업자는 도구 사용법과 함께 데이터셋 계약을 문서로 남겨야 합니다.

## 먼저 확인할 품질 신호

- **images 폴더**: 작업 전에 기준을 문서로 고정합니다. 라벨러가 같은 이미지를 봤을 때 같은 결정을 내릴 수 있도록 포함 기준, 제외 기준, 예외 예시를 함께 둡니다.
- **labels 폴더**: 파일럿 배치에서 바로 확인합니다. 전체 데이터를 열기 전에 20~50장 샘플로 좌표, 클래스, 저장 경로가 학습 폴더와 맞는지 봅니다.
- **고아 라벨**: 애매한 사례를 질문 로그나 edge case gallery에 남깁니다. 반복 질문이 생기면 개인 판단으로 넘기지 말고 지침서 버전을 올립니다.
- **상대경로**: 학습팀에 넘기기 전 검수 기록과 함께 묶습니다. 이미지, 라벨, 클래스 파일, 변환 스크립트, 검수 샘플이 같은 버전을 가리켜야 합니다.

![객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기 라벨링 검수 체크리스트](/images/2026-05-23-dataset-folder-structure/checklist.png)

## Easy Labeling 적용 흐름

작업은 작은 파일럿 배치에서 시작합니다. 먼저 이미지와 라벨 폴더를 같은 분할 이름으로 맞춥니다. 그 다음 라벨 파일이 없는 이미지와 이미지가 없는 라벨을 찾습니다. 20~50장 정도의 샘플을 Easy Labeling에서 열어 실제 박스를 그려 보면 지침서의 빈칸이 빨리 드러납니다. 이 단계에서 나온 질문은 채팅으로 흘려보내지 말고 클래스 사전이나 edge case gallery에 반영해야 합니다.

Easy Labeling은 로컬 우선 이미지 주석 작업에 맞춰져 있습니다. 현재 저장소 기준 Detection은 YOLO bounding box를, Segmentation은 브러시 기반 마스크를 다루므로 라벨링 전에 데이터셋 계약에 맞는 탭을 먼저 정해야 합니다. 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다.


## 저장소 기준 기능 범위

현재 Easy Labeling은 YOLO 박스 전용 편집기만은 아닙니다. 저장소 README 기준 상단에는 `Detection`과 `Segmentation` 두 워크플로우 탭이 있습니다. Detection은 YOLO bounding box를 다루고 `label/<image>.txt`로 저장합니다. Segmentation은 브러시 기반 마스크를 다루며 `mask/<image>.png`와 `mask/<image>.seg.json`을 저장합니다.

브라우저 버전은 로컬 폴더 읽기/쓰기에 File System Access API가 필요하므로 Desktop Chrome 또는 Edge 사용을 전제로 보는 편이 안전합니다. 저장소에는 Windows용 Electron 빌드도 문서화되어 있습니다. 박스 목록 기반 다중 편집, 정렬, 분배, 복사/붙여넣기는 Detection 중심 기능으로 보고, Segmentation은 브러시, 지우개, 연결 영역 선택, 드래그 이동, 클래스 변경 중심으로 검수해야 합니다.

![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면](/images/easy_labeling_sample.png)

## 검수 예시

검수자는 전체 이미지를 다시 라벨링하지 않아도 됩니다. 샘플을 열고 **images 폴더** 기준이 지켜졌는지, 그리고 **고아 라벨**가 프로젝트 규칙과 맞는지 먼저 봅니다. 문제가 반복되면 해당 라벨러의 전체 배치를 의심하기보다 지침서가 충분히 구체적인지, 예시 이미지가 부족한지, 도구 저장 설정이 헷갈리게 되어 있는지 순서대로 확인합니다.

## 실무 체크리스트

- 작업 전 **images 폴더** 기준을 문서에서 확인합니다.
- 파일 저장 후 **labels 폴더**가 실제 라벨 파일에 반영됐는지 샘플로 확인합니다.
- 라벨링 중 생긴 질문은 다음 배치 전에 지침서로 되돌립니다.
- 학습팀에 넘기기 전 이미지, 라벨, 클래스 파일, 검수 기록을 같은 버전으로 묶습니다.

## 자주 묻는 질문

### 객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기는 Easy Labeling만 쓰면 해결되나요?

아닙니다. Easy Labeling은 로컬 Detection 박스 작업을 빠르게 만들고 Segmentation 마스크 작업도 제공하지만, **images 폴더** 기준은 프로젝트가 직접 정해야 합니다. 도구와 지침서를 같이 써야 재작업이 줄어듭니다.

### 작은 데이터셋도 이런 검수가 필요한가요?

작은 데이터셋일수록 한두 개 오류가 결과에 크게 보일 수 있습니다. 최소한 **labels 폴더**와 클래스 순서는 샘플로 확인한 뒤 학습으로 넘기는 편이 안전합니다.

### 언제 다시 라벨링해야 하나요?

같은 유형의 오류가 여러 이미지에서 반복되거나 모델 오류 분석에서 특정 클래스가 계속 흔들리면 다시 라벨링해야 합니다. 단순히 박스 하나를 고치는 수준이 아니라 기준 문서를 고친 뒤 같은 기준으로 배치를 다시 보는 것이 좋습니다.


## 참고할 자료

- [Easy Labeling GitHub 저장소](https://github.com/MouseBall54/easy_labeling): 현재 기능 범위, Detection/Segmentation 워크플로우, 저장 형식, 브라우저 조건, Electron 빌드 참고 자료입니다.
- [Ultralytics Object Detection Dataset Docs](https://docs.ultralytics.com/datasets/detect/)
- [CVAT YOLO Format](https://docs.cvat.ai/docs/dataset_management/formats/format-yolo/)
- [Ultralytics Simple Utilities](https://docs.ultralytics.com/usage/simple-utilities/)

## 함께 보면 좋은 글

- [모델 오류 분석으로 라벨링 개선하기: 오탐과 미탐을 다음 작업으로 바꾸기](/ko_easy_labeling/model-error-analysis-labeling/)
- [라벨러 온보딩 체크리스트: 첫날부터 같은 기준으로 작업하게 만들기](/ko_easy_labeling/labeler-onboarding-checklist/)
