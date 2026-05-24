#!/usr/bin/env python3
"""Generate paired Easy Labeling and computer vision campaign posts."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-23"
LAST_MODIFIED_AT = "2026-05-23T23:59:00+09:00"
KO_CATEGORY = "ko_easy_labeling"
EN_CATEGORY = "en_easy_labeling"
TOOL_URL = "https://mouseball54.github.io/easy_labeling/"
SAMPLE_IMAGE = "/images/easy_labeling_sample.png"


SOURCES = {
    "ultralytics_detect": {
        "ko": "Ultralytics Object Detection Dataset Docs",
        "en": "Ultralytics Object Detection Dataset Docs",
        "url": "https://docs.ultralytics.com/datasets/detect/",
    },
    "ultralytics_coco": {
        "ko": "Ultralytics COCO to YOLO Conversion Guide",
        "en": "Ultralytics COCO to YOLO Conversion Guide",
        "url": "https://docs.ultralytics.com/guides/coco-to-yolo/",
    },
    "ultralytics_augment": {
        "ko": "Ultralytics YOLO Data Augmentation Guide",
        "en": "Ultralytics YOLO Data Augmentation Guide",
        "url": "https://docs.ultralytics.com/guides/yolo-data-augmentation/",
    },
    "ultralytics_utils": {
        "ko": "Ultralytics Simple Utilities",
        "en": "Ultralytics Simple Utilities",
        "url": "https://docs.ultralytics.com/usage/simple-utilities/",
    },
    "cvat_formats": {
        "ko": "CVAT Dataset Formats",
        "en": "CVAT Dataset Formats",
        "url": "https://docs.cvat.ai/docs/dataset_management/formats/",
    },
    "cvat_yolo": {
        "ko": "CVAT YOLO Format",
        "en": "CVAT YOLO Format",
        "url": "https://docs.cvat.ai/docs/dataset_management/formats/format-yolo/",
    },
    "labelstudio_bbox": {
        "ko": "Label Studio Bounding Box Template",
        "en": "Label Studio Bounding Box Template",
        "url": "https://labelstud.io/templates/image_bbox",
    },
    "fiftyone_annotation": {
        "ko": "FiftyOne Annotation Guide",
        "en": "FiftyOne Annotation Guide",
        "url": "https://docs.voxel51.com/getting_started/annotation/index.html",
    },
    "fiftyone_api": {
        "ko": "FiftyOne Annotation API",
        "en": "FiftyOne Annotation API",
        "url": "https://docs.voxel51.com/integrations/annotation.html",
    },
    "mdn_filesystem": {
        "ko": "MDN File System API",
        "en": "MDN File System API",
        "url": "https://developer.mozilla.org/en-US/docs/Web/API/File_System_API",
    },
}


TOPICS = [
    {
        "slug": "yolo-label-format",
        "ko_title": "YOLO Label Format 읽는 법: class, center x, center y, width, height 이해하기",
        "en_title": "YOLO Label Format: Read Class, Center X, Center Y, Width, and Height",
        "ko_summary": "YOLO 라벨은 한 객체를 class ID와 정규화된 중심 좌표, 너비, 높이로 표현하므로 이미지 크기와 좌표 기준을 함께 이해해야 한다.",
        "en_summary": "A YOLO label represents one object with a class ID and normalized center coordinates, width, and height, so image size and coordinate rules must be checked together.",
        "ko_focus": "라벨 파일을 열었을 때 숫자가 맞아 보이더라도 클래스 순서, 정규화 범위, 이미지-라벨 파일명이 어긋나면 학습 데이터는 깨집니다.",
        "en_focus": "The numbers may look valid, but the dataset breaks when class order, normalization range, or image-label filenames drift.",
        "ko_actions": ["이미지 파일명과 같은 이름의 `.txt` 라벨이 있는지 확인합니다.", "각 줄이 `class x_center y_center width height` 순서인지 봅니다.", "좌표가 0과 1 사이의 정규화 값인지 샘플로 검산합니다."],
        "en_actions": ["Confirm that each image has a matching `.txt` label file.", "Check that each row follows `class x_center y_center width height`.", "Spot-check that coordinates are normalized between 0 and 1."],
        "signals": ["class index", "normalized center", "box size", "matching filename"],
        "ko_signals": ["클래스 ID", "정규화 중심점", "박스 크기", "파일명 매칭"],
        "sources": ["ultralytics_detect", "cvat_yolo", "labelstudio_bbox"],
        "tags": ["YOLO", "LabelFormat", "ObjectDetection", "Dataset"],
    },
    {
        "slug": "coco-to-yolo-conversion",
        "ko_title": "COCO to YOLO 변환 실수: 객체 탐지 라벨이 깨지는 이유",
        "en_title": "COCO to YOLO Conversion Mistakes: Avoid Broken Detection Labels",
        "ko_summary": "COCO JSON을 YOLO 텍스트 라벨로 바꿀 때는 좌표 원점, 폭과 높이, category ID, 이미지 파일명을 모두 다시 맞춰야 한다.",
        "en_summary": "Converting COCO JSON to YOLO text labels requires checking coordinate origin, width and height, category IDs, and image filenames.",
        "ko_focus": "변환 스크립트가 성공했다는 메시지는 충분한 검증이 아닙니다. 변환 뒤에는 반드시 이미지를 열어 박스 위치와 클래스명을 확인해야 합니다.",
        "en_focus": "A successful conversion message is not enough. After conversion, open samples and verify box positions and class names visually.",
        "ko_actions": ["COCO `bbox`가 왼쪽 위 기준인지 확인합니다.", "YOLO 중심 좌표로 바뀐 값을 샘플 이미지에서 역산합니다.", "변환 후 클래스 ID가 `data.yaml` 순서와 같은지 비교합니다."],
        "en_actions": ["Confirm that COCO `bbox` starts from the top-left corner.", "Reverse-check converted YOLO center coordinates on sample images.", "Compare converted class IDs with the `data.yaml` order."],
        "signals": ["bbox origin", "category mapping", "converted txt", "visual overlay"],
        "ko_signals": ["bbox 원점", "카테고리 매핑", "변환된 txt", "시각 검수"],
        "sources": ["ultralytics_coco", "ultralytics_utils", "cvat_formats"],
        "tags": ["COCO", "YOLO", "Conversion", "Annotation"],
    },
    {
        "slug": "image-labeling-classes",
        "ko_title": "이미지 라벨링 클래스 관리법: class name, ID, dataset consistency 지키기",
        "en_title": "Image Labeling Classes: Manage Names, IDs, and Dataset Consistency",
        "ko_summary": "클래스 관리는 모델 학습 전 가장 먼저 고정해야 하는 규칙이며, 이름보다 ID 순서와 예외 기준이 더 중요하다.",
        "en_summary": "Class management is the first rule to freeze before training; ID order and edge-case rules matter more than names alone.",
        "ko_focus": "라벨러가 같은 물체를 다른 이름으로 부르거나 같은 이름을 다른 기준으로 쓰면 모델은 일관된 신호를 배울 수 없습니다.",
        "en_focus": "If labelers use different names for the same object or one name for different standards, the model cannot learn a consistent signal.",
        "ko_actions": ["클래스 이름, ID, 포함 기준, 제외 기준을 한 표에 적습니다.", "비슷한 클래스는 예시 이미지로 차이를 고정합니다.", "작업 중 클래스 순서를 바꾸지 않도록 `data.yaml`을 잠급니다."],
        "en_actions": ["Write class name, ID, include rule, and exclude rule in one table.", "Use example images to separate similar classes.", "Freeze `data.yaml` so class order does not change during labeling."],
        "signals": ["class dictionary", "include rule", "exclude rule", "id order"],
        "ko_signals": ["클래스 사전", "포함 기준", "제외 기준", "ID 순서"],
        "sources": ["ultralytics_detect", "labelstudio_bbox", "fiftyone_annotation"],
        "tags": ["Classes", "Dataset", "YOLO", "QualityControl"],
    },
    {
        "slug": "local-image-labeling-workflow",
        "ko_title": "로컬 이미지 라벨링 워크플로우: 이미지, 클래스, 라벨, 검수 정리법",
        "en_title": "Local Image Labeling Workflow: Organize Images, Classes, Labels, and Review",
        "ko_summary": "로컬 라벨링은 파일 업로드를 줄이고 민감한 이미지를 통제할 수 있지만 폴더 구조, 저장 규칙, 백업 기준을 먼저 정해야 한다.",
        "en_summary": "Local labeling reduces uploads and keeps sensitive images under control, but folder structure, save rules, and backups must be defined first.",
        "ko_focus": "로컬 우선 작업은 빠르지만 파일을 사람이 직접 다루기 때문에 이름, 위치, 백업이 흐트러지면 복구 비용이 커집니다.",
        "en_focus": "Local-first work is fast, but because people handle files directly, naming, location, and backup drift can become expensive.",
        "ko_actions": ["원본 이미지는 읽기 전용 폴더에 둡니다.", "작업 폴더와 검수 완료 폴더를 분리합니다.", "하루 작업이 끝날 때 라벨 파일과 클래스 파일을 함께 백업합니다."],
        "en_actions": ["Keep original images in a read-only folder.", "Separate working and reviewed folders.", "Back up label files and class files together at the end of each day."],
        "signals": ["source folder", "working folder", "reviewed folder", "backup copy"],
        "ko_signals": ["원본 폴더", "작업 폴더", "검수 폴더", "백업본"],
        "sources": ["mdn_filesystem", "cvat_formats", "ultralytics_detect"],
        "tags": ["LocalFirst", "Workflow", "Labeling", "Privacy"],
    },
    {
        "slug": "easy-labeling-yolo-dataset",
        "ko_title": "Easy Labeling으로 YOLO 데이터셋 만들기: 이미지에서 학습 폴더까지",
        "en_title": "Build a YOLO Dataset with Easy Labeling: From Images to Training Folders",
        "ko_summary": "Easy Labeling은 브라우저에서 로컬 이미지를 열고 YOLO 박스를 저장할 수 있으므로 작은 샘플 검수부터 학습 폴더 구성까지 연결하기 좋다.",
        "en_summary": "Easy Labeling can open local images in the browser and save YOLO boxes, making it useful from small-sample review to training folder setup.",
        "ko_focus": "도구를 여는 것보다 중요한 것은 라벨링 전 클래스 규칙과 라벨링 후 폴더 검증을 같은 루틴에 넣는 것입니다.",
        "en_focus": "Opening the tool is not the main task; class rules before labeling and folder validation after labeling must be part of one routine.",
        "ko_actions": ["클래스 목록을 먼저 만들고 샘플 20장으로 기준을 시험합니다.", "Easy Labeling에서 박스를 저장한 뒤 라벨 파일을 확인합니다.", "`images/train`, `images/val`, `labels/train`, `labels/val` 구조로 정리합니다."],
        "en_actions": ["Create the class list first and test it on 20 sample images.", "Save boxes in Easy Labeling and inspect the label files.", "Organize `images/train`, `images/val`, `labels/train`, and `labels/val`."],
        "signals": ["class yaml", "saved label", "train split", "validation split"],
        "ko_signals": ["클래스 yaml", "저장 라벨", "train 분할", "validation 분할"],
        "sources": ["ultralytics_detect", "mdn_filesystem", "cvat_yolo"],
        "tags": ["EasyLabeling", "YOLO", "Dataset", "Training"],
    },
    {
        "slug": "bounding-box-quality-checklist",
        "ko_title": "Bounding Box 품질 체크리스트: 느슨한 박스와 잘린 객체를 줄이는 법",
        "en_title": "Bounding Box Quality Checklist: Reduce Loose Boxes and Cut Objects",
        "ko_summary": "박스 품질은 모델 성능의 상한을 정하므로 객체 경계, 가림, 잘림, 여백, 클래스 기준을 검수표로 반복 확인해야 한다.",
        "en_summary": "Box quality sets a ceiling for model performance, so object borders, occlusion, truncation, padding, and class rules need repeatable review.",
        "ko_focus": "좋은 박스는 예쁜 박스가 아니라 학습 목표와 같은 기준으로 반복해서 그릴 수 있는 박스입니다.",
        "en_focus": "A good box is not a pretty box; it is a box that can be redrawn consistently under the training objective.",
        "ko_actions": ["객체 외곽에 불필요한 배경이 많이 들어갔는지 봅니다.", "잘린 객체도 라벨링할지 프로젝트 기준을 정합니다.", "라벨러별 샘플을 같은 이미지 위에서 비교합니다."],
        "en_actions": ["Check whether too much background is included around the object.", "Define whether truncated objects should be labeled.", "Compare labeler samples on the same image."],
        "signals": ["tight border", "occlusion rule", "truncation rule", "review sample"],
        "ko_signals": ["타이트한 경계", "가림 기준", "잘림 기준", "검수 샘플"],
        "sources": ["labelstudio_bbox", "fiftyone_annotation", "ultralytics_detect"],
        "tags": ["BoundingBox", "QualityControl", "Annotation", "Review"],
    },
    {
        "slug": "labeling-instructions-template",
        "ko_title": "라벨링 지침서 템플릿: 라벨러가 같은 기준으로 박스를 그리게 만드는 법",
        "en_title": "Labeling Instructions Template: Make Labelers Draw Boxes the Same Way",
        "ko_summary": "라벨링 지침서는 클래스 설명, 포함·제외 기준, 예외 이미지, 저장 규칙, 질문 처리 방법을 한 문서로 고정해야 한다.",
        "en_summary": "A labeling instruction document should freeze class definitions, include and exclude rules, edge images, save rules, and question handling.",
        "ko_focus": "구두 설명으로 시작한 프로젝트는 라벨러가 늘어날수록 기준이 갈라집니다. 지침서는 작업 속도를 늦추는 문서가 아니라 재작업을 줄이는 장치입니다.",
        "en_focus": "Projects that start with verbal instructions drift as labelers grow. Instructions are not paperwork; they reduce relabeling.",
        "ko_actions": ["각 클래스마다 좋은 예시와 제외 예시를 넣습니다.", "애매한 이미지는 질문 로그에 모아 주 1회 기준을 업데이트합니다.", "지침서 버전과 데이터셋 버전을 함께 기록합니다."],
        "en_actions": ["Add positive and negative examples for each class.", "Collect ambiguous images in a question log and update rules weekly.", "Record instruction version together with dataset version."],
        "signals": ["positive example", "negative example", "question log", "instruction version"],
        "ko_signals": ["좋은 예시", "제외 예시", "질문 로그", "지침서 버전"],
        "sources": ["labelstudio_bbox", "cvat_formats", "fiftyone_api"],
        "tags": ["Instructions", "Labeling", "TeamWorkflow", "Dataset"],
    },
    {
        "slug": "dataset-split-train-val-test",
        "ko_title": "Train, Val, Test 데이터셋 분할: 이미지 라벨링 후 누수를 막는 기준",
        "en_title": "Train, Val, Test Dataset Split: Prevent Leakage After Image Labeling",
        "ko_summary": "데이터셋 분할은 단순 비율 문제가 아니라 중복 이미지, 같은 촬영 환경, 같은 객체가 서로 다른 분할로 새지 않게 막는 품질 작업이다.",
        "en_summary": "Dataset splitting is not only a ratio; it prevents duplicate images, shared capture conditions, and the same object from leaking across splits.",
        "ko_focus": "분할이 잘못되면 검증 점수는 좋아 보이지만 실제 현장 이미지에서는 모델이 무너질 수 있습니다.",
        "en_focus": "A bad split can make validation metrics look strong while the model fails on real deployment images.",
        "ko_actions": ["같은 촬영 세션 이미지를 한 분할에 묶습니다.", "중복과 거의 같은 이미지를 먼저 제거합니다.", "분할별 클래스 개수와 작은 객체 비율을 비교합니다."],
        "en_actions": ["Keep images from the same capture session in one split.", "Remove duplicates and near-duplicates before splitting.", "Compare class counts and small-object ratios across splits."],
        "signals": ["split ratio", "capture group", "duplicate check", "class balance"],
        "ko_signals": ["분할 비율", "촬영 그룹", "중복 확인", "클래스 균형"],
        "sources": ["ultralytics_detect", "ultralytics_utils", "fiftyone_annotation"],
        "tags": ["DatasetSplit", "Validation", "YOLO", "DataLeakage"],
    },
    {
        "slug": "data-yaml-for-yolo",
        "ko_title": "YOLO data.yaml 작성법: 경로, 클래스 순서, 검증 오류 줄이기",
        "en_title": "YOLO data.yaml Guide: Paths, Class Order, and Validation Errors",
        "ko_summary": "`data.yaml`은 YOLO 학습에서 이미지 경로와 클래스 이름을 연결하는 계약서이므로 경로, 이름, 순서가 라벨 파일과 맞아야 한다.",
        "en_summary": "`data.yaml` is the contract connecting image paths and class names in YOLO training, so paths, names, and order must match label files.",
        "ko_focus": "`names` 목록 하나가 바뀌어도 같은 라벨 파일이 완전히 다른 클래스로 해석될 수 있습니다.",
        "en_focus": "Changing one `names` list can make the same label files mean completely different classes.",
        "ko_actions": ["`train`, `val`, `test` 경로가 실제 폴더와 맞는지 확인합니다.", "`names` 순서가 라벨 class ID와 같은지 잠급니다.", "경로를 상대경로로 둘지 절대경로로 둘지 팀 기준을 정합니다."],
        "en_actions": ["Check that `train`, `val`, and `test` paths match real folders.", "Freeze `names` order so it matches label class IDs.", "Decide whether the team uses relative or absolute paths."],
        "signals": ["train path", "val path", "names order", "yaml version"],
        "ko_signals": ["train 경로", "val 경로", "names 순서", "yaml 버전"],
        "sources": ["ultralytics_detect", "cvat_yolo", "ultralytics_utils"],
        "tags": ["YOLO", "DataYaml", "Training", "Dataset"],
    },
    {
        "slug": "annotation-review-sampling",
        "ko_title": "라벨 검수 샘플링: 모든 이미지를 다시 보지 않고 품질을 잡는 법",
        "en_title": "Annotation Review Sampling: Catch Quality Issues Without Rechecking Everything",
        "ko_summary": "라벨 검수는 전수 확인만 답이 아니며 클래스, 라벨러, 촬영 조건, 모델 오류 유형별로 샘플을 뽑아 반복 문제를 찾을 수 있다.",
        "en_summary": "Annotation review does not require checking every image; sampling by class, labeler, capture condition, and model error can reveal repeat issues.",
        "ko_focus": "검수는 랜덤 몇 장을 보는 행위가 아니라 어떤 위험을 확인할지 정한 뒤 샘플을 뽑는 과정입니다.",
        "en_focus": "Review is not just opening a few random images; it starts by naming the risk and then sampling for it.",
        "ko_actions": ["클래스별 최소 검수 수량을 정합니다.", "새 라벨러 작업은 첫날 더 높은 비율로 봅니다.", "모델이 자주 틀린 이미지 묶음을 별도 검수합니다."],
        "en_actions": ["Set a minimum review count per class.", "Review a higher share of a new labeler's first-day work.", "Create a separate review batch for images the model often misses."],
        "signals": ["review rate", "class sample", "labeler sample", "error batch"],
        "ko_signals": ["검수 비율", "클래스 샘플", "라벨러 샘플", "오류 묶음"],
        "sources": ["fiftyone_annotation", "fiftyone_api", "labelstudio_bbox"],
        "tags": ["Review", "Sampling", "QualityControl", "Annotation"],
    },
    {
        "slug": "small-object-labeling",
        "ko_title": "작은 객체 라벨링 기준: 보이는 물체와 학습 가능한 물체를 구분하기",
        "en_title": "Small Object Labeling Rules: Separate Visible Objects from Learnable Objects",
        "ko_summary": "작은 객체는 박스 오차가 모델 학습에 크게 작용하므로 최소 픽셀 크기, 확대 기준, 제외 기준을 먼저 정해야 한다.",
        "en_summary": "Small objects are sensitive to box error, so minimum pixel size, zoom rules, and exclusion rules should be decided before labeling.",
        "ko_focus": "사람 눈에 보인다고 항상 모델이 학습할 수 있는 라벨은 아닙니다. 목표 해상도에서 의미 있는 크기인지 봐야 합니다.",
        "en_focus": "An object being visible to humans does not mean it is useful for training. Check whether it matters at the target resolution.",
        "ko_actions": ["최소 박스 너비와 높이를 픽셀 단위로 정합니다.", "작은 객체는 확대 상태에서 한 번 더 검수합니다.", "너무 흐리거나 작은 객체는 제외 라벨 기준에 넣습니다."],
        "en_actions": ["Set minimum box width and height in pixels.", "Review small objects once more while zoomed in.", "Put very blurry or tiny objects into the exclusion rule."],
        "signals": ["minimum pixels", "zoom review", "blur rule", "target resolution"],
        "ko_signals": ["최소 픽셀", "확대 검수", "흐림 기준", "목표 해상도"],
        "sources": ["ultralytics_detect", "labelstudio_bbox", "fiftyone_annotation"],
        "tags": ["SmallObjects", "BoundingBox", "YOLO", "QualityControl"],
    },
    {
        "slug": "occlusion-truncation-labeling",
        "ko_title": "가림과 잘림 객체 라벨링: occlusion, truncation 기준을 문서화하기",
        "en_title": "Occlusion and Truncation Labeling: Document Edge-Case Rules",
        "ko_summary": "가려진 객체와 화면 밖으로 잘린 객체는 프로젝트마다 다르게 처리되므로 라벨링 전에 포함 기준과 박스 범위를 문서화해야 한다.",
        "en_summary": "Occluded and truncated objects are handled differently by project, so include rules and box extent must be documented before labeling.",
        "ko_focus": "애매한 객체를 그때그때 판단하면 검수자는 틀린 라벨과 다른 기준의 라벨을 구분할 수 없습니다.",
        "en_focus": "If ambiguous objects are decided case by case, reviewers cannot separate wrong labels from different label standards.",
        "ko_actions": ["가림 비율이 어느 정도면 라벨링할지 정합니다.", "보이는 부분만 그릴지 전체 추정 박스를 그릴지 정합니다.", "대표 예외 이미지를 지침서에 붙입니다."],
        "en_actions": ["Define how much occlusion still counts as labelable.", "Decide whether to draw only the visible part or the estimated full object.", "Attach representative edge images to the instruction document."],
        "signals": ["occlusion percent", "visible box", "estimated box", "edge example"],
        "ko_signals": ["가림 비율", "보이는 박스", "추정 박스", "예외 예시"],
        "sources": ["labelstudio_bbox", "cvat_formats", "fiftyone_annotation"],
        "tags": ["Occlusion", "Truncation", "Annotation", "Dataset"],
    },
    {
        "slug": "negative-images-for-detection",
        "ko_title": "객체가 없는 이미지도 필요한 이유: YOLO negative sample 설계",
        "en_title": "Why Object Detection Needs Negative Images: Design YOLO Negative Samples",
        "ko_summary": "객체가 없는 이미지는 모델이 배경을 객체로 착각하는 문제를 줄이는 데 도움이 되며, 실제 배포 환경의 배경을 반영해야 한다.",
        "en_summary": "Negative images help reduce false positives by teaching the model real deployment backgrounds where target objects are absent.",
        "ko_focus": "없는 이미지를 아무 배경이나 넣는 것이 아니라 모델이 실제로 헷갈릴 장면을 넣어야 합니다.",
        "en_focus": "Negative images should not be arbitrary backgrounds; they should represent scenes the model is likely to confuse.",
        "ko_actions": ["객체가 없는 이미지는 빈 라벨 파일 또는 프로젝트 규칙에 맞게 관리합니다.", "배포 환경과 비슷한 배경을 우선 모읍니다.", "검증 세트에도 negative 이미지를 포함해 오탐을 확인합니다."],
        "en_actions": ["Manage object-free images with empty label files or the project's chosen rule.", "Prioritize backgrounds similar to deployment scenes.", "Include negative images in validation to check false positives."],
        "signals": ["empty label", "background scene", "false positive", "deployment match"],
        "ko_signals": ["빈 라벨", "배경 장면", "오탐", "배포 환경 일치"],
        "sources": ["ultralytics_detect", "fiftyone_annotation", "cvat_yolo"],
        "tags": ["NegativeSamples", "ObjectDetection", "YOLO", "FalsePositives"],
    },
    {
        "slug": "duplicate-image-cleanup",
        "ko_title": "중복 이미지 정리: 라벨링 전에 near-duplicate를 줄여야 하는 이유",
        "en_title": "Duplicate Image Cleanup: Why Near-Duplicates Should Be Reduced Before Labeling",
        "ko_summary": "중복 이미지는 라벨링 비용을 늘리고 검증 점수를 부풀릴 수 있으므로 작업 전 파일명, 해시, 시각적 유사도를 기준으로 정리해야 한다.",
        "en_summary": "Duplicate images increase labeling cost and can inflate validation scores, so filenames, hashes, and visual similarity should be checked before labeling.",
        "ko_focus": "거의 같은 이미지를 많이 라벨링하면 데이터가 많아진 것처럼 보이지만 모델이 새로운 상황을 배운 것은 아닐 수 있습니다.",
        "en_focus": "Labeling many near-identical images can make the dataset look larger without adding much new signal.",
        "ko_actions": ["완전 중복 파일은 해시로 먼저 제거합니다.", "연속 프레임은 간격을 두고 샘플링합니다.", "train과 val에 같은 장면이 나뉘어 들어가지 않게 묶습니다."],
        "en_actions": ["Remove exact duplicates with hashes first.", "Sample video frames with spacing.", "Group the same scene so it does not split across train and val."],
        "signals": ["file hash", "near duplicate", "scene group", "split leakage"],
        "ko_signals": ["파일 해시", "근접 중복", "장면 그룹", "분할 누수"],
        "sources": ["fiftyone_annotation", "ultralytics_utils", "ultralytics_detect"],
        "tags": ["Duplicates", "DatasetCleaning", "Validation", "ComputerVision"],
    },
    {
        "slug": "class-imbalance-dataset",
        "ko_title": "클래스 불균형 데이터셋: 많이 찍힌 클래스만 잘 맞는 문제 줄이기",
        "en_title": "Class Imbalance in Datasets: Reduce Models That Only Learn Frequent Classes",
        "ko_summary": "클래스 불균형은 흔한 객체만 잘 맞는 모델을 만들 수 있으므로 라벨링 단계에서 빈도, 난이도, 검증 표본을 함께 관리해야 한다.",
        "en_summary": "Class imbalance can produce models that work only for frequent objects, so frequency, difficulty, and validation samples must be tracked during labeling.",
        "ko_focus": "클래스 수를 맞추는 것만으로는 부족합니다. 어려운 각도와 작은 객체가 어느 클래스에 몰려 있는지도 봐야 합니다.",
        "en_focus": "Balancing raw class counts is not enough; difficult angles and small objects may still cluster in a few classes.",
        "ko_actions": ["클래스별 이미지 수와 객체 수를 따로 봅니다.", "희귀 클래스는 검증 세트에 최소 표본을 보장합니다.", "쉬운 이미지 추가보다 어려운 케이스를 먼저 모읍니다."],
        "en_actions": ["Track image counts and object counts per class separately.", "Guarantee minimum validation samples for rare classes.", "Collect hard cases before adding more easy images."],
        "signals": ["class count", "object count", "rare class", "hard example"],
        "ko_signals": ["클래스 수", "객체 수", "희귀 클래스", "어려운 예시"],
        "sources": ["fiftyone_annotation", "ultralytics_detect", "labelstudio_bbox"],
        "tags": ["ClassImbalance", "Dataset", "YOLO", "ModelQuality"],
    },
    {
        "slug": "active-learning-labeling-loop",
        "ko_title": "Active Learning 라벨링 루프: 모델이 어려워한 이미지부터 다시 라벨링하기",
        "en_title": "Active Learning Labeling Loop: Relabel the Images Your Model Finds Hard",
        "ko_summary": "Active learning은 모든 이미지를 같은 순서로 라벨링하지 않고 모델의 낮은 확신, 오탐, 미탐 샘플을 우선 검수하는 반복 루프다.",
        "en_summary": "Active learning avoids labeling every image in order; it prioritizes low-confidence, false-positive, and false-negative samples for review.",
        "ko_focus": "라벨링을 한 번에 끝내려 하지 말고 작은 모델 학습 결과를 다음 라벨링 우선순위로 돌려야 합니다.",
        "en_focus": "Do not treat labeling as a one-pass task; use small model results to choose the next labeling batch.",
        "ko_actions": ["초기 데이터로 작게 학습합니다.", "낮은 확신과 반복 오류 이미지를 모읍니다.", "Easy Labeling에서 해당 묶음을 열어 기준을 수정하고 재라벨링합니다."],
        "en_actions": ["Train a small baseline with initial data.", "Collect low-confidence and repeat-error images.", "Open that batch in Easy Labeling, adjust rules, and relabel."],
        "signals": ["low confidence", "false positive", "false negative", "next batch"],
        "ko_signals": ["낮은 확신", "오탐", "미탐", "다음 배치"],
        "sources": ["fiftyone_annotation", "fiftyone_api", "ultralytics_detect"],
        "tags": ["ActiveLearning", "ModelReview", "Labeling", "YOLO"],
    },
    {
        "slug": "prelabeling-human-review",
        "ko_title": "Pre-labeling과 사람 검수: 자동 라벨을 그대로 믿지 않는 워크플로우",
        "en_title": "Pre-Labeling and Human Review: Do Not Trust Auto Labels Without QA",
        "ko_summary": "모델이 미리 그린 박스는 속도를 높일 수 있지만 클래스 혼동, 작은 객체 누락, 과신 오류를 사람이 검수해야 학습 데이터로 쓸 수 있다.",
        "en_summary": "Model-generated boxes can speed up work, but class confusion, missed small objects, and overconfident mistakes need human QA before training use.",
        "ko_focus": "자동 라벨은 정답이 아니라 초안입니다. 사람 검수가 빠진 자동화는 오류를 빠르게 복사하는 방식이 될 수 있습니다.",
        "en_focus": "Auto labels are drafts, not truth. Automation without review can copy mistakes faster.",
        "ko_actions": ["자동 라벨을 별도 버전으로 저장합니다.", "확신도 낮은 박스와 너무 큰 박스를 우선 봅니다.", "수정된 라벨만 학습 데이터로 승격합니다."],
        "en_actions": ["Save auto labels as a separate version.", "Review low-confidence boxes and overly large boxes first.", "Promote only corrected labels into the training dataset."],
        "signals": ["auto label", "human edit", "confidence score", "approved label"],
        "ko_signals": ["자동 라벨", "사람 수정", "확신도", "승인 라벨"],
        "sources": ["ultralytics_utils", "fiftyone_annotation", "labelstudio_bbox"],
        "tags": ["PreLabeling", "HumanReview", "Automation", "QualityControl"],
    },
    {
        "slug": "video-frame-extraction-labeling",
        "ko_title": "비디오 프레임 라벨링: 너무 많은 비슷한 장면을 줄이는 추출 기준",
        "en_title": "Video Frame Labeling: Extract Frames Without Flooding the Dataset",
        "ko_summary": "비디오에서 프레임을 추출할 때는 시간 간격, 장면 변화, 객체 다양성, 중복 제거 기준을 정해야 라벨링 비용을 줄일 수 있다.",
        "en_summary": "When extracting frames from video, time interval, scene change, object diversity, and duplicate cleanup rules reduce labeling cost.",
        "ko_focus": "초당 모든 프레임을 라벨링하면 비용은 커지지만 새 정보는 거의 늘지 않을 수 있습니다.",
        "en_focus": "Labeling every frame can explode cost while adding little new information.",
        "ko_actions": ["기본 추출 간격을 먼저 정합니다.", "장면 전환이나 객체 등장 이벤트에서 추가 샘플을 뽑습니다.", "연속 프레임은 한 분할에 묶어 누수를 막습니다."],
        "en_actions": ["Choose a default extraction interval first.", "Add samples around scene changes or object appearance events.", "Keep neighboring frames in one split to prevent leakage."],
        "signals": ["frame interval", "scene change", "event sample", "sequence group"],
        "ko_signals": ["프레임 간격", "장면 전환", "이벤트 샘플", "시퀀스 그룹"],
        "sources": ["cvat_formats", "fiftyone_annotation", "ultralytics_detect"],
        "tags": ["VideoFrames", "Labeling", "DatasetSplit", "ObjectDetection"],
    },
    {
        "slug": "segmentation-vs-detection-labels",
        "ko_title": "Segmentation과 Detection 라벨 선택: 박스가 충분한지 마스크가 필요한지 판단하기",
        "en_title": "Segmentation vs Detection Labels: Decide Whether Boxes Are Enough",
        "ko_summary": "객체 탐지 박스와 세그멘테이션 마스크는 비용과 활용 목적이 다르므로 라벨링 전에 모델 목표와 필요한 정밀도를 분리해야 한다.",
        "en_summary": "Detection boxes and segmentation masks have different costs and use cases, so model objective and required precision should be separated before labeling.",
        "ko_focus": "박스로 충분한 문제에 마스크를 쓰면 비용이 커지고, 마스크가 필요한 문제에 박스만 쓰면 결과가 부족할 수 있습니다.",
        "en_focus": "Using masks when boxes are enough increases cost; using only boxes when masks are needed can underfit the task.",
        "ko_actions": ["목표가 위치 탐지인지 경계 추정인지 나눕니다.", "박스 라벨로 먼저 baseline을 만들어 봅니다.", "경계 오류가 비즈니스 문제라면 마스크 라벨을 검토합니다."],
        "en_actions": ["Separate location detection from boundary estimation.", "Build a baseline with box labels first.", "Consider masks when boundary error is the real business problem."],
        "signals": ["box label", "mask label", "boundary error", "annotation cost"],
        "ko_signals": ["박스 라벨", "마스크 라벨", "경계 오류", "라벨링 비용"],
        "sources": ["cvat_formats", "fiftyone_annotation", "ultralytics_detect"],
        "tags": ["Segmentation", "Detection", "Annotation", "ModelDesign"],
    },
    {
        "slug": "rotated-bounding-box-decision",
        "ko_title": "Rotated Bounding Box가 필요한 경우: 기울어진 객체를 일반 박스로 충분히 표현할 수 있을까",
        "en_title": "When Rotated Bounding Boxes Matter: Are Regular Boxes Enough?",
        "ko_summary": "기울어진 물체가 많은 데이터셋에서는 일반 박스가 배경을 많이 포함할 수 있으므로 OBB 지원 여부와 학습 목표를 먼저 확인해야 한다.",
        "en_summary": "Datasets with many angled objects may include too much background in regular boxes, so OBB support and the training objective should be checked first.",
        "ko_focus": "기울어진 박스가 멋져 보여서 쓰는 것이 아니라 일반 박스로 생기는 오류가 실제 문제인지부터 봐야 합니다.",
        "en_focus": "Use rotated boxes only when regular-box error is a real problem, not because angled boxes look more precise.",
        "ko_actions": ["일반 박스에서 배경 비율이 과도한 샘플을 모읍니다.", "사용할 학습 프레임워크가 OBB를 지원하는지 확인합니다.", "도구와 포맷 변환 과정이 회전 정보를 보존하는지 검증합니다."],
        "en_actions": ["Collect samples where regular boxes include too much background.", "Confirm that the training framework supports OBB.", "Verify that tools and conversions preserve rotation data."],
        "signals": ["angle object", "background ratio", "obb support", "format support"],
        "ko_signals": ["기울어진 객체", "배경 비율", "OBB 지원", "포맷 지원"],
        "sources": ["cvat_formats", "labelstudio_bbox", "ultralytics_detect"],
        "tags": ["RotatedBox", "OBB", "Annotation", "ObjectDetection"],
    },
    {
        "slug": "label-version-control",
        "ko_title": "라벨 버전 관리: 데이터셋 v1, v2를 되돌릴 수 있게 만드는 방법",
        "en_title": "Label Version Control: Make Dataset v1 and v2 Reversible",
        "ko_summary": "라벨 버전 관리는 모델 실험을 재현하기 위해 이미지, 라벨, 클래스 파일, 지침서를 같은 버전으로 묶어 보관하는 작업이다.",
        "en_summary": "Label version control keeps images, labels, class files, and instructions tied to one version so model experiments can be reproduced.",
        "ko_focus": "라벨을 조금 고친 뒤 어떤 모델이 어떤 데이터로 학습됐는지 모르면 개선인지 우연인지 판단할 수 없습니다.",
        "en_focus": "If labels change but experiments do not record the dataset version, you cannot tell whether improvement is real or accidental.",
        "ko_actions": ["데이터셋 릴리스마다 버전 이름을 붙입니다.", "변경된 라벨과 변경 이유를 기록합니다.", "모델 학습 로그에 데이터셋 버전을 남깁니다."],
        "en_actions": ["Name every dataset release.", "Record changed labels and the reason for change.", "Write the dataset version into the model training log."],
        "signals": ["dataset version", "change log", "class file", "training run"],
        "ko_signals": ["데이터셋 버전", "변경 로그", "클래스 파일", "학습 실행"],
        "sources": ["fiftyone_api", "cvat_formats", "ultralytics_detect"],
        "tags": ["VersionControl", "Dataset", "Reproducibility", "MLOps"],
    },
    {
        "slug": "dataset-folder-structure",
        "ko_title": "객체 탐지 데이터셋 폴더 구조: images와 labels를 안전하게 맞추기",
        "en_title": "Object Detection Dataset Folder Structure: Keep Images and Labels Aligned",
        "ko_summary": "객체 탐지 데이터셋은 이미지와 라벨의 상대 위치가 맞아야 하며 train, val, test 폴더가 서로 섞이지 않아야 한다.",
        "en_summary": "An object detection dataset needs aligned image and label paths, and train, val, and test folders must not be mixed.",
        "ko_focus": "폴더 구조 오류는 모델 코드 문제가 아니라 데이터 패키징 문제인 경우가 많습니다.",
        "en_focus": "Folder-structure failures often look like model-code issues, but they are usually dataset packaging problems.",
        "ko_actions": ["이미지와 라벨 폴더를 같은 분할 이름으로 맞춥니다.", "라벨 파일이 없는 이미지와 이미지가 없는 라벨을 찾습니다.", "압축하거나 공유하기 전에 상대경로로 다시 열어 봅니다."],
        "en_actions": ["Match image and label folders with the same split names.", "Find images without labels and labels without images.", "Reopen the dataset with relative paths before zipping or sharing."],
        "signals": ["images folder", "labels folder", "orphan label", "relative path"],
        "ko_signals": ["images 폴더", "labels 폴더", "고아 라벨", "상대경로"],
        "sources": ["ultralytics_detect", "cvat_yolo", "ultralytics_utils"],
        "tags": ["FolderStructure", "YOLO", "Dataset", "Validation"],
    },
    {
        "slug": "model-error-analysis-labeling",
        "ko_title": "모델 오류 분석으로 라벨링 개선하기: 오탐과 미탐을 다음 작업으로 바꾸기",
        "en_title": "Improve Labeling with Model Error Analysis: Turn FP and FN into Next Work",
        "ko_summary": "모델 오류 분석은 성능표를 보는 데서 끝나지 않고 오탐, 미탐, 클래스 혼동 이미지를 다음 라벨링 작업으로 바꾸는 과정이다.",
        "en_summary": "Model error analysis should turn false positives, false negatives, and class confusion images into the next labeling tasks.",
        "ko_focus": "모델이 틀린 이유가 모델 구조가 아니라 라벨 기준과 데이터 공백일 수 있습니다.",
        "en_focus": "A model failure may come from label rules and data gaps, not only model architecture.",
        "ko_actions": ["오탐과 미탐 이미지를 별도 폴더로 모읍니다.", "라벨 누락인지 클래스 기준 문제인지 나눕니다.", "수정된 지침서로 새 배치를 다시 라벨링합니다."],
        "en_actions": ["Collect false-positive and false-negative images in separate folders.", "Separate missing labels from class-rule problems.", "Relabel the next batch with updated instructions."],
        "signals": ["false positive", "false negative", "class confusion", "relabel batch"],
        "ko_signals": ["오탐", "미탐", "클래스 혼동", "재라벨링 배치"],
        "sources": ["fiftyone_annotation", "ultralytics_detect", "labelstudio_bbox"],
        "tags": ["ErrorAnalysis", "ModelReview", "Labeling", "Dataset"],
    },
    {
        "slug": "annotation-cost-estimation",
        "ko_title": "이미지 라벨링 비용 산정: 장당 시간이 아니라 재작업률까지 계산하기",
        "en_title": "Annotation Cost Estimation: Count Rework, Not Only Time Per Image",
        "ko_summary": "라벨링 비용은 이미지 수와 장당 시간만으로 끝나지 않으며 지침 작성, 검수, 재작업, 포맷 변환, 데이터 정리 시간을 포함해야 한다.",
        "en_summary": "Annotation cost is not only image count times time per image; instructions, QA, rework, conversion, and cleanup should be included.",
        "ko_focus": "가장 싼 라벨링은 나중에 다시 고쳐야 하면 비쌀 수 있습니다.",
        "en_focus": "The cheapest labeling pass can become expensive if it creates rework later.",
        "ko_actions": ["파일 준비 시간을 별도 항목으로 둡니다.", "검수 비율과 재작업률을 가정합니다.", "클래스 난이도별로 장당 시간을 다르게 잡습니다."],
        "en_actions": ["Track file preparation as a separate cost.", "Estimate review rate and rework rate.", "Use different time assumptions by class difficulty."],
        "signals": ["time per image", "review cost", "rework rate", "conversion time"],
        "ko_signals": ["장당 시간", "검수 비용", "재작업률", "변환 시간"],
        "sources": ["labelstudio_bbox", "fiftyone_api", "cvat_formats"],
        "tags": ["AnnotationCost", "Planning", "Dataset", "Workflow"],
    },
    {
        "slug": "privacy-local-labeling",
        "ko_title": "민감한 이미지 라벨링과 로컬 우선 작업: 업로드 전에 확인할 보안 기준",
        "en_title": "Sensitive Image Labeling and Local-First Work: Security Checks Before Uploads",
        "ko_summary": "민감한 이미지 라벨링은 업로드 편의성보다 접근 권한, 저장 위치, 삭제 기준, 익명화 가능성을 먼저 확인해야 한다.",
        "en_summary": "Sensitive image labeling should check access rights, storage location, deletion rules, and anonymization before upload convenience.",
        "ko_focus": "데이터가 작아도 얼굴, 위치, 내부 설비, 고객 정보가 포함되면 도구 선택 기준이 달라집니다.",
        "en_focus": "Even small datasets require stricter tool choices when faces, locations, internal facilities, or customer information are present.",
        "ko_actions": ["이미지에 개인 정보나 내부 정보가 있는지 분류합니다.", "업로드가 필요한 도구와 로컬 작업 도구를 분리 비교합니다.", "작업 종료 후 라벨, 원본, 임시 파일 삭제 기준을 정합니다."],
        "en_actions": ["Classify whether images contain personal or internal information.", "Compare upload-based tools with local-first tools separately.", "Define deletion rules for labels, originals, and temporary files."],
        "signals": ["sensitive data", "local access", "upload policy", "deletion rule"],
        "ko_signals": ["민감 데이터", "로컬 접근", "업로드 정책", "삭제 기준"],
        "sources": ["mdn_filesystem", "fiftyone_annotation", "cvat_formats"],
        "tags": ["Privacy", "LocalFirst", "Security", "Labeling"],
    },
    {
        "slug": "augmentation-label-safety",
        "ko_title": "데이터 증강 전 라벨 안전성: 회전, 자르기, 뒤집기가 박스를 망가뜨리지 않게 하기",
        "en_title": "Label Safety Before Data Augmentation: Keep Boxes Valid After Crop and Flip",
        "ko_summary": "데이터 증강은 모델 일반화에 도움이 될 수 있지만 회전, 자르기, 확대가 라벨 박스와 클래스 의미를 깨지 않는지 확인해야 한다.",
        "en_summary": "Data augmentation can help generalization, but rotation, cropping, and scaling must not break boxes or class meaning.",
        "ko_focus": "증강은 데이터 부족을 마법처럼 해결하지 않습니다. 잘못된 증강은 틀린 라벨을 더 많이 만드는 과정이 될 수 있습니다.",
        "en_focus": "Augmentation is not magic for data scarcity. Bad augmentation can create more incorrect labels.",
        "ko_actions": ["증강 후 박스가 이미지 밖으로 나가지 않는지 봅니다.", "좌우 반전이 클래스 의미를 바꾸는지 확인합니다.", "증강 샘플을 실제 학습 전에 시각화합니다."],
        "en_actions": ["Check that boxes do not move outside the image after augmentation.", "Confirm whether horizontal flip changes class meaning.", "Visualize augmented samples before training."],
        "signals": ["augmented image", "box validity", "class meaning", "visual preview"],
        "ko_signals": ["증강 이미지", "박스 유효성", "클래스 의미", "시각 미리보기"],
        "sources": ["ultralytics_augment", "ultralytics_detect", "fiftyone_annotation"],
        "tags": ["Augmentation", "YOLO", "BoundingBox", "Training"],
    },
    {
        "slug": "exporting-yolo-training-ready",
        "ko_title": "YOLO 학습 준비 export 체크리스트: 라벨링 끝난 뒤 바로 훈련하지 말아야 하는 이유",
        "en_title": "YOLO Training-Ready Export Checklist: Do Not Train Immediately After Labeling",
        "ko_summary": "라벨링이 끝나도 학습 전에는 폴더 구조, 클래스 순서, 빈 라벨, 손상 이미지, 검증 샘플을 확인해야 한다.",
        "en_summary": "After labeling, training should wait until folder structure, class order, empty labels, corrupt images, and validation samples are checked.",
        "ko_focus": "학습이 시작된 뒤 발견한 데이터 오류는 원인 추적이 어렵습니다. export 직후 검증 단계가 더 싸고 빠릅니다.",
        "en_focus": "Data errors found after training begins are harder to trace. Validation immediately after export is cheaper and faster.",
        "ko_actions": ["이미지와 라벨 개수를 분할별로 비교합니다.", "`data.yaml`을 새 경로에서 다시 열어 봅니다.", "각 클래스에서 최소 몇 장을 시각 검수합니다."],
        "en_actions": ["Compare image and label counts by split.", "Open `data.yaml` from a fresh path.", "Visually review at least a few images from each class."],
        "signals": ["export folder", "label count", "yaml check", "sample preview"],
        "ko_signals": ["export 폴더", "라벨 개수", "yaml 확인", "샘플 미리보기"],
        "sources": ["ultralytics_detect", "cvat_yolo", "ultralytics_utils"],
        "tags": ["Export", "YOLO", "Training", "Checklist"],
    },
    {
        "slug": "label-format-migration-plan",
        "ko_title": "라벨 포맷 전환 계획: YOLO, COCO, CVAT 사이를 오갈 때 지킬 기준",
        "en_title": "Label Format Migration Plan: Move Between YOLO, COCO, and CVAT Safely",
        "ko_summary": "라벨 포맷 전환은 단순 변환 명령이 아니라 좌표 체계, 클래스 ID, 메타데이터, 지원하지 않는 속성 손실을 점검하는 마이그레이션이다.",
        "en_summary": "Label format migration is not just a conversion command; coordinate systems, class IDs, metadata, and unsupported attributes must be checked.",
        "ko_focus": "포맷이 바뀌면 어떤 정보가 사라지는지 모른 채 원본을 덮어쓰면 복구가 어려워집니다.",
        "en_focus": "If you overwrite originals without knowing which information is lost, recovery becomes difficult.",
        "ko_actions": ["원본 포맷은 읽기 전용 백업으로 보관합니다.", "변환 전후 샘플을 같은 이미지 위에 겹쳐 봅니다.", "회전, 마스크, 속성 같은 정보가 유지되는지 확인합니다."],
        "en_actions": ["Keep the source format as a read-only backup.", "Overlay before-and-after samples on the same image.", "Check whether rotation, masks, and attributes are preserved."],
        "signals": ["source format", "target format", "lost metadata", "overlay check"],
        "ko_signals": ["원본 포맷", "대상 포맷", "손실 메타데이터", "오버레이 확인"],
        "sources": ["cvat_formats", "ultralytics_coco", "cvat_yolo"],
        "tags": ["FormatMigration", "COCO", "YOLO", "CVAT"],
    },
    {
        "slug": "edge-case-gallery-dataset",
        "ko_title": "Edge Case Gallery 만들기: 애매한 라벨 기준을 이미지로 고정하는 법",
        "en_title": "Build an Edge Case Gallery: Freeze Ambiguous Label Rules with Images",
        "ko_summary": "Edge case gallery는 애매한 객체, 가림, 작은 물체, 클래스 혼동 사례를 모아 라벨러와 검수자가 같은 기준을 보게 하는 자료다.",
        "en_summary": "An edge-case gallery collects ambiguous objects, occlusion, small objects, and class confusion examples so labelers and reviewers share one standard.",
        "ko_focus": "애매한 기준은 문장만으로 전달하기 어렵습니다. 실제 이미지를 붙이면 다음 작업에서 같은 질문이 반복되는 비용이 줄어듭니다.",
        "en_focus": "Ambiguous rules are hard to communicate in text alone. Real images reduce repeated questions in later batches.",
        "ko_actions": ["질문이 나온 이미지를 따로 저장합니다.", "결정된 기준을 이미지 아래 한 문장으로 씁니다.", "지침서 업데이트 때 edge case gallery도 함께 버전업합니다."],
        "en_actions": ["Save images that triggered questions.", "Write the decided rule under each image in one sentence.", "Version the edge-case gallery together with the instructions."],
        "signals": ["ambiguous image", "decision note", "gallery version", "review training"],
        "ko_signals": ["애매한 이미지", "결정 메모", "갤러리 버전", "검수 교육"],
        "sources": ["labelstudio_bbox", "fiftyone_annotation", "cvat_formats"],
        "tags": ["EdgeCases", "Instructions", "Annotation", "Review"],
    },
    {
        "slug": "qa-before-yolo-training",
        "ko_title": "YOLO 학습 전 QA 루틴: 데이터 오류를 모델 문제로 착각하지 않기",
        "en_title": "QA Before YOLO Training: Do Not Mistake Data Errors for Model Problems",
        "ko_summary": "YOLO 학습 전 QA는 라벨 누락, 클래스 순서 오류, 이미지 손상, 분할 누수, 극단적 박스를 먼저 잡아 모델 실험 시간을 아낀다.",
        "en_summary": "QA before YOLO training catches missing labels, class-order mistakes, corrupt images, split leakage, and extreme boxes before model time is wasted.",
        "ko_focus": "모델 튜닝 전에 데이터 QA를 통과하지 못하면 하이퍼파라미터 실험은 노이즈를 키우는 일이 됩니다.",
        "en_focus": "If the dataset has not passed QA, hyperparameter tuning mostly amplifies noise.",
        "ko_actions": ["라벨 파일이 비어 있는 경우와 누락된 경우를 구분합니다.", "박스 좌표가 0과 1 사이인지 확인합니다.", "클래스별 샘플 미리보기를 만든 뒤 학습을 시작합니다."],
        "en_actions": ["Separate intentionally empty labels from missing labels.", "Check whether box coordinates are between 0 and 1.", "Create per-class previews before starting training."],
        "signals": ["missing label", "empty label", "coordinate range", "class preview"],
        "ko_signals": ["누락 라벨", "빈 라벨", "좌표 범위", "클래스 미리보기"],
        "sources": ["ultralytics_detect", "ultralytics_utils", "fiftyone_annotation"],
        "tags": ["QA", "YOLO", "Training", "Dataset"],
    },
    {
        "slug": "labeler-onboarding-checklist",
        "ko_title": "라벨러 온보딩 체크리스트: 첫날부터 같은 기준으로 작업하게 만들기",
        "en_title": "Labeler Onboarding Checklist: Start New Annotators with the Same Standard",
        "ko_summary": "새 라벨러는 도구 사용법보다 클래스 기준, 예외 처리, 저장 규칙, 질문 경로를 먼저 익혀야 재작업을 줄일 수 있다.",
        "en_summary": "New labelers need class rules, edge-case handling, save rules, and question paths before tool speed, otherwise rework increases.",
        "ko_focus": "첫날 작업량을 많이 만드는 것보다 같은 이미지에서 같은 판단을 하게 만드는 것이 더 중요합니다.",
        "en_focus": "On day one, consistent decisions on the same images matter more than high volume.",
        "ko_actions": ["공통 연습 이미지 20장을 먼저 라벨링합니다.", "검수자가 기준 차이를 바로 피드백합니다.", "질문은 채팅보다 추적 가능한 로그에 남깁니다."],
        "en_actions": ["Label 20 shared practice images first.", "Have a reviewer give immediate feedback on standard differences.", "Put questions in a trackable log rather than only chat."],
        "signals": ["practice batch", "review feedback", "question log", "approval gate"],
        "ko_signals": ["연습 배치", "검수 피드백", "질문 로그", "승인 게이트"],
        "sources": ["labelstudio_bbox", "fiftyone_api", "cvat_formats"],
        "tags": ["Onboarding", "Labeling", "TeamWorkflow", "Review"],
    },
    {
        "slug": "dataset-handoff-for-training",
        "ko_title": "라벨링 팀에서 학습 팀으로 데이터 넘기기: handoff 문서에 들어갈 것",
        "en_title": "Dataset Handoff for Training Teams: What to Include in the Handoff Document",
        "ko_summary": "데이터셋 handoff는 압축 파일 전달이 아니라 버전, 클래스 규칙, 분할 방식, 알려진 한계, 검수 결과를 함께 넘기는 과정이다.",
        "en_summary": "Dataset handoff is not just sending a zip file; it should include version, class rules, split method, known limits, and QA results.",
        "ko_focus": "학습 팀이 데이터의 의도와 한계를 모르면 오류가 생겼을 때 라벨 문제인지 모델 문제인지 늦게 알게 됩니다.",
        "en_focus": "If the training team does not know the dataset intent and limits, label problems and model problems are separated too late.",
        "ko_actions": ["데이터셋 버전과 생성 날짜를 적습니다.", "클래스 사전과 edge case 기준을 포함합니다.", "검수 표본 수와 발견된 주요 문제를 요약합니다."],
        "en_actions": ["Write dataset version and creation date.", "Include the class dictionary and edge-case rules.", "Summarize review sample counts and major issues found."],
        "signals": ["handoff note", "dataset version", "known limits", "qa summary"],
        "ko_signals": ["handoff 문서", "데이터셋 버전", "알려진 한계", "QA 요약"],
        "sources": ["ultralytics_detect", "fiftyone_api", "cvat_formats"],
        "tags": ["Handoff", "Dataset", "MLOps", "Training"],
    },
    {
        "slug": "browser-based-labeling-pros-cons",
        "ko_title": "브라우저 기반 라벨링 도구 장단점: 설치 없음과 파일 접근 권한 사이의 균형",
        "en_title": "Browser-Based Labeling Tools: Balance No Install with File Access Control",
        "ko_summary": "브라우저 기반 라벨링은 설치 부담을 줄이지만 파일 접근 권한, 브라우저 지원, 저장 위치, 대용량 작업 기준을 확인해야 한다.",
        "en_summary": "Browser-based labeling reduces installation friction, but file permissions, browser support, save location, and large-batch limits must be checked.",
        "ko_focus": "설치가 없다는 장점은 명확하지만, 작업자는 어떤 폴더를 허용했고 어디에 저장되는지 이해해야 합니다.",
        "en_focus": "No-install workflows are useful, but workers must understand which folder was granted and where labels are saved.",
        "ko_actions": ["지원 브라우저와 파일 접근 권한 흐름을 확인합니다.", "작업 전 테스트 폴더에서 저장 동작을 시험합니다.", "대용량 이미지 묶음은 작은 배치로 나눕니다."],
        "en_actions": ["Check supported browsers and the file permission flow.", "Test save behavior in a sandbox folder first.", "Split large image sets into smaller batches."],
        "signals": ["browser support", "folder permission", "save path", "batch size"],
        "ko_signals": ["브라우저 지원", "폴더 권한", "저장 경로", "배치 크기"],
        "sources": ["mdn_filesystem", "labelstudio_bbox", "cvat_formats"],
        "tags": ["BrowserTool", "LocalFirst", "FileAccess", "Labeling"],
    },
    {
        "slug": "image-labeling-project-plan",
        "ko_title": "이미지 라벨링 프로젝트 계획서: 수집, 라벨링, 검수, 학습을 한 흐름으로 묶기",
        "en_title": "Image Labeling Project Plan: Connect Collection, Annotation, QA, and Training",
        "ko_summary": "이미지 라벨링 프로젝트는 라벨링 화면에서 시작하지 않고 목표 정의, 데이터 수집, 기준 문서, 검수, 학습 피드백 루프로 설계해야 한다.",
        "en_summary": "An image labeling project should start before the labeling screen, with objective, collection, instructions, QA, and training feedback designed as one loop.",
        "ko_focus": "도구 선택보다 먼저 어떤 모델 실패를 줄이기 위한 데이터셋인지 정의해야 합니다.",
        "en_focus": "Before choosing a tool, define which model failure the dataset is meant to reduce.",
        "ko_actions": ["탐지할 객체와 쓰지 않을 객체를 먼저 적습니다.", "작은 파일럿 배치로 기준과 시간을 검증합니다.", "학습 결과가 다음 라벨링 우선순위를 바꾸도록 루프를 만듭니다."],
        "en_actions": ["Write target objects and excluded objects first.", "Use a small pilot batch to validate standards and time estimates.", "Make training results change the next labeling priority."],
        "signals": ["project objective", "pilot batch", "qa gate", "feedback loop"],
        "ko_signals": ["프로젝트 목표", "파일럿 배치", "QA 게이트", "피드백 루프"],
        "sources": ["fiftyone_annotation", "labelstudio_bbox", "ultralytics_detect"],
        "tags": ["ProjectPlan", "Annotation", "Dataset", "Workflow"],
    },
]


LEGACY_IMAGES = {
    "yolo-label-format": ["yolo-label-format-hero.png"],
    "coco-to-yolo-conversion": ["coco-to-yolo-conversion-hero.png"],
    "image-labeling-classes": ["image-labeling-classes-hero.png"],
    "local-image-labeling-workflow": ["local-image-labeling-workflow-hero.png"],
    "easy-labeling-yolo-dataset": ["easy-labeling-yolo-dataset-hero.png"],
}


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def blend(a: tuple[int, int, int], b: tuple[int, int, int], ratio: float) -> tuple[int, int, int]:
    return tuple(int(a[i] * (1 - ratio) + b[i] * ratio) for i in range(3))


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, title: str, labels: list[str], palette: tuple[str, str], variant: int) -> None:
    width, height = 1200, 675
    base = hex_to_rgb(palette[0])
    accent = hex_to_rgb(palette[1])
    slate = (15, 23, 42)
    panel = (245, 247, 250)
    rows: list[bytes] = []
    seed = sum(ord(ch) for ch in title) % 210

    for y in range(height):
        vertical = y / (height - 1)
        left = blend(base, panel, 0.10 + vertical * 0.12)
        center = blend(slate, base, 0.36 + vertical * 0.08)
        right = blend(accent, slate, 0.28 + variant * 0.03)
        card = blend(panel, accent, 0.08)
        mark = blend(accent, panel, 0.18)

        if 86 <= y <= 162:
            row = bytes(left) * 96 + bytes(mark) * (520 + seed) + bytes(center) * (184 - seed) + bytes(right) * 400
        elif 220 <= y <= 545:
            band = (y - 220) // 58
            if (y - 220) % 58 < 34:
                row = bytes(left) * 88 + bytes(card) * 472 + bytes(mark) * 34 + bytes(center) * 246 + bytes(right) * 360
            elif band % 2 == 0:
                row = bytes(left) * 88 + bytes(card) * 560 + bytes(center) * 192 + bytes(right) * 360
            else:
                row = bytes(left) * 88 + bytes(card) * 438 + bytes(center) * 314 + bytes(right) * 360
        elif 166 <= y <= 590 and (y + seed) % 122 < 16:
            row = bytes(left) * 640 + bytes(center) * 190 + bytes(mark) * 260 + bytes(right) * 110
        elif y % 74 == 0:
            row = bytes(blend(left, panel, 0.20)) * width
        else:
            row = bytes(left) * 626 + bytes(center) * 258 + bytes(right) * 316
        rows.append(b"\x00" + row)

    raw = b"".join(rows)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + png_chunk(b"IDAT", zlib.compress(raw, 6))
        + png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def bounded_text(value: str, minimum: int, maximum: int, suffix: str) -> str:
    text = value if len(value) >= minimum else f"{value} {suffix}"
    if len(text) > maximum:
        text = text[: maximum - 3].rstrip() + "..."
    return text


def seo_title(topic: dict[str, object], lang: str) -> str:
    title = str(topic["ko_title"] if lang == "ko" else topic["en_title"])
    return bounded_text(title, 10 if lang == "ko" else 20, 70, "image labeling guide")


def seo_description(topic: dict[str, object], lang: str) -> str:
    if lang == "ko":
        return bounded_text(str(topic["ko_summary"]), 60, 170, "Easy Labeling 작업 흐름과 검수 기준을 함께 정리합니다.")
    return bounded_text(
        str(topic["en_summary"]),
        80,
        170,
        "It connects Easy Labeling usage with dataset QA and training-ready exports.",
    )


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 9) % len(TOPICS)]]
    category_path = KO_CATEGORY if lang == "ko" else EN_CATEGORY
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def ko_signal_items(topic: dict[str, object]) -> str:
    templates = [
        "작업 전에 기준을 문서로 고정합니다. 라벨러가 같은 이미지를 봤을 때 같은 결정을 내릴 수 있도록 포함 기준, 제외 기준, 예외 예시를 함께 둡니다.",
        "파일럿 배치에서 바로 확인합니다. 전체 데이터를 열기 전에 20~50장 샘플로 좌표, 클래스, 저장 경로가 학습 폴더와 맞는지 봅니다.",
        "애매한 사례를 질문 로그나 edge case gallery에 남깁니다. 반복 질문이 생기면 개인 판단으로 넘기지 말고 지침서 버전을 올립니다.",
        "학습팀에 넘기기 전 검수 기록과 함께 묶습니다. 이미지, 라벨, 클래스 파일, 변환 스크립트, 검수 샘플이 같은 버전을 가리켜야 합니다.",
    ]
    return "\n".join(
        f"- **{signal}**: {templates[index % len(templates)]}"
        for index, signal in enumerate(topic["ko_signals"])
    )


def en_signal_items(topic: dict[str, object]) -> str:
    templates = [
        "Freeze the rule before labeling starts. Include positive examples, exclusion rules, and edge cases so two labelers can make the same decision on the same image.",
        "Check it in a pilot batch first. Before opening the full dataset, use 20 to 50 samples to verify coordinates, classes, and save paths against the training folder.",
        "Capture ambiguous cases in a question log or edge-case gallery. When the same question repeats, update the instruction version instead of relying on individual judgment.",
        "Package it with the QA record before handoff. Images, labels, class files, conversion scripts, and reviewed samples should point to the same dataset version.",
    ]
    return "\n".join(
        f"- **{signal}**: {templates[index % len(templates)]}"
        for index, signal in enumerate(topic["signals"])
    )


def ko_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["ko_actions"])


def en_action_items(topic: dict[str, object]) -> str:
    return "\n".join(f"- {action}" for action in topic["en_actions"])


def ko_context(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return (
        f"이 주제는 라벨을 더 많이 그리는 방법보다 **{first}**와 **{second}**를 안정적으로 남기는 방법에 가깝습니다. "
        "객체 탐지 프로젝트에서는 작은 좌표 오류, 클래스 순서 변경, 폴더 구조 실수가 학습 실패처럼 보일 수 있습니다. "
        "그래서 작업자는 도구 사용법과 함께 데이터셋 계약을 문서로 남겨야 합니다."
    )


def en_context(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return (
        f"This topic is less about drawing more boxes and more about preserving **{first}** and **{second}** consistently. "
        "In object detection, small coordinate errors, class-order changes, and folder mistakes can look like model failures. "
        "That is why tool usage and the dataset contract should be documented together."
    )


def ko_workflow(topic: dict[str, object]) -> str:
    first_action = str(topic["ko_actions"][0])
    second_action = str(topic["ko_actions"][1])
    return (
        f"작업은 작은 파일럿 배치에서 시작합니다. 먼저 {first_action} 그 다음 {second_action} "
        "20~50장 정도의 샘플을 Easy Labeling에서 열어 실제 박스를 그려 보면 지침서의 빈칸이 빨리 드러납니다. "
        "이 단계에서 나온 질문은 채팅으로 흘려보내지 말고 클래스 사전이나 edge case gallery에 반영해야 합니다."
    )


def en_workflow(topic: dict[str, object]) -> str:
    first_action = str(topic["en_actions"][0])
    second_action = str(topic["en_actions"][1])
    return (
        f"Start with a small pilot batch. First, {first_action.lower()} Then, {second_action.lower()} "
        "Opening 20 to 50 sample images in Easy Labeling quickly exposes missing rules in the instruction document. "
        "Questions from this step should update the class dictionary or edge-case gallery rather than disappear in chat."
    )


def ko_review_example(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    third = topic["ko_signals"][2]
    return (
        f"검수자는 전체 이미지를 다시 라벨링하지 않아도 됩니다. 샘플을 열고 **{first}** 기준이 지켜졌는지, "
        f"그리고 **{third}**가 프로젝트 규칙과 맞는지 먼저 봅니다. 문제가 반복되면 해당 라벨러의 전체 배치를 의심하기보다 "
        "지침서가 충분히 구체적인지, 예시 이미지가 부족한지, 도구 저장 설정이 헷갈리게 되어 있는지 순서대로 확인합니다."
    )


def en_review_example(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    third = topic["signals"][2]
    return (
        f"Reviewers do not need to relabel every image. Open samples and check whether **{first}** follows the rule, "
        f"then confirm that **{third}** matches the project standard. If the issue repeats, inspect the instruction document, "
        "example images, and save settings before blaming an individual labeler."
    )


def ko_checklist(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return "\n".join(
        [
            f"- 작업 전 **{first}** 기준을 문서에서 확인합니다.",
            f"- 파일 저장 후 **{second}**가 실제 라벨 파일에 반영됐는지 샘플로 확인합니다.",
            "- 라벨링 중 생긴 질문은 다음 배치 전에 지침서로 되돌립니다.",
            "- 학습팀에 넘기기 전 이미지, 라벨, 클래스 파일, 검수 기록을 같은 버전으로 묶습니다.",
        ]
    )


def en_checklist(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return "\n".join(
        [
            f"- Before labeling, confirm the **{first}** rule in the instruction document.",
            f"- After saving, spot-check that **{second}** appears correctly in label files.",
            "- Turn questions from labeling into instruction updates before the next batch.",
            "- Before handoff, package images, labels, class files, and QA notes as one version.",
        ]
    )


def ko_faq(topic: dict[str, object]) -> str:
    first = topic["ko_signals"][0]
    second = topic["ko_signals"][1]
    return dedent(f"""\
    ### {topic["ko_title"]}는 Easy Labeling만 쓰면 해결되나요?

    아닙니다. Easy Labeling은 로컬 이미지와 YOLO 박스를 다루는 작업을 빠르게 만들 수 있지만, **{first}** 기준은 프로젝트가 직접 정해야 합니다. 도구와 지침서를 같이 써야 재작업이 줄어듭니다.

    ### 작은 데이터셋도 이런 검수가 필요한가요?

    작은 데이터셋일수록 한두 개 오류가 결과에 크게 보일 수 있습니다. 최소한 **{second}**와 클래스 순서는 샘플로 확인한 뒤 학습으로 넘기는 편이 안전합니다.

    ### 언제 다시 라벨링해야 하나요?

    같은 유형의 오류가 여러 이미지에서 반복되거나 모델 오류 분석에서 특정 클래스가 계속 흔들리면 다시 라벨링해야 합니다. 단순히 박스 하나를 고치는 수준이 아니라 기준 문서를 고친 뒤 같은 기준으로 배치를 다시 보는 것이 좋습니다.
    """)


def en_faq(topic: dict[str, object]) -> str:
    first = topic["signals"][0]
    second = topic["signals"][1]
    return dedent(f"""\
    ### Does {topic["en_title"]} become easy just by using Easy Labeling?

    No. Easy Labeling can make local images and YOLO boxes faster to handle, but the project must define the **{first}** rule. The tool and instruction document need to work together.

    ### Do small datasets need this much QA?

    Yes. In a small dataset, one or two mistakes can move results visibly. At minimum, spot-check **{second}** and class order before handing data to training.

    ### When should labels be redone?

    Relabel when the same error type repeats across images or model analysis shows a class keeps drifting. Fix the instruction document first, then review the batch under the updated rule.
    """)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["ko_title"]}
    seo_title: >
      {seo_title(topic, "ko")}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 17:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: {slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.36
      image_description: >
        {topic["ko_title"]}의 이미지 라벨링 흐름과 검수 기준을 요약한 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {seo_description(topic, "ko")}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    이 글은 **{topic["ko_title"]}**를 라벨링 속도가 아니라 데이터셋 품질 기준으로 정리합니다. Easy Labeling은 작업을 빠르게 만들 수 있지만, 학습 가능한 데이터는 클래스 규칙과 검수 루틴이 함께 있을 때 만들어집니다.

    {topic["ko_summary"]}

    도구 실행: [Easy Labeling]({TOOL_URL})

    ![{topic["ko_title"]} 라벨링 품질 흐름도]({image_dir}/hero.png)

    ## 이 작업이 줄이는 문제

    {topic["ko_focus"]}

    {ko_context(topic)}

    ## 먼저 확인할 품질 신호

    {ko_signal_items(topic)}

    ![{topic["ko_title"]} 라벨링 검수 체크리스트]({image_dir}/checklist.png)

    ## Easy Labeling 적용 흐름

    {ko_workflow(topic)}

    Easy Labeling은 브라우저에서 로컬 이미지 폴더를 열어 YOLO 박스를 작성하는 흐름에 맞춰져 있습니다. 업로드 기반 도구가 부담스러운 파일, 빠르게 확인해야 하는 샘플 배치, 클래스 기준을 실험하는 초기 데이터셋에 특히 잘 맞습니다. 다만 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다.

    ![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면]({SAMPLE_IMAGE})

    ## 검수 예시

    {ko_review_example(topic)}

    ## 실무 체크리스트

    {ko_checklist(topic)}

    ## 자주 묻는 질문

    {ko_faq(topic)}

    ## 참고할 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["en_title"]}
    seo_title: >
      {seo_title(topic, "en")}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 17:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: {slug}
    header:
      teaser: {image_dir}/hero.png
      overlay_image: {image_dir}/hero.png
      overlay_filter: 0.36
      image_description: >
        Image labeling workflow diagram summarizing dataset QA and review criteria for this topic.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {seo_description(topic, "en")}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    This guide frames **{topic["en_title"]}** as a dataset-quality workflow rather than a labeling-speed trick. Easy Labeling can make the work faster, but trainable data still depends on class rules and review routines.

    {topic["en_summary"]}

    Launch the tool: [Easy Labeling]({TOOL_URL})

    ![{topic["en_title"]} labeling quality workflow diagram]({image_dir}/hero.png)

    ## What This Work Reduces

    {topic["en_focus"]}

    {en_context(topic)}

    ## Quality Signals To Check First

    {en_signal_items(topic)}

    ![{topic["en_title"]} labeling review checklist]({image_dir}/checklist.png)

    ## Easy Labeling Workflow

    {en_workflow(topic)}

    Easy Labeling fits a browser-based local workflow for opening image folders and saving YOLO bounding boxes. It is especially useful for files that should not be uploaded casually, small review batches, and early datasets where class rules are still being tested. The tool does not replace project standards, so the instruction document before labeling and the QA routine after labeling still matter.

    ![Easy Labeling sample screen for drawing object detection boxes]({SAMPLE_IMAGE})

    ## Review Example

    {en_review_example(topic)}

    ## Practical Checklist

    {en_checklist(topic)}

    ## FAQ

    {en_faq(topic)}

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Easy Labeling"
        layout: archive
        permalink: /ko_easy_labeling/
        lang: ko
        seo_description: >
          Easy Labeling, YOLO 라벨 포맷, COCO 변환, 클래스 관리, 라벨 검수, 데이터셋 분할, 로컬 이미지 라벨링 워크플로우를 정리한 실무 글 모음입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Easy Labeling 카테고리는 이미지 라벨링 작업을 더 빠르고 일관되게 만드는 방법을 다룹니다. YOLO 라벨 포맷, COCO 변환, 클래스 사전, bounding box 품질, train/val/test 분할, 데이터셋 QA, active learning 루프, 로컬 우선 작업처럼 모델 학습 전 데이터 품질을 좌우하는 주제를 모았습니다.

        각 글은 단순한 도구 소개보다 실제 데이터셋이 깨지는 지점을 중심으로 설명합니다. 작은 샘플 세트로 클래스 기준을 먼저 맞추고, Easy Labeling에서 라벨을 저장한 뒤, 폴더 구조와 `data.yaml`까지 검수하는 흐름을 권장합니다.

        처음에는 로컬 라벨링 워크플로우와 YOLO 포맷을 읽고, 이후 bounding box 품질, 라벨 지침서, train/val/test 분할, QA 루틴으로 확장하면 좋습니다.

        ## 먼저 읽기

        - [로컬 이미지 라벨링 워크플로우](/ko_easy_labeling/local-image-labeling-workflow/)
        - [Easy Labeling으로 YOLO 데이터셋 만들기](/ko_easy_labeling/easy-labeling-yolo-dataset/)
        - [YOLO 라벨 포맷 이해하기](/ko_easy_labeling/yolo-label-format/)
        - [Bounding Box 품질 체크리스트](/ko_easy_labeling/bounding-box-quality-checklist/)
        - [Train, Val, Test 데이터셋 분할](/ko_easy_labeling/dataset-split-train-val-test/)

        ## 최신 글

        {% assign posts = site.categories["ko_easy_labeling"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
    ---
    title: "Easy Labeling"
    layout: archive
    permalink: /en_easy_labeling/
    lang: en
    seo_description: >
      Easy Labeling guides for YOLO label format, COCO conversion, class management, annotation QA, dataset splits, local image labeling, and training-ready exports.
    sidebar:
        nav: "sidebar-category"
    ---

    The Easy Labeling category explains how to make image labeling faster, more consistent, and easier to verify before model training. It covers YOLO label format, COCO conversion, class dictionaries, bounding box quality, train/val/test splits, dataset QA, active learning loops, and local-first annotation workflows.

    The articles focus on the places where real datasets break, not only tool buttons. A practical workflow starts with a small sample set, freezes class rules, saves labels in Easy Labeling, then checks folder structure and `data.yaml` before training.

    Start with the local labeling workflow and YOLO format, then move into bounding box quality, labeling instructions, dataset split rules, and QA before training.

    ## Start Here

    - [Local Image Labeling Workflow](/en_easy_labeling/local-image-labeling-workflow/)
    - [Create a YOLO Dataset with Easy Labeling](/en_easy_labeling/easy-labeling-yolo-dataset/)
    - [YOLO Label Format](/en_easy_labeling/yolo-label-format/)
    - [Bounding Box Quality Checklist](/en_easy_labeling/bounding-box-quality-checklist/)
    - [Train, Val, Test Dataset Split](/en_easy_labeling/dataset-split-train-val-test/)

    ## Latest Articles

    {% assign posts = site.categories["en_easy_labeling"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#0f172a", "#06b6d4"),
        ("#164e63", "#f97316"),
        ("#14532d", "#eab308"),
        ("#7f1d1d", "#38bdf8"),
    ]
    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        image_dir = ROOT / "images" / f"{POST_DATE}-{slug}"
        image_dir.mkdir(parents=True, exist_ok=True)
        for legacy_name in LEGACY_IMAGES.get(slug, []):
            legacy_path = image_dir / legacy_name
            if legacy_path.exists():
                legacy_path.unlink()
        palette = palettes[index % len(palettes)]
        write_png(image_dir / "hero.png", str(topic["en_title"]), [str(item) for item in topic["signals"]], palette, index % 3)
        write_png(image_dir / "checklist.png", str(topic["en_title"]), [str(item) for item in topic["en_actions"]], (palette[0], "#facc15"), (index + 1) % 3)
        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(ko_post(topic, index)), encoding="utf-8")
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(normalize_markdown(en_post(topic, index)), encoding="utf-8")
    (ROOT / "_pages" / "category-ko_easy_labeling.md").write_text(normalize_markdown(category_page("ko")), encoding="utf-8")
    (ROOT / "_pages" / "category-en_easy_labeling.md").write_text(normalize_markdown(category_page("en")), encoding="utf-8")
    print(f"Generated {len(TOPICS)} paired Easy Labeling campaign topics.")


if __name__ == "__main__":
    main()
