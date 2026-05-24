---
typora-root-url: ../
header:
  teaser: /images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png
  overlay_image: /images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png
  overlay_filter: 0.36
  image_description: >
    이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기
layout: single
title: "Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기"
date: 2025-07-20T00:00:00+09:00
last_modified_at: 2026-05-24T00:00:00+09:00
excerpt: "Easy Labeling 첫 번째 가이드입니다. Detection용 이미지와 라벨 폴더를 불러오고, 클래스 파일을 관리하며, Segmentation 저장 형식도 함께 확인합니다."

seo_description: "Easy Labeling 첫 번째 가이드입니다. Detection용 이미지와 라벨 폴더를 불러오고, 클래스 파일을 관리하며, Segmentation 저장 형식도 함께 확인합니다."
lang: ko
translation_id: easy-labeling-guide-1
categories:
  - ko_easy_labeling
tags:
  - EasyLabeling
  - Guide
  - YOLO
  - DataLabeling
  - Annotation
---


![이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기](/images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png)
<p><strong>Easy Labeling 프로젝트 페이지: <a href="https://mouseball54.github.io/easy_labeling/">https://mouseball54.github.io/easy_labeling/</a></strong></p>

안녕하세요! 이번 글부터 **Easy Labeling** 사용법을 소개합니다. 현재 저장소 기준 Easy Labeling은 YOLO 박스를 다루는 Detection과 브러시 기반 마스크를 다루는 Segmentation을 함께 제공합니다.

그 첫 번째 시간으로, **이미지와 라벨 파일을 불러오는 방법**과 **클래스 설명 파일을 활용하는 방법**을 알아보겠습니다.

---

## 1. 이미지 불러오기

### 1.1 권장 환경

아래 환경에서 사용을 권장합니다.  
> **운영체제**: Windows 10 이상, macOS 10.14 이상  
> **브라우저**: 로컬 폴더 읽기/쓰기에 File System Access API가 필요하므로 Desktop Chrome 또는 Edge 권장  
> **화면 해상도**: 1280×720 이상  

