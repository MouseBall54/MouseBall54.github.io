---
typora-root-url: ../
layout: single
title: >
  YOLO Label Format 읽는 법: class, center x, center y, width, height 이해하기
seo_title: >
  YOLO Label Format 읽는 법
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: yolo-label-format
header:
   teaser: /images/2026-05-23-yolo-label-format/yolo-label-format-hero.png
   overlay_image: /images/2026-05-23-yolo-label-format/yolo-label-format-hero.png
   overlay_filter: 0.35
   image_description: >
     YOLO Label Format 읽는 법: class, center x, center y, width, height 이해하기 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  YOLO 객체 탐지 라벨 형식인 class id, center x, center y, width, height를 정규화 좌표 기준으로 읽고 검증하는 방법을 정리합니다.
seo_description: >
  YOLO 객체 탐지 라벨 형식인 class id, center x, center y, width, height를 정규화 좌표 기준으로 읽고 검증하는 방법을 정리합니다.
categories:
  - ko_easy_labeling
tags:
  - YOLO
  - ComputerVision
  - DataLabeling
  - ObjectDetection
  - EasyLabeling
---

## 핵심 요약

YOLO object detection label은 보통 이미지마다 하나의 `.txt` 파일로 저장됩니다.
각 줄은 객체 하나를 뜻합니다.
일반적인 형식은 다음과 같습니다.

```text
class_id center_x center_y width height
```

네 개의 box 값은 normalized value입니다.
즉 pixel 값이 아니라 이미지 width와 height를 기준으로 `0`부터 `1` 사이의 비율로 표현합니다.

![Bounding box, 중심점, width와 height 화살표, 추상 라벨 행으로 표현한 YOLO label format 이미지](/images/2026-05-23-yolo-label-format/yolo-label-format-hero.png)

이미지는 핵심 개념을 보여줍니다.
객체 주변에 bounding box가 있고, 라벨은 class와 box 위치를 center point, width, height로 저장합니다.

## 기본 예시

이미지에 bottle 객체 하나가 있다고 가정합니다.
라벨 파일에는 다음과 같은 줄이 들어갈 수 있습니다.

```text
0 0.500000 0.520000 0.250000 0.640000
```

읽는 방법은 다음과 같습니다.

| 값 | 의미 |
| --- | --- |
| `0` | class id |
| `0.500000` | center x 위치 |
| `0.520000` | center y 위치 |
| `0.250000` | bounding box width |
| `0.640000` | bounding box height |

class id는 index입니다.
class list가 아래와 같다면:

```text
0 bottle
1 cup
2 box
```

class id `0`은 `bottle`을 뜻합니다.

## 이미지 하나, 라벨 파일 하나

YOLO dataset에서는 image file과 label file이 보통 같은 base name을 가집니다.

```text
images/train/photo_001.jpg
labels/train/photo_001.txt
```

`photo_001.jpg`에 객체가 세 개 있으면 `photo_001.txt`에는 세 줄이 들어갑니다.
객체가 없는 이미지라면 label file을 비워 두거나 생략할 수 있는데, 이는 training pipeline의 기대 방식에 따라 다릅니다.
사용하는 tool과 training code의 기준을 확인해야 합니다.

## 왜 좌표를 정규화하는가

YOLO는 training 중 image resize가 일어나도 label이 유지되도록 normalized coordinate를 사용합니다.
예를 들어 `center_x = 0.5`는 이미지의 가로 중앙을 뜻합니다.
이미지가 `640x480`이든 `1280x720`이든 의미는 같습니다.

변환 공식은 다음과 같습니다.

```text
center_x = box_center_x_in_pixels / image_width
center_y = box_center_y_in_pixels / image_height
width    = box_width_in_pixels / image_width
height   = box_height_in_pixels / image_height
```

다시 pixel로 바꾸려면:

```text
box_width_pixels  = width * image_width
box_height_pixels = height * image_height
```

라벨링 실수는 여기서 자주 발생합니다.
YOLO text file에 pixel 값을 그대로 넣는 경우입니다.
보통 값은 `0`과 `1` 사이여야 하므로, `340 220 120 80` 같은 값은 잘못된 형식일 가능성이 큽니다.

## Corner Format이 아니라 Center Format

YOLO label은 center format을 사용합니다.
반면 많은 annotation tool과 image library는 corner format을 사용합니다.

```text
x_min y_min x_max y_max
```

corner coordinate를 YOLO format으로 바꾸려면:

```text
box_width  = x_max - x_min
box_height = y_max - y_min
center_x   = x_min + box_width / 2
center_y   = y_min + box_height / 2
```

