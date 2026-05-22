---
typora-root-url: ../
layout: single
title: >
  Easy Labeling으로 YOLO 데이터셋 만들기: 이미지에서 학습 폴더까지
seo_title: >
  Easy Labeling으로 YOLO 데이터셋 만들기
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: easy-labeling-yolo-dataset
header:
   teaser: /images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png
   overlay_image: /images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png
   overlay_filter: 0.35
excerpt: >
  Easy Labeling으로 YOLO object detection dataset을 만들 때 image 준비, class 관리, label 저장, train-validation split, data.yaml 검증까지 정리합니다.
seo_description: >
  Easy Labeling으로 YOLO object detection dataset을 만들 때 image 준비, class 관리, label 저장, train-validation split, data.yaml 검증까지 정리합니다.
categories:
  - ko_easy_labeling
tags:
  - EasyLabeling
  - YOLO
  - ImageLabeling
  - ComputerVision
  - Dataset
---

## 핵심 요약

Easy Labeling으로 YOLO dataset을 만들 때는 안정적인 class list를 먼저 준비하고, 작은 batch로 image를 라벨링하고, image마다 YOLO `.txt` label file을 저장한 뒤, sample을 시각적으로 검수하고, `images/train`, `images/val`, `labels/train`, `labels/val` 구조로 export해야 합니다.
가장 중요한 원칙은 일관성입니다.
Class ID, image name, label name, train-validation split이 계속 맞아야 합니다.

![image folder와 class list에서 label, review, data.yaml, training folder로 이어지는 Easy Labeling YOLO dataset workflow 이미지](/images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png)

이미지는 전체 흐름을 보여줍니다.
Easy Labeling은 annotation 단계를 쉽게 해주지만, dataset quality는 명확한 class, 반복 검수, 예측 가능한 export structure에 달려 있습니다.

## 추천 Project Folder

아래처럼 단순하게 시작합니다.

```text
yolo-dataset-project/
  raw_images/
  working_images/
  labels/
  classes.txt
  export/
```

`raw_images/`는 원본 보관용입니다.
backup 뒤에는 이 파일들을 직접 수정하거나 이름을 바꾸지 않습니다.
라벨링할 파일만 `working_images/`로 복사합니다.

이렇게 하면 작업을 다시 시작해야 할 때도 복구하기 쉽습니다.

## 1. Class List 준비

라벨링 전에 `classes.txt`를 만듭니다.

```text
helmet
vest
glove
person
forklift
```

YOLO class ID는 줄 순서로 정해집니다.
첫 번째 줄은 class `0`, 두 번째 줄은 class `1`입니다.
라벨링이 시작된 뒤에는 이 파일의 순서를 바꾸지 않습니다.

새 class가 필요하면 가능하면 마지막 줄에 추가하세요.
순서를 바꾸면 기존 label이 조용히 망가질 수 있습니다.

## 2. Easy Labeling에서 이미지 라벨링

Easy Labeling에서는 다음 흐름으로 작업합니다.

```text
1. Working image folder를 연다.
2. Class list를 불러오거나 만든다.
3. 대상 object 주변에 bounding box를 그린다.
4. 올바른 class를 지정한다.
5. YOLO format으로 label을 저장한다.
6. 저장된 image 몇 장을 다시 열어 box와 class를 확인한다.
```

도구는 여기에서 열 수 있습니다: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

![Object detection box를 그리는 Easy Labeling sample screen](/images/easy_labeling_sample.png)

모든 image에 같은 labeling rule을 적용해야 합니다.
예를 들어 일부가 가려진 object를 라벨링할지 먼저 정해야 합니다.
애매한 rule은 noisy training data를 만듭니다.

## 3. YOLO Label File 확인

YOLO detection label file은 아래 구조를 사용합니다.

```text
class_id x_center y_center width height
```

예시:

```text
0 0.512500 0.433333 0.180000 0.260000
3 0.720000 0.510000 0.120000 0.300000
```

