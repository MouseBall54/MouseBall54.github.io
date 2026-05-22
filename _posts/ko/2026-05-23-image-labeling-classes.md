---
typora-root-url: ../
layout: single
title: >
  이미지 라벨링 클래스 관리법: class name, ID, dataset consistency 지키기
seo_title: >
  이미지 라벨링 클래스 관리법
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: image-labeling-classes
header:
   teaser: /images/2026-05-23-image-labeling-classes/image-labeling-classes-hero.png
   overlay_image: /images/2026-05-23-image-labeling-classes/image-labeling-classes-hero.png
   overlay_filter: 0.35
excerpt: >
  이미지 라벨링 클래스 관리를 위해 안정적인 class ID, naming rule, merge/split 기준, reviewer check, train-validation consistency를 정리합니다.
seo_description: >
  이미지 라벨링 클래스 관리를 위해 안정적인 class ID, naming rule, merge/split 기준, reviewer check, train-validation consistency를 정리합니다.
categories:
  - ko_easy_labeling
tags:
  - ImageLabeling
  - ComputerVision
  - DataLabeling
  - YOLO
  - Dataset
---

## 핵심 요약

이미지 라벨링 클래스 관리는 annotation을 시작하기 전에 정해야 합니다.
class name, 안정적인 class ID, merge/split rule, 예시, 애매한 사례, review check를 먼저 정의해야 합니다.
YOLO label은 numeric ID가 class 의미를 가지므로, 라벨링 후 class 순서를 바꾸면 label이 깨질 수 있습니다.

![안정적인 class ID, sample object, color class, quality check를 보여주는 image labeling class taxonomy 이미지](/images/2026-05-23-image-labeling-classes/image-labeling-classes-hero.png)

이미지는 class management board를 보여줍니다.
각 class에는 고정된 위치, sample example, review check, dataset consistency rule이 있습니다.
이 구조가 나중의 대규모 relabeling을 막습니다.

## 왜 Class 관리가 중요한가

object detection에서 box는 class가 맞을 때만 유용합니다.
한 labeler는 `car`, 다른 labeler는 `vehicle`, 또 다른 labeler는 `sedan`을 사용한다면 model은 일관성 없는 데이터를 학습합니다.

YOLO dataset에서는 문제가 더 엄격합니다.
label file에는 class name이 아니라 numeric class ID가 저장됩니다.
class list 순서가 바뀌면 기존 label이 조용히 다른 class를 가리킬 수 있습니다.

예시:

```text
Before:
0 car
1 truck

After:
0 truck
1 car
```

label text는 바뀌지 않았지만 의미는 바뀝니다.
그래서 class ID는 안정적으로 유지해야 합니다.

## 1. 가장 작은 유용한 Class List로 시작

처음부터 모든 subtype을 만들지 마세요.
model의 실제 목적에 필요한 class부터 시작합니다.

질문:

- model이 이 class들을 구분해야 하는가?
- annotator가 일관되게 구분할 수 있는가?
- class마다 충분한 예시가 있는가?
- production image에도 이 class가 등장하는가?

답이 아니라면 class를 합치거나 나중으로 미룹니다.

## 2. Class Definition 작성

각 class에는 아래 항목이 있어야 합니다.

```text
Class name:
Class ID:
Include:
Exclude:
Ambiguous examples:
Minimum visible area:
Occlusion rule:
```

예시:

```text
Class name: delivery_truck
Include: 물류 운송용 box truck과 delivery van
Exclude: passenger car, bus, bicycle
Ambiguous: cargo 표시가 없는 작은 van
```

definition은 labeler 간 판단 차이를 줄입니다.

## 3. Stable ID 사용

라벨링이 시작된 뒤에는 class ID 순서를 바꾸지 않습니다.
새 class가 필요하면 가능하면 마지막에 추가합니다.

좋은 예:

```text
0 car
1 truck
2 bicycle
3 traffic_light
```

추가:

```text
4 bus
```

