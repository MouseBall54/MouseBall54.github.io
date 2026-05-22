---
typora-root-url: ../
layout: single
title: >
  COCO to YOLO 변환 실수: 객체 탐지 라벨이 깨지는 이유
seo_title: >
  COCO to YOLO 변환 실수
date: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: coco-to-yolo-conversion
header:
   teaser: /images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png
   overlay_image: /images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png
   overlay_filter: 0.35
excerpt: >
  COCO annotation을 YOLO format으로 변환할 때 category ID, bbox 좌표, image path, empty image, 시각 검증을 놓치지 않는 방법을 정리합니다.
seo_description: >
  COCO annotation을 YOLO format으로 변환할 때 category ID, bbox 좌표, image path, empty image, 시각 검증을 놓치지 않는 방법을 정리합니다.
categories:
  - ko_easy_labeling
tags:
  - COCO
  - YOLO
  - ComputerVision
  - DataLabeling
  - ObjectDetection
---

## 핵심 요약

COCO to YOLO 변환은 category ID mapping이나 bounding box 변환이 틀릴 때 가장 자주 깨집니다.
COCO bbox는 보통 pixel 단위의 top-left `x`, top-left `y`, `width`, `height`입니다.
YOLO detection label은 image size로 정규화된 `class_id center_x center_y width height`입니다.

![COCO annotation이 YOLO normalized bounding box로 변환되는 흐름 이미지](/images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png)

이미지는 변환 흐름을 보여줍니다.
왼쪽은 source annotation data이고 오른쪽은 normalized YOLO label입니다.
변환 단계에서 class 의미와 box 위치가 보존되어야 합니다.

## COCO와 YOLO는 저장 방식이 다르다

COCO annotation file은 보통 images, annotations, categories가 들어 있는 하나의 JSON 파일입니다.
YOLO detection dataset은 보통 image마다 하나의 `.txt` label file을 사용합니다.

YOLO line format:

```text
class_id center_x center_y width height
```

주요 차이는 다음과 같습니다.

| 영역 | COCO | YOLO |
| --- | --- | --- |
| 파일 구조 | 하나의 JSON file | 이미지별 text file |
| Box format | top-left x, top-left y, width, height | center x, center y, width, height |
| 좌표 단위 | pixels | normalized ratios |
| Category ID | sparse할 수 있음 | 보통 zero-based continuous |

그래서 단순한 text rewrite만으로는 충분하지 않습니다.

## 1. Category ID를 다시 매핑한다

COCO category ID는 항상 `0, 1, 2, 3`이 아닙니다.
`1`부터 시작할 수 있고, 중간 숫자를 건너뛸 수도 있습니다.

YOLO class ID는 보통 zero-based continuous입니다.

```text
0 person
1 car
2 bicycle
```

명시적인 mapping을 만들어야 합니다.

```text
COCO category 1 -> YOLO class 0
COCO category 3 -> YOLO class 1
COCO category 17 -> YOLO class 2
```

COCO category ID가 이미 YOLO class list와 같다는 확신이 없다면 그대로 쓰지 마세요.

## 2. Bounding Box를 정확히 변환한다

COCO bbox:

```text
x_min, y_min, box_width, box_height
```

YOLO는 아래 값을 기대합니다.

```text
center_x, center_y, width, height
```

변환 공식:

```text
center_x = (x_min + box_width / 2) / image_width
center_y = (y_min + box_height / 2) / image_height
width    = box_width / image_width
height   = box_height / image_height
```

변환 후 네 값은 보통 `0`과 `1` 사이여야 합니다.
YOLO label file에 큰 pixel 값이 그대로 있다면 변환이 잘못된 것입니다.

## 3. Image ID와 Filename을 맞춘다

COCO annotation은 `image_id`를 참조합니다.
이 ID를 `images` 목록의 올바른 filename과 연결해야 합니다.

이 부분이 틀리면 전혀 다른 image에 label이 붙습니다.
누락보다 더 위험할 수 있습니다.
training은 진행되지만 잘못된 데이터를 학습할 수 있기 때문입니다.

확인 흐름:

```text
annotation.image_id -> images[id].file_name -> labels/file_name.txt
```

train, validation, test split도 유지해야 합니다.
validation label이 train folder로 들어가지 않게 주의합니다.

## 4. Empty Image 처리

객체가 없는 image가 있을 수 있습니다.
training pipeline이 empty image를 어떻게 기대하는지 정해야 합니다.

- 빈 `.txt` label file
- label file 없음
- image 제외

중요한 것은 일관성입니다.
tool이 empty file을 기대하는데 파일이 없으면 warning이 날 수 있습니다.
반대로 missing file을 기대하는데 잘못된 빈 row를 만들면 training이 실패할 수 있습니다.

## 5. 시각적으로 검증한다

변환 후 sample image를 열어 converted box를 그려 봅니다.

```text
[ ] box가 올바른 객체 위에 있다.
[ ] box가 밀리지 않았다.
[ ] box가 너무 크거나 작지 않다.
[ ] class가 객체와 맞다.
[ ] empty image 처리가 일관적이다.
```

시각 검증은 text validation으로 잡지 못하는 오류를 잡습니다.

## Easy Labeling Workflow

Easy Labeling을 conversion 후 visual check 용도로 사용할 수 있습니다.

```text
1. COCO annotation을 YOLO file로 변환한다.
2. image folder를 연다.
3. class list를 불러온다.
4. YOLO label을 불러온다.
5. class별 sample을 확인한다.
```

도구는 여기에서 사용할 수 있습니다: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## 흔한 실수

첫 번째 실수는 COCO category ID를 그대로 쓰는 것입니다.
모든 class가 밀릴 수 있습니다.

두 번째 실수는 image width와 height로 normalize하지 않는 것입니다.

세 번째 실수는 COCO bbox를 `x_min y_min x_max y_max`로 착각하는 것입니다.
COCO detection bbox는 보통 bottom-right 좌표가 아니라 width와 height를 저장합니다.

네 번째 실수는 다양한 image size를 확인하지 않는 것입니다.
고정 resolution만 가정한 converter는 mixed-size dataset에서 깨질 수 있습니다.

## Easy Labeling 화면 예시

아래 화면처럼 image를 열고 box를 그린 뒤 class를 지정하는 흐름으로 작업합니다.

![Object detection box를 그리는 Easy Labeling sample screen](/images/easy_labeling_sample.png)

## 함께 보면 좋은 글

- [YOLO Label Format 읽는 법](/ko_easy_labeling/yolo-label-format/)
- [Easy Labeling 가이드: 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)
- [COCO dataset format](https://cocodataset.org/#format-data)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## 최종 체크리스트

```text
[ ] Category ID가 YOLO class ID로 remap되었다.
[ ] COCO pixel box가 normalized YOLO center box로 변환되었다.
[ ] Image ID가 올바른 filename과 연결된다.
[ ] Train과 validation split이 섞이지 않았다.
[ ] Empty image 처리가 일관적이다.
[ ] Training 전에 converted label을 시각적으로 확인했다.
```

COCO to YOLO 변환은 mapping이 명확할 때만 단순합니다.
class map과 box formula를 드러내고 실제 image로 검증하세요.