좌표는 `0`부터 `1`까지 정규화된 값입니다.
pixel 값이 아닙니다.
Ultralytics 문서도 YOLO detection dataset에서 정규화된 `class x_center y_center width height` 패턴을 설명합니다.

자세한 형식은 [YOLO Label Format 읽는 법](/ko_easy_labeling/yolo-label-format/)과 [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)을 함께 확인하세요.

## 4. Split 전에 검수

수백 장을 라벨링하기 전에 작은 batch를 먼저 검수합니다.

확인할 것:

```text
[ ] Box가 충분히 tight하다.
[ ] Class ID가 classes.txt와 맞다.
[ ] 비슷한 object에 같은 class를 사용한다.
[ ] Empty image 처리가 의도적이다.
[ ] Label filename이 image filename과 맞다.
[ ] 어려운 예외 case가 문서화되어 있다.
```

검수는 선택이 아닙니다.
label이 일관되지 않으면 training이 조용히 실패할 수 있습니다.

## 5. Train과 Validation Folder Export

최종 dataset은 아래 구조를 권장합니다.

```text
dataset/
  images/
    train/
    val/
  labels/
    train/
    val/
  data.yaml
```

`images/train/photo_001.jpg`가 있다면 label은 아래 위치에 있어야 합니다.

```text
labels/train/photo_001.txt
```

`images/val/photo_101.jpg`가 있다면 label은 아래 위치에 있어야 합니다.

```text
labels/val/photo_101.txt
```

Image와 label을 함께 split하세요.
Image를 먼저 나누고 label을 따로 나누면 안 됩니다.

## 6. `data.yaml` 작성

최소 `data.yaml`은 아래처럼 만들 수 있습니다.

```yaml
path: dataset
train: images/train
val: images/val
names:
  0: helmet
  1: vest
  2: glove
  3: person
  4: forklift
```

`names` 순서는 `classes.txt`와 맞아야 합니다.
순서가 다르면 model이 잘못된 object name을 학습할 수 있습니다.

## 7. 짧은 Verification Pass 실행

전체 training 전에 dataset을 확인합니다.

```text
[ ] Train image 10장을 label과 함께 열어본다.
[ ] Validation image 10장을 label과 함께 열어본다.
[ ] 모든 label file row가 유효한 숫자인지 확인한다.
[ ] 의도적으로 empty image가 아닌데 label이 없는 image가 없는지 확인한다.
[ ] 환경이 준비되어 있다면 짧은 training dry run을 실행한다.
```

이 단계에서 대부분의 dataset 실수를 잡을 수 있습니다.

## 함께 보면 좋은 글

- [로컬 이미지 라벨링 워크플로우](/ko_easy_labeling/local-image-labeling-workflow/)
- [이미지 라벨링 클래스 관리법](/ko_easy_labeling/image-labeling-classes/)
- [YOLO Label Format 읽는 법](/ko_easy_labeling/yolo-label-format/)
- [Easy Labeling](https://mouseball54.github.io/easy_labeling/)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## 최종 체크리스트

```text
[ ] Raw images가 backup되어 있다.
[ ] classes.txt가 안정적이다.
[ ] Easy Labeling이 YOLO label file을 저장한다.
[ ] Image와 label filename이 맞다.
[ ] Train과 validation split이 맞다.
[ ] data.yaml이 class list와 맞다.
[ ] 시각 sample review가 끝났다.
```

좋은 YOLO dataset은 image가 많이 들어 있는 folder가 아닙니다.
첫 image부터 training run까지 class definition, label file, export folder가 일관되게 유지되는 반복 가능한 labeling process입니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

데이터셋을 만들거나 라벨 품질을 일정하게 유지해야 할 때 먼저 적용하면 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 클래스 정의, 예시 이미지, 검수 기준, 파일 내보내기 형식을 먼저 정하세요. 도구보다 라벨 기준이 먼저입니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Easy Labeling으로 YOLO 데이터셋 만들기: 이미지에서 학습 폴더까지" 같은 핵심 문구와 image labeling, dataset, annotation workflow, YOLO, COCO 같은 키워드를 붙이면 도움이 됩니다.
