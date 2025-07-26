---
typora-root-url: ../
header:
  teaser: ../images/2025-07-13-easy-labeling-development/image-20250715203036663.png
layout: single
title: "YOLO 데이터 라벨링, 설치 없이 웹에서 바로! Easy Labeling 개발기"
date: 2025-07-13T15:00:00+09:00
toc: true
toc_sticky: true
author_profile: false
sidebar:
  nav: "docs"
categories:
  - ko_easy_labeling
tags:
  - YOLO
  - Labeling
  - Annotation
  - Object Detection
  - Data Augmentation
  - Bounding Box
  - AI
  - Machine Learning
  - Dataset
excerpt: "YOLO 객체 탐지 모델 학습, 데이터 라벨링 때문에 힘드셨나요? 설치가 필요 없는 웹 기반 YOLO 라벨링 도구, Easy Labeling의 개발 과정과 주요 기능을 소개합니다. 로컬 파일을 직접 사용하여 빠르고 안전하게 인공지능 데이터셋을 구축하는 방법을 알아보세요."
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



## 향후 계획

앞으로 데이터 증강(Data Augmentation) 관련 기능과 다양한 주석 포맷 지원을 추가할 계획입니다. 개발 진행 상황과 기술적인 도전 과제들을 이 블로그를 통해 꾸준히 공유하겠습니다.

프로젝트에 관심이 있으시다면 [GitHub 저장소](https://github.com/MouseBall54/easy_labeling)를 방문해주세요. 많은 관심과 피드백 부탁드립니다!

---