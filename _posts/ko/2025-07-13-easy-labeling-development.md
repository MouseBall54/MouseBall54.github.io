---
typora-root-url: ../
layout: single
header:
  teaser: /images/2025-07-13-easy-labeling-development/image-20250715203036663.png
  overlay_image: /images/2025-07-13-easy-labeling-development/image-20250715203036663.png
  overlay_filter: 0.36
  image_description: >
    이 글의 핵심 주제를 한눈에 설명하는 이미지입니다: Easy Labeling 개발기: 로컬 Detection과 Segmentation 주석 도구
title: "Easy Labeling 개발기: 로컬 Detection과 Segmentation 주석 도구"

date: 2025-07-13T00:00:00+09:00
last_modified_at: 2026-05-24T00:00:00+09:00
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

이 게시물에서는 제가 개발한 웹 기반 이미지 주석(Annotation) 및 라벨링(Labeling) 도구, **Easy Labeling**을 소개합니다. 현재 저장소 기준으로는 **Detection**에서 YOLO bounding box를 만들고, **Segmentation**에서 브러시 기반 마스크를 편집할 수 있습니다.

![image-20250715203036663](/images/2025-07-13-easy-labeling-development/image-20250715203036663.png)

## 프로젝트 소개: YOLO 데이터셋을 위한 최적의 솔루션

Easy Labeling은 컴퓨터 비전 데이터셋 주석 작업을 로컬에서 빠르게 처리하기 위해 만들었습니다. 브라우저 버전은 File System Access API로 로컬 폴더를 직접 읽고 쓰며, 저장소에는 Windows용 Electron 빌드 방법도 문서화되어 있습니다.

현재 도구는 두 가지 주요 워크플로우를 제공합니다. **Detection**은 YOLO bounding box를 만들고 `label/<image>.txt`로 저장합니다. **Segmentation**은 브러시와 지우개로 마스크를 편집하고 `mask/<image>.png`, `mask/<image>.seg.json`을 저장합니다. 클래스 이름은 `.yaml` 파일로 관리할 수 있습니다.

## 주요 기능

*   **Detection 워크플로우:** YOLO bounding box 라벨 파일을 생성하고 `.yaml` 클래스 파일을 불러와 작업합니다.
*   **로컬 파일 시스템 연동:** 이미지와 라벨 파일을 서버에 올리지 않고 로컬에서 바로 불러와 작업합니다.
*   **Detection과 Segmentation 도구:**
    *   Detection에서 bounding box 그리기, 편집, 이동, 크기 조정, 복사, 정렬, 분배, 삭제를 지원합니다.
    *   Segmentation에서 브러시와 지우개로 마스크를 편집하고, 연결 영역 이동과 클래스 변경을 지원합니다.
    *   확대/축소, pan, crosshair, 미리보기 이동으로 세부 작업을 돕습니다.
*   **효율적인 워크플로우 및 UI:**
    *   이미지 미리보기, 라벨 목록-캔버스 동기화, 클래스별 필터링
    *   작업 속도를 높이는 다양한 키보드 단축키
*   **고급 라벨 관리:**
    *   여러 개의 경계 상자 클래스를 한 번에 변경하는 등 대량 작업 지원
*   **유연한 설정:** JPG, PNG, TIFF 등 다양한 이미지 형식과 자동 저장, 다크 모드 지원

## 실제 작업 흐름에서 중요한 점

Easy Labeling을 사용할 때 핵심은 “박스를 빨리 그리는 것”에서 끝나지 않습니다. 객체 탐지 데이터셋은 **클래스 순서**, **이미지 파일명과 라벨 파일명**, **YOLO 좌표 정규화**, **검수 기준**이 함께 맞아야 학습 단계에서 안정적으로 동작합니다.

따라서 처음부터 전체 이미지를 모두 라벨링하기보다, 작은 샘플 폴더를 먼저 열어 클래스 기준을 시험하는 편이 좋습니다. 예를 들어 20~50장 정도를 골라 Easy Labeling에서 박스를 그린 뒤, 저장된 `.txt` 파일을 열어 class ID와 좌표 값이 기대한 구조인지 확인합니다. 이 과정을 거치면 클래스 이름은 맞지만 ID 순서가 어긋나는 문제, 너무 느슨한 bounding box, 애매한 객체를 라벨링할지 말지 정하지 않은 문제를 초기에 잡을 수 있습니다.