그 다음 image width와 height로 나누어 정규화합니다.

COCO, Pascal VOC, custom CSV annotation에서 변환할 때 이 부분을 특히 조심해야 합니다.
좌표 변환이 틀리면 box가 밀리거나, 너무 크거나, 너무 작게 보입니다.

## Class ID는 Class List와 반드시 맞아야 한다

label file에는 class name이 아니라 numeric class id만 저장됩니다.
class name은 보통 dataset configuration file이나 class list에 있습니다.

예를 들어:

```text
0 car
1 bus
2 truck
```

나중에 class list 순서를 바꾸면 기존 label이 틀어질 수 있습니다.
원래 `car`였던 label이 갑자기 `bus`가 될 수 있습니다.

기본 규칙은 다음과 같습니다.

```text
라벨링을 시작한 뒤에는 class ID 순서를 바꾸지 않는다.
새 class는 가능하면 마지막에 추가한다.
```

여러 사람이 함께 labeling할 때 특히 중요합니다.

## 흔한 YOLO Label 실수

첫 번째 실수는 normalized coordinate 대신 pixel coordinate를 쓰는 것입니다.
값이 `340 220 120 80`처럼 크다면 YOLO format이 아닐 가능성이 큽니다.

두 번째 실수는 center coordinate 대신 top-left corner coordinate를 넣는 것입니다.
YOLO는 box의 왼쪽 위가 아니라 중심점을 기대합니다.

세 번째 실수는 image와 label filename이 맞지 않는 것입니다.
`photo_001.jpg`는 `photo_001.txt`와 맞아야 합니다.

네 번째 실수는 class id drift입니다.
label을 만든 뒤 class list 순서가 바뀔 때 발생합니다.

다섯 번째 실수는 box를 너무 느슨하게 그리는 것입니다.
object detection label은 보이는 객체를 충분히 감싸야 하지만, 불필요한 배경을 많이 포함하면 품질이 떨어집니다.

## 검증 체크리스트

training 전에 몇 장을 샘플로 열어 확인합니다.

```text
[ ] 모든 image에 기대한 label file이 있다.
[ ] 객체 한 줄은 값 5개를 가진다.
[ ] class ID가 class list에 존재한다.
[ ] coordinate 값은 0과 1 사이이다.
[ ] box가 올바른 객체 위에 표시된다.
[ ] resize 후 box가 밀리지 않는다.
[ ] empty image 처리 방식이 일관적이다.
```

시각적 검증은 중요합니다.
텍스트로는 맞아 보여도 box가 실제 위치와 어긋날 수 있습니다.

## Easy Labeling Workflow

Easy Labeling을 사용할 때 기본 흐름은 다음과 같습니다.

```text
1. image folder를 불러온다.
2. class list를 불러오거나 정의한다.
3. 객체 주변에 box를 그린다.
4. YOLO format으로 label을 저장한다.
5. sample image를 다시 열어 box 위치를 확인한다.
```

검증 단계는 수백 장을 라벨링하기 전에 반드시 하는 편이 좋습니다.
class 순서 실수와 coordinate export 문제를 초기에 잡을 수 있습니다.

도구는 여기에서 사용할 수 있습니다: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## Easy Labeling 화면 예시

아래 화면처럼 image를 열고 box를 그린 뒤 class를 지정하는 흐름으로 작업합니다.

![Object detection box를 그리는 Easy Labeling sample screen](/images/easy_labeling_sample.png)

## 함께 보면 좋은 글

- [Easy Labeling 가이드: 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)
- [Easy Labeling 상세 기능 소개](/ko_easy_labeling/easy-labeling-in-depth-features/)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## 마무리

YOLO label format은 단순하지만 엄격합니다.
한 줄은 객체 하나입니다.
순서는 class id, center x, center y, width, height입니다.
box 값은 pixel이 아니라 normalized value입니다.

이 규칙을 기억하고 training 전에 시각적으로 확인하면 object detection dataset 문제를 많이 줄일 수 있습니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

데이터셋을 만들거나 라벨 품질을 일정하게 유지해야 할 때 먼저 적용하면 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 클래스 정의, 예시 이미지, 검수 기준, 파일 내보내기 형식을 먼저 정하세요. 도구보다 라벨 기준이 먼저입니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "YOLO Label Format 읽는 법: class, center x, center y, width, height 이해하기" 같은 핵심 문구와 image labeling, dataset, annotation workflow, YOLO, COCO 같은 키워드를 붙이면 도움이 됩니다.