위험한 예:

```text
0 bus
1 car
2 truck
3 bicycle
```

이 방식은 모든 label을 migration하지 않으면 의미를 밀어버립니다.

## 4. Merge와 Split Rule 결정

어떤 class는 너무 넓고, 어떤 class는 너무 좁습니다.

class를 split할 때:

- 시각적 차이가 명확하다.
- model이 다른 행동을 해야 한다.
- 충분한 예시가 있다.
- labeler가 rule을 일관되게 적용할 수 있다.

class를 merge할 때:

- labeler disagreement가 잦다.
- model이 구분할 필요가 없다.
- 한 class의 예시가 너무 적다.
- image에서 차이가 보이지 않는다.

결정은 문서화해야 합니다.
각 annotator가 혼자 판단하게 두면 안 됩니다.

## 5. Train과 Validation Consistency 확인

train, validation, test split은 같은 class list를 사용해야 합니다.
validation class order가 다르면 metric은 의미가 없어집니다.

확인:

```text
[ ] 같은 class names
[ ] 같은 class order
[ ] 같은 class IDs
[ ] 같은 merge/split rules
[ ] 같은 empty-image policy
```

여러 source dataset을 합칠 때 특히 중요합니다.

## Easy Labeling Workflow

Easy Labeling에서는 class file을 의도적으로 관리합니다.

```text
1. 라벨링 전 class list를 준비한다.
2. class list를 불러온다.
3. 작은 pilot batch를 라벨링한다.
4. class confusion을 review한다.
5. 대량 작업 전에 class ID를 freeze한다.
6. export 후 sample을 다시 열어 label을 확인한다.
```

도구는 여기에서 사용할 수 있습니다: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## 흔한 실수

첫 번째 실수는 class definition 없이 annotation을 시작하는 것입니다.

두 번째 실수는 기존 label migration 없이 class를 rename하거나 reorder하는 것입니다.

세 번째 실수는 이론적으로만 다르고 실제 image에서는 구분되지 않는 class를 만드는 것입니다.

네 번째 실수는 rare class를 방치하는 것입니다.
예시가 너무 적다면 data를 더 모을지, merge할지, 제거할지 결정해야 합니다.

다섯 번째 실수는 labeler disagreement를 보지 않는 것입니다.
disagreement는 class rule이 불명확하다는 신호입니다.

## Easy Labeling 화면 예시

아래 화면처럼 image를 열고 box를 그린 뒤 class를 지정하는 흐름으로 작업합니다.

![Object detection box를 그리는 Easy Labeling sample screen](/images/easy_labeling_sample.png)

## 함께 보면 좋은 글

- [YOLO Label Format 읽는 법](/ko_easy_labeling/yolo-label-format/)
- [COCO to YOLO 변환 실수](/ko_easy_labeling/coco-to-yolo-conversion/)
- [Easy Labeling 가이드: 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)

## 최종 체크리스트

```text
[ ] Class ID가 안정적으로 유지된다.
[ ] 모든 class에 include/exclude 예시가 있다.
[ ] 애매한 사례에 대한 written rule이 있다.
[ ] split별 class order가 동일하다.
[ ] 새 class는 의도적으로 추가한다.
[ ] 전체 라벨링 전에 pilot batch를 review했다.
```

좋은 라벨링은 첫 box를 그리기 전에 시작됩니다.
class를 정의하고, ID를 고정하고, 애매한 사례를 초기에 review하세요.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

데이터셋을 만들거나 라벨 품질을 일정하게 유지해야 할 때 먼저 적용하면 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 클래스 정의, 예시 이미지, 검수 기준, 파일 내보내기 형식을 먼저 정하세요. 도구보다 라벨 기준이 먼저입니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "이미지 라벨링 클래스 관리법: class name, ID, dataset consistency 지키기" 같은 핵심 문구와 image labeling, dataset, annotation workflow, YOLO, COCO 같은 키워드를 붙이면 도움이 됩니다.
