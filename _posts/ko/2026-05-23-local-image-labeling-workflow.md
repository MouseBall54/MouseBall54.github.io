---
typora-root-url: ../
layout: single
title: >
  로컬 이미지 라벨링 워크플로우: 이미지, 클래스, 라벨, 검수 정리법
seo_title: >
  로컬 이미지 라벨링 워크플로우
date: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: local-image-labeling-workflow
header:
   teaser: /images/2026-05-23-local-image-labeling-workflow/local-image-labeling-workflow-hero.png
   overlay_image: /images/2026-05-23-local-image-labeling-workflow/local-image-labeling-workflow-hero.png
   overlay_filter: 0.35
excerpt: >
  로컬 이미지 라벨링을 folder structure, class file, YOLO label, review batch, backup, train-validation split 기준으로 정리합니다.
seo_description: >
  로컬 이미지 라벨링을 folder structure, class file, YOLO label, review batch, backup, train-validation split 기준으로 정리합니다.
categories:
  - ko_easy_labeling
tags:
  - ImageLabeling
  - YOLO
  - ComputerVision
  - Dataset
  - EasyLabeling
---

## 핵심 요약

로컬 이미지 라벨링 workflow는 raw images, working labels, reviewed labels, exported dataset을 분리해야 합니다.
downloads folder 안에서 바로 라벨링하지 마세요.
예측 가능한 folder structure, 안정적인 class file, review checklist, backup routine이 필요합니다.

![로컬 이미지 폴더에서 class list, annotation, label files, review, dataset export로 이어지는 workflow 이미지](/images/2026-05-23-local-image-labeling-workflow/local-image-labeling-workflow-hero.png)

이미지는 로컬 workflow를 보여줍니다.
이미지는 수집, 라벨링, 검수, export 단계를 거칩니다.
이 과정에서 image filename과 label filename이 계속 짝을 이뤄야 합니다.

## 추천 Folder Structure

아래처럼 시작합니다.

```text
dataset-project/
  raw_images/
  working_images/
  labels_working/
  labels_reviewed/
  classes.txt
  export/
```

`raw_images/`는 원본 보관용으로 둡니다.
라벨링 전에 `working_images/`로 복사합니다.
이렇게 하면 원본 파일을 보호할 수 있습니다.

## 1. Class File 준비

라벨링 전에 class list를 만듭니다.

```text
car
truck
bicycle
chair
bottle
```

YOLO에서는 줄 순서가 중요합니다.
0번째 줄은 class ID 0, 1번째 줄은 class ID 1입니다.
라벨링이 시작된 뒤에는 순서를 바꾸지 않습니다.

새 class가 필요하면 가능하면 마지막에 추가합니다.

## 2. 파일 이름을 예측 가능하게 만든다

가능하면 camera가 만든 random filename을 그대로 쓰지 않습니다.
안정적인 이름을 사용합니다.

```text
road_0001.jpg
road_0002.jpg
warehouse_0001.jpg
```

label file도 맞춰야 합니다.

```text
road_0001.txt
road_0002.txt
warehouse_0001.txt
```

이렇게 해야 깨진 pair를 찾기 쉽습니다.

## 3. 작은 Batch로 라벨링

10,000장을 한 번에 라벨링한 뒤 품질을 확인하면 늦습니다.
먼저 50-100장 정도를 라벨링합니다.
검수합니다.
class rule을 수정합니다.
그 다음 확장합니다.

batch workflow:

```text
1. 작은 batch를 라벨링한다.
2. box tightness와 class consistency를 확인한다.
3. 애매한 class rule을 수정한다.
4. 다음 batch로 넘어간다.
```

작은 batch는 재작업 비용을 줄입니다.

## 4. Export 전 검수

검수 checklist:

```text
[ ] Image와 label filename이 맞다.
[ ] Class ID가 class file과 맞다.
[ ] Box가 충분히 tight하다.
[ ] Occluded object rule이 적용됐다.
[ ] Empty image 처리가 일관적이다.
[ ] Reviewed label을 labels_reviewed로 복사했다.
```

시각 검수가 중요합니다.
text validation만으로는 충분하지 않습니다.

## 5. Train과 Validation Split Export

일반적인 YOLO export 구조:

```text
export/
  images/
    train/
    val/
  labels/
    train/
    val/
  data.yaml
```

image와 label split을 맞춰야 합니다.
image가 `images/val`에 들어가면 label도 `labels/val`에 들어가야 합니다.

label만 image와 따로 split하면 안 됩니다.

## Easy Labeling Workflow

Easy Labeling에서는 다음 흐름을 사용합니다.

```text
1. image folder를 연다.
2. class file을 불러온다.
3. box를 그린다.
4. YOLO label을 저장한다.
5. sample을 다시 열어 label을 확인한다.
6. 검수된 label을 reviewed folder로 옮긴다.
```

도구는 여기에서 사용할 수 있습니다: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## Easy Labeling 화면 예시

아래 화면처럼 image를 열고 box를 그린 뒤 class를 지정하는 흐름으로 작업합니다.

![Object detection box를 그리는 Easy Labeling sample screen](/images/easy_labeling_sample.png)

## 함께 보면 좋은 글

- [YOLO Label Format 읽는 법](/ko_easy_labeling/yolo-label-format/)
- [이미지 라벨링 클래스 관리법](/ko_easy_labeling/image-labeling-classes/)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## 최종 체크리스트

```text
[ ] Raw images가 보존되어 있다.
[ ] Class file이 안정적이다.
[ ] Image와 label filename이 맞다.
[ ] 작은 batch 단위로 검수한다.
[ ] Train과 validation split이 맞다.
[ ] Export folder가 working files와 분리되어 있다.
```

로컬 라벨링은 folder structure가 단순할수록 좋습니다.
구조가 덜 복잡할수록 나중에 training과 debugging이 쉬워집니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

데이터셋을 만들거나 라벨 품질을 일정하게 유지해야 할 때 먼저 적용하면 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 클래스 정의, 예시 이미지, 검수 기준, 파일 내보내기 형식을 먼저 정하세요. 도구보다 라벨 기준이 먼저입니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "로컬 이미지 라벨링 워크플로우: 이미지, 클래스, 라벨, 검수 정리법" 같은 핵심 문구와 image labeling, dataset, annotation workflow, YOLO, COCO 같은 키워드를 붙이면 도움이 됩니다.