## 저장소 기준 기능 범위

현재 Easy Labeling은 YOLO 박스 전용 편집기만은 아닙니다. 저장소 README 기준 상단에는 `Detection`과 `Segmentation` 두 워크플로우 탭이 있습니다. Detection은 YOLO bounding box를 다루고 `label/<image>.txt`로 저장합니다. Segmentation은 브러시 기반 마스크를 다루며 `mask/<image>.png`와 `mask/<image>.seg.json`을 저장합니다.

브라우저 버전은 로컬 폴더 읽기/쓰기에 File System Access API가 필요하므로 Desktop Chrome 또는 Edge 사용을 전제로 보는 편이 안전합니다. 저장소에는 Windows용 Electron 빌드도 문서화되어 있습니다. 박스 목록 기반 다중 편집, 정렬, 분배, 복사/붙여넣기는 Detection 중심 기능으로 보고, Segmentation은 브러시, 지우개, 연결 영역 선택, 드래그 이동, 클래스 변경 중심으로 검수해야 합니다.

![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면](/images/easy_labeling_sample.png)

실무에서는 라벨링 지침서도 함께 필요합니다. “사람”, “차량”, “간판”처럼 쉬워 보이는 클래스도 가려진 경우, 잘린 경우, 반사된 경우, 매우 작은 경우에 기준이 달라질 수 있습니다. 이런 edge case를 이미지와 함께 남겨 두면 라벨러가 늘어나도 같은 판단을 반복하기 쉬워집니다.

작업이 끝난 뒤에는 `images/train`, `images/val`, `labels/train`, `labels/val` 구조와 `data.yaml`의 클래스 순서를 다시 확인해야 합니다. 모델 학습 오류처럼 보이는 문제 중 상당수는 실제로 라벨 파일 누락, 파일명 불일치, 클래스 순서 변경에서 시작됩니다.

## 전문 보완 체크

**Easy Labeling 개발기: 로컬 Detection과 Segmentation 주석 도구**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 컴퓨터 비전 데이터셋 품질 관리 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 클래스 사전, 어노테이션 일관성, train/validation/test 분리, 내보내기 형식를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 샘플 검수 메모, YOLO 또는 COCO 파일, 라벨러 불일치 기록, 학습 오류 사례가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

## 참고할 자료

- [Easy Labeling GitHub 저장소](https://github.com/MouseBall54/easy_labeling): 현재 기능 범위, Detection/Segmentation 워크플로우, 저장 형식, 브라우저 조건, Electron 빌드 참고 자료입니다.
- [MDN File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API): 브라우저에서 로컬 폴더와 파일을 다루는 방식의 기본 자료입니다.
- [Ultralytics Object Detection Dataset Docs](https://docs.ultralytics.com/datasets/detect/): YOLO 데이터셋 폴더 구조와 라벨 형식을 확인할 때 참고할 공식 문서입니다.
- [CVAT YOLO Format](https://docs.cvat.ai/docs/dataset_management/formats/format-yolo/): 다른 라벨링 도구와 YOLO 포맷을 비교할 때 참고할 수 있는 형식 문서입니다.

## 현재 저장소 기준 상태

GitHub 저장소 README는 Easy Labeling을 Detection과 Segmentation 두 워크플로우를 가진 로컬 주석 도구로 설명합니다. 브라우저 버전은 로컬 폴더 읽기/쓰기 지원 때문에 Desktop Chrome 또는 Edge 사용을 권장하고, Windows 앱이 필요한 경우 Electron 빌드 명령도 확인할 수 있습니다.

프로젝트에 관심이 있으시다면 [GitHub 저장소](https://github.com/MouseBall54/easy_labeling)를 확인하고, 대량 라벨링 전에 README의 기능 범위와 데이터셋 요구사항을 먼저 비교해 보세요.

---
## 함께 보면 좋은 글

같은 주제 흐름에서 이어서 읽기 좋은 글입니다.

- [YOLO 라벨링을 위한 Easy Labeling 주요 기능](/ko_easy_labeling/easy-labeling-in-depth-features/)
- [Easy Labeling 가이드 (1) - 이미지와 라벨 불러오기](/ko_easy_labeling/easy-labeling-guide-1/)
