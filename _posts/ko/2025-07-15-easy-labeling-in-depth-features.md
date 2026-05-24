---
typora-root-url: ../
layout: single
header:
  teaser: /images/2025-07-15-introducing-easy-labeling-in-depth-features/image-20250715235507837.png
  overlay_image: /images/2025-07-15-introducing-easy-labeling-in-depth-features/image-20250715235507837.png
  overlay_filter: 0.36
  image_description: >
    이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: YOLO 라벨링을 위한 Easy Labeling 주요 기능
title: "YOLO 라벨링을 위한 Easy Labeling 주요 기능"
date: 2025-07-15T00:00:00+09:00
last_modified_at: 2026-05-24T00:00:00+09:00
excerpt: "AI 객체 탐지를 위한 YOLO 데이터 라벨링, 아직도 힘드신가요? Easy Labeling의 강력한 기능으로 데이터셋 구축 시간을 단축하세요. 로컬 파일 연동, 고급 Annotation 기능, 효율적인 단축키 등 YOLO 라벨링 생산성을 극대화하는 모든 비법을 공개합니다."

seo_description: "AI 객체 탐지를 위한 YOLO 데이터 라벨링, 아직도 힘드신가요? Easy Labeling의 강력한 기능으로 데이터셋 구축 시간을 단축하세요. 로컬 파일 연동, 고급 Annotation 기능, 효율적인 단축키 등 YOLO 라벨링 생산성을 극대화하는 모든 비법을 공개합니다."
lang: ko
translation_id: easy-labeling-in-depth-features
categories:
  - ko_easy_labeling
tags:
  - EasyLabeling
  - Features
  - YOLO
  - ComputerVision
  - Annotation
---

안녕하세요! 오늘은 객체 탐지(Object Detection) 데이터셋을 만드는 과정을 획기적으로 개선해 줄 강력한 이미지 주석(Annotation) 도구, **Easy Labeling**의 주요 기능들을 상세하게 소개해 드리고자 합니다.

현재 저장소 기준 Easy Labeling은 Detection과 Segmentation 두 워크플로우 탭을 제공합니다. 이 글은 Detection 중심 생산성 기능을 주로 설명하되, 마스크 작업은 다른 흐름으로 검수해야 한다는 점도 함께 반영합니다.

![image-20250715235317783](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235317783.png)

## 1. 서버가 필요 없는 완벽한 로컬 환경 지원

Easy Labeling의 가장 큰 특징 중 하나는 **별도의 서버나 파일 업로드 과정 없이** 사용자의 컴퓨터에 있는 파일을 직접 열어 작업할 수 있다는 점입니다. 최신 웹 기술인 File System Access API를 활용하여 보안은 지키면서 로컬 폴더에 바로 접근해 이미지와 라벨 파일을 불러오고 저장합니다.

-   **빠른 속도:** 파일을 업로드하고 다운로드하는 시간이 없어 대용량 데이터셋도 빠르게 처리할 수 있습니다.
-   **강력한 보안:** 모든 데이터는 사용자의 컴퓨터 안에서만 처리되므로 민감한 데이터도 안심하고 다룰 수 있습니다.

## 2. 직관적이고 강력한 주석(Annotation) 도구

Easy Labeling은 박스 주석과 마스크 주석을 구분해 다룰 수 있는 도구를 제공합니다.

-   **Detection 박스 편집:** YOLO 박스를 그리고, 크기 조정, 이동, 삭제, 복사, 붙여넣기, 정렬, 분배, 클래스 변경을 할 수 있습니다.
-   **Segmentation 마스크 편집:** 브러시와 지우개로 마스크를 편집하고, 연결 영역을 옮기거나 선택 영역의 클래스를 바꿀 수 있습니다.
-   **정밀한 제어:** 확대/축소, pan, crosshair, `Ctrl+Q` 그리기/편집 모드 전환으로 세부 영역을 확인합니다.

![image-20250715235507837](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235507837.png)





