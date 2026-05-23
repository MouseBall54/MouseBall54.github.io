---
typora-root-url: ../
layout: single
header:
  teaser: /images/2025-07-13-easy-labeling-development/image-20250715203036663.png
  overlay_image: /images/2025-07-13-easy-labeling-development/image-20250715203036663.png
  overlay_filter: 0.36
  image_description: >
    이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: YOLO 데이터 라벨링, 설치 없이 웹에서 바로! Easy Labeling 개발기
title: "YOLO 데이터 라벨링, 설치 없이 웹에서 바로! Easy Labeling 개발기"

date: 2025-07-13T00:00:00+09:00
lang: ko
translation_id: easy-labeling-development
categories:
  - ko_easy_labeling
tags:
  - YOLO
  - Labeling
  - Annotation
  - ObjectDetection
  - Dataset
excerpt: "YOLO 객체 탐지 모델 학습, 데이터 라벨링 때문에 힘드셨나요? 설치가 필요 없는 웹 기반 YOLO 라벨링 도구, Easy Labeling의 개발 과정과 주요 기능을 소개합니다. 로컬 파일을 직접 사용하여 빠르고 안전하게 인공지능 데이터셋을 구축하는 방법을 알아보세요."
seo_description: "YOLO 객체 탐지 모델 학습, 데이터 라벨링 때문에 힘드셨나요? 설치가 필요 없는 웹 기반 YOLO 라벨링 도구, Easy Labeling의 개발 과정과 주요 기능을 소개합니다. 로컬 파일을 직접 사용하여 빠르고 안전하게 인공지능 데이터셋을 구축하는 방법을 알아보세요."
---


<p><strong>Easy Labeling 프로젝트 페이지: <a href="https://mouseball54.github.io/easy_labeling/">https://mouseball54.github.io/easy_labeling/</a></strong></p>

안녕하세요! MouseBall54's Toolbox의 첫 번째 게시물입니다.

이 게시물에서는 제가 개발한 웹 기반 이미지 주석(Annotation) 및 라벨링(Labeling) 도구, **Easy Labeling**을 소개합니다. 특히 **YOLO 포맷** 데이터셋 생성을 목표로 하는 분들께 유용한 도구가 될 것입니다.

![image-20250715203036663](/images/2025-07-13-easy-labeling-development/image-20250715203036663.png)

## 프로젝트 소개: YOLO 데이터셋을 위한 최적의 솔루션

Easy Labeling은 객체 탐지(Object Detection) 모델, 특히 YOLO 계열 모델 학습에 필요한 데이터셋을 구축하는 과정을 간소화하기 위해 탄생했습니다. 가장 큰 특징은 **설치가 필요 없는 웹 기반**이라는 점과, 사용자의 **로컬 파일을 직접 처리**한다는 점입니다. File System Access API를 활용하여 이미지와 라벨 파일을 서버에 업로드하는 과정 없이 작업하므로, 민감한 데이터를 안전하게 다룰 수 있고 속도도 매우 빠릅니다.

주요 출력 포맷은 **YOLO 텍스트 포맷(.txt)**이며, `.yaml` 파일을 통해 클래스 이름을 관리하는 등 YOLO 사용자를 위한 편의 기능을 다수 포함하고 있습니다.

## 주요 기능

*   **YOLO 포맷 완벽 지원:** 라벨 파일을 YOLO 포맷으로 생성하고, `.yaml` 클래스 파일을 불러와 작업의 효율성을 높입니다.
*   **로컬 파일 시스템 연동:** 이미지와 라벨 파일을 서버에 올리지 않고 로컬에서 바로 불러와 작업합니다.
*   **다양한 주석(Annotation) 도구:**
    *   경계 상자(Bounding Box) 그리기, 편집, 이동, 크기 조정 및 삭제
    *   정밀 작업을 위한 '그리기'와 '편집' 모드 전환
    *   캔버스 확대/축소, 이동(Pan), 좌표 직접 입력
*   **효율적인 워크플로우 및 UI:**
    *   이미지 미리보기, 라벨 목록-캔버스 동기화, 클래스별 필터링
    *   작업 속도를 높이는 다양한 키보드 단축키
*   **고급 라벨 관리:**
    *   여러 개의 경계 상자 클래스를 한 번에 변경하는 등 대량 작업 지원
*   **유연한 설정:** JPG, PNG, TIFF 등 다양한 이미지 형식과 자동 저장, 다크 모드 지원

## 실제 작업 흐름에서 중요한 점

Easy Labeling을 사용할 때 핵심은 “박스를 빨리 그리는 것”에서 끝나지 않습니다. 객체 탐지 데이터셋은 **클래스 순서**, **이미지 파일명과 라벨 파일명**, **YOLO 좌표 정규화**, **검수 기준**이 함께 맞아야 학습 단계에서 안정적으로 동작합니다.

따라서 처음부터 전체 이미지를 모두 라벨링하기보다, 작은 샘플 폴더를 먼저 열어 클래스 기준을 시험하는 편이 좋습니다. 예를 들어 20~50장 정도를 골라 Easy Labeling에서 박스를 그린 뒤, 저장된 `.txt` 파일을 열어 class ID와 좌표 값이 기대한 구조인지 확인합니다. 이 과정을 거치면 클래스 이름은 맞지만 ID 순서가 어긋나는 문제, 너무 느슨한 bounding box, 애매한 객체를 라벨링할지 말지 정하지 않은 문제를 초기에 잡을 수 있습니다.

![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면](/images/easy_labeling_sample.png)

실무에서는 라벨링 지침서도 함께 필요합니다. “사람”, “차량”, “간판”처럼 쉬워 보이는 클래스도 가려진 경우, 잘린 경우, 반사된 경우, 매우 작은 경우에 기준이 달라질 수 있습니다. 이런 edge case를 이미지와 함께 남겨 두면 라벨러가 늘어나도 같은 판단을 반복하기 쉬워집니다.

작업이 끝난 뒤에는 `images/train`, `images/val`, `labels/train`, `labels/val` 구조와 `data.yaml`의 클래스 순서를 다시 확인해야 합니다. 모델 학습 오류처럼 보이는 문제 중 상당수는 실제로 라벨 파일 누락, 파일명 불일치, 클래스 순서 변경에서 시작됩니다.



## 향후 계획

앞으로 데이터 증강(Data Augmentation) 관련 기능과 다양한 주석 포맷 지원을 추가할 계획입니다. 개발 진행 상황과 기술적인 도전 과제들을 이 블로그를 통해 꾸준히 공유하겠습니다.

프로젝트에 관심이 있으시다면 [GitHub 저장소](https://github.com/MouseBall54/easy_labeling)를 방문해주세요. 많은 관심과 피드백 부탁드립니다!

---
## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [YOLO 라벨링 끝판왕, Easy Labeling 주요 기능 파헤치기](/ko_easy_labeling/easy-labeling-in-depth-features/)
- [Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)