### 1.2 웹사이트 접속
웹 브라우저에서 Easy Labeling 프로젝트 페이지([https://mouseball54.github.io/easy_labeling/](https://mouseball54.github.io/easy_labeling/))로 접속합니다.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720230233737.png" alt="Easy Labeling 초기 화면">
  <figcaption>Figure 1. Easy Labeling 초기 화면. 좌측 상단의 <code>Load Image Folder</code> 버튼을 클릭합니다.</figcaption>
</figure>



### 1.3 이미지 폴더 선택

- <code>Load Image Folder</code> 버튼을 클릭하여 라벨링할 이미지가 저장된 폴더를 선택합니다.

> **(참고)** Easy Labeling은 서버 없이 사용자의 브라우저에서 직접 실행되는 웹 프로그램입니다. 따라서 이미지나 라벨 데이터가 외부로 전송되거나 유출될 걱정 없이 안전하게 사용할 수 있습니다.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720232309611.png" alt="이미지 폴더 선택 화면">
  <figcaption>Figure 2. 이미지 폴더 선택 화면.</figcaption>
</figure>



### 1.4 라벨 폴더 생성

- 선택한 이미지 폴더에 <code>label</code> 폴더가 없으면 생성 여부를 묻는 알림창이 표시됩니다.  
- “확인”을 누르면 자동으로 <code>label</code> 폴더가 생성되고, 향후 라벨 데이터가 해당 폴더에 저장됩니다.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720230951821.png" alt="label 폴더 생성 확인">
  <figcaption>Figure 3. <code>label</code> 폴더 생성 확인 창.</figcaption>
</figure>

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720231126118.png" alt="이미지 및 라벨 폴더 로딩 완료">
  <figcaption>Figure 4. 이미지 및 라벨 폴더 로딩 완료. 버튼이 <code>label (created)</code>로 변경됩니다.</figcaption>
</figure>



---

## 2. 이미지 전환 방법

Easy Labeling은 빠른 작업을 위해 다양한 전환 방법을 제공합니다. 편하신 방법을 선택하여 효율성을 높이십시오.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720235716476.png" alt="다양한 이미지 전환 방법">
  <figcaption>Figure 5. 다양한 이미지 전환 방법.</figcaption>
</figure>


- **방법 1**: 좌측 <code>Image Files</code> 목록에서 원하는 이미지를 직접 클릭  
- **방법 2**: 상단 화살표 아이콘 (<code>◀</code>, <code>▶</code>) 클릭  
- **방법 3**: <code>Image Previews</code> 창의 미리보기나 화살표 클릭  
- **방법 4**: 키보드 단축키 <code>A</code>(이전), <code>D</code>(다음) 사용  

---

## 3. 라벨 데이터 불러오기 및 관리

### 3.1 라벨 폴더 불러오기
기존에 작업하던 라벨 데이터를 불러오거나 다른 위치의 폴더를 사용하려면 다음 방식을 참고하십시오.

1. <code>label</code> 폴더가 없으면 자동 생성 (<code>label (created)</code>)  
2. 폴더가 이미지 폴더 하위에 있으면 자동 불러오기 (<code>label (auto)</code>)  
3. 수동 지정: <code>Load Label Folder</code> 버튼 클릭

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png" alt="수동으로 라벨 폴더 지정하기">
  <figcaption>Figure 6. 수동으로 라벨 폴더 지정 화면.</figcaption>
</figure>


- <code>Search files...</code>: 파일 이름 일부로 검색  
- <code>Labeled</code> / <code>Unlabeled</code> 필터로 라벨 유무별로 분류  

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720233244263.png" alt="Labeled 필터 적용 화면">
  <figcaption>Figure 7. <code>Labeled</code> 필터 적용 화면.</figcaption>
</figure>


### 3.2 라벨 데이터 관리 기능
<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250721010743987.png" alt="라벨 데이터 관리 기능">
  <figcaption>Figure 8. 라벨 데이터 관리 메뉴 (<code>Auto Save</code>, <code>Save Labels</code>, <code>Download Class Template</code>).</figcaption>
</figure>


- <code>Auto Save</code>: 이미지 전환 시 자동 저장  
- <code>Save Labels</code> (<code>Ctrl + S</code>): 수동 저장  
- <code>Download Class Template</code>: <code>custom-classes.yaml</code> 템플릿 다운로드  

---

## 4. 클래스 설명 파일 활용

다운로드한 <code>custom-classes.yaml</code> 파일은 다음 형식으로 제공됩니다. 원하는 클래스 ID와 이름을 수정하십시오.

```yaml
# This is a YAML file for class definitions.
# Each line should be in the format: id: name
# The ID must be an integer.

0: person
1: car
2: bicycle
3: dog
10: traffic light
```

이 파일을 수정하여 자신만의 클래스 목록을 만들면, 라벨링 시 클래스 번호 대신 지정한 이름(person, car 등)이 표시되어 훨씬 직관적으로 작업할 수 있습니다. 현재 저장소에는 클래스 파일 선택과 생성/편집 모달도 문서화되어 있으므로, 여러 데이터셋이 비슷한 클래스 이름을 쓸 때는 YAML 파일을 버전으로 관리하는 편이 좋습니다.



이번 글에서는 이미지 폴더를 열고, Detection용 `label` 폴더를 만들거나 불러오며, 클래스 파일을 사용하는 기본 흐름을 정리했습니다. 프로젝트가 마스크를 필요로 한다면 Segmentation 워크플로우를 별도로 열고 `mask/<image>.png`, `mask/<image>.seg.json` 저장 여부를 확인해야 합니다.

대량 작업 전에는 Desktop Chrome 또는 Edge에서 작은 파일럿 배치를 실행하고 저장 폴더가 예상대로 만들어지는지 먼저 확인하세요.

------

## 5. FAQ 및 팁

### FAQ

**Q1. 이미지 폴더가 로드되지 않습니다.**
 A. 지원되는 확장자(.jpg, .png, .bmp,tiff 등)를 사용하는지 확인하고,
 브라우저의 폴더 접근 권한을 허용했는지 점검하십시오.

**Q2. 라벨 폴더 생성 창이 나타나지 않습니다.**
 A. 브라우저 팝업 차단 설정을 해제한 후 <code>Load Image Folder</code>를 다시 실행하십시오.



### Tips

- 라벨링 전 <code>Ctrl + S</code>로 수동 저장을 권장합니다.
- 클래스 템플릿을 Git 등 버전 관리 시스템으로 관리하여 협업 시 일관성을 유지하십시오.

------

## 참고할 자료

- [Easy Labeling GitHub 저장소](https://github.com/MouseBall54/easy_labeling): 현재 기능 범위, Detection/Segmentation 워크플로우, 저장 형식, 브라우저 조건, Electron 빌드 참고 자료입니다.
- [MDN File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API): 브라우저에서 로컬 폴더를 여는 방식의 기본 자료입니다.
- [Ultralytics Object Detection Dataset Docs](https://docs.ultralytics.com/datasets/detect/): YOLO 폴더 구조, `data.yaml`, 라벨 형식을 확인할 때 참고할 공식 문서입니다.
- [CVAT YOLO Format](https://docs.cvat.ai/docs/dataset_management/formats/format-yolo/): YOLO annotation 형식을 다른 도구와 비교할 때 참고할 수 있습니다.

---
## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [Easy Labeling 개발기: 로컬 Detection과 Segmentation 주석 도구](/ko_easy_labeling/easy-labeling-development/)
- [YOLO 라벨링을 위한 Easy Labeling 주요 기능](/ko_easy_labeling/easy-labeling-in-depth-features/)