## 3. 효율적인 워크플로우를 위한 UI/UX

사용자가 작업에만 집중할 수 있도록 똑똑한 UI/UX를 제공합니다.

-   **넓은 작업 공간:** 좌우 패널의 크기를 자유롭게 조절하거나 완전히 접어서 이미지를 더 넓은 공간에서 보며 작업할 수 있습니다.
-   **이미지 미리보기 바:** 하단의 썸네일 바를 통해 전체 이미지 목록을 한눈에 파악하고 원하는 이미지로 빠르게 이동할 수 있습니다.
-   **실시간 동기화:** 캔버스에서 특정 박스를 선택하면 우측 라벨 목록에서 해당 라벨이 하이라이트되고, 반대로 목록에서 라벨을 선택하면 캔버스 위 박스가 선택됩니다.
-   **강력한 필터링:** 라벨이 없는 이미지, 특정 클래스가 포함된 이미지 등 원하는 조건으로 이미지를 필터링하여 체계적으로 작업할 수 있습니다.

![image-20250715235602498](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235602498.png)

![image-20250715235649892](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235649892.png)



## 4. 똑똑한 라벨 관리 기능

단순 반복 작업을 넘어, 데이터셋을 체계적으로 관리할 수 있는 고급 기능을 지원합니다.

-   **YAML 파일을 이용한 클래스 이름 로드:** `data.yaml`과 같은 클래스 정의 파일을 불러와 '0', '1'과 같은 숫자 ID 대신 'car', 'person'처럼 알아보기 쉬운 이름으로 라벨을 관리할 수 있습니다.
-   **일괄 작업:** 특정 클래스에 해당하는 모든 박스를 한 번에 선택하거나, 여러 박스를 선택하여 클래스를 동시에 변경하는 등 반복 작업을 최소화할 수 있습니다.

![image-20250715235526521](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235526521.png)

![image-20250715235802994](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235802994.png)





## 5. 생산성을 높이는 다양한 편의 기능

-   **다크 모드:** 장시간 작업에도 눈이 편안한 다크 모드를 지원합니다.
-   **자동 저장:** 혹시 모를 데이터 유실을 방지하기 위해 작업 내용이 자동으로 저장됩니다.
-   **다양한 단축키:** 이미지 이동(A/D), 복사/붙여넣기(Ctrl+C/V) 등 풍부한 단축키를 활용해 작업 속도를 극대화할 수 있습니다.

![image-20250715235825197](/images/2025-07-15-easy-labeling-in-depth-features/image-20250715235825197.png)

## 지금 바로 사용해보기

Easy Labeling은 개발자와 연구자들의 피드백을 통해 계속 개선하는 오픈소스 프로젝트입니다. 실제 사용은 실행 페이지에서 시작하고, 소스 코드와 변경 사항은 GitHub 저장소에서 확인할 수 있습니다.

**[Easy Labeling 실행 페이지 열기](https://mouseball54.github.io/easy_labeling/)**

**[Easy Labeling GitHub 저장소 보기](https://github.com/MouseBall54/easy_labeling)**

## 참고할 자료

- [Easy Labeling GitHub 저장소](https://github.com/MouseBall54/easy_labeling): 현재 기능 범위, Detection/Segmentation 워크플로우, 저장 형식, 브라우저 조건, Electron 빌드 참고 자료입니다.
- [MDN File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API): 브라우저 기반 로컬 폴더 접근 방식의 기본 자료입니다.
- [Ultralytics Object Detection Dataset Docs](https://docs.ultralytics.com/datasets/detect/): YOLO 데이터셋과 라벨 형식을 확인할 때 참고할 공식 문서입니다.
- [Label Studio Bounding Box Template](https://labelstud.io/templates/image_bbox): bounding box annotation 개념을 다른 라벨링 도구와 비교할 때 참고할 수 있습니다.

## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [Easy Labeling 개발기: 로컬 Detection과 Segmentation 주석 도구](/ko_easy_labeling/easy-labeling-development/)
- [Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)
