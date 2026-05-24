from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
POST_DIRS = [ROOT / "_posts" / "en", ROOT / "_posts" / "ko"]
TODAY = "2026-05-24T00:00:00+09:00"


EN_SCOPE = """Current Easy Labeling is not only a YOLO box editor. The repository README documents two workflow tabs: `Detection` for YOLO bounding boxes and `Segmentation` for brush-based masks. Detection saves `label/<image>.txt` in YOLO format. Segmentation saves `mask/<image>.png` and `mask/<image>.seg.json`.

Use Desktop Chrome or Edge for the browser version because local folder read/write depends on the File System Access API. The repository also documents an Electron Windows build for teams that prefer an installed local app. Detection list actions such as multi-edit, alignment, distribution, copy, and paste should be treated as Detection-focused features, while Segmentation editing is brush, eraser, connected-region selection, drag, and class-change work."""

KO_SCOPE = """현재 Easy Labeling은 YOLO 박스 전용 편집기만은 아닙니다. 저장소 README 기준 상단에는 `Detection`과 `Segmentation` 두 워크플로우 탭이 있습니다. Detection은 YOLO bounding box를 다루고 `label/<image>.txt`로 저장합니다. Segmentation은 브러시 기반 마스크를 다루며 `mask/<image>.png`와 `mask/<image>.seg.json`을 저장합니다.

브라우저 버전은 로컬 폴더 읽기/쓰기에 File System Access API가 필요하므로 Desktop Chrome 또는 Edge 사용을 전제로 보는 편이 안전합니다. 저장소에는 Windows용 Electron 빌드도 문서화되어 있습니다. 박스 목록 기반 다중 편집, 정렬, 분배, 복사/붙여넣기는 Detection 중심 기능으로 보고, Segmentation은 브러시, 지우개, 연결 영역 선택, 드래그 이동, 클래스 변경 중심으로 검수해야 합니다."""

EN_SOURCE = "- [Easy Labeling GitHub Repository](https://github.com/MouseBall54/easy_labeling): current tool scope, Detection/Segmentation workflows, save formats, browser requirements, and Electron build notes."
KO_SOURCE = "- [Easy Labeling GitHub 저장소](https://github.com/MouseBall54/easy_labeling): 현재 기능 범위, Detection/Segmentation 워크플로우, 저장 형식, 브라우저 조건, Electron 빌드 참고 자료입니다."


OLD_EN_WORKFLOW = """Easy Labeling fits a browser-based local workflow for opening image folders and saving YOLO bounding boxes. It is especially useful for files that should not be uploaded casually, small review batches, and early datasets where class rules are still being tested. The tool does not replace project standards, so the instruction document before labeling and the QA routine after labeling still matter."""
NEW_EN_WORKFLOW = """Easy Labeling fits a local-first image annotation workflow. In the current repository, Detection handles YOLO bounding boxes and Segmentation handles brush-based masks, so choose the tab according to the dataset contract before labeling starts. The tool does not replace project standards, so the instruction document before labeling and the QA routine after labeling still matter."""

OLD_KO_WORKFLOW = """Easy Labeling은 브라우저에서 로컬 이미지 폴더를 열어 YOLO 박스를 작성하는 흐름에 맞춰져 있습니다. 업로드 기반 도구가 부담스러운 파일, 빠르게 확인해야 하는 샘플 배치, 클래스 기준을 실험하는 초기 데이터셋에 특히 잘 맞습니다. 다만 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다."""
NEW_KO_WORKFLOW = """Easy Labeling은 로컬 우선 이미지 주석 작업에 맞춰져 있습니다. 현재 저장소 기준 Detection은 YOLO bounding box를, Segmentation은 브러시 기반 마스크를 다루므로 라벨링 전에 데이터셋 계약에 맞는 탭을 먼저 정해야 합니다. 최종 품질은 도구가 자동으로 보장하지 않으므로 작업 전 지침서와 작업 후 검수 루틴이 필요합니다."""


def is_easy_labeling_post(text: str) -> bool:
    return "  - en_easy_labeling" in text or "  - ko_easy_labeling" in text


def lang_of(text: str) -> str:
    return "ko" if "\nlang: ko\n" in text else "en"


def ensure_last_modified(text: str) -> str:
    if "last_modified_at:" in text.split("---", 2)[1]:
        return re.sub(r"last_modified_at: .+", f"last_modified_at: {TODAY}", text, count=1)
    return re.sub(r"(date: .+\n)", rf"\1last_modified_at: {TODAY}\n", text, count=1)


def insert_scope_after_workflow(text: str, lang: str) -> str:
    if "## Repository-Checked Tool Scope" in text or "## 저장소 기준 기능 범위" in text:
        return text
    if lang == "en":
        marker = "![Easy Labeling sample screen"
        heading = "## Repository-Checked Tool Scope"
        scope = EN_SCOPE
    else:
        marker = "![Easy Labeling에서 객체 탐지 박스를 그리는 샘플 화면]"
        heading = "## 저장소 기준 기능 범위"
        scope = KO_SCOPE
    idx = text.find(marker)
    if idx == -1:
        return text
    block = f"\n## {heading.split('## ', 1)[-1]}\n\n{scope}\n\n"
    return text[:idx] + block + text[idx:]


def ensure_source_note(text: str, lang: str) -> str:
    source_line = KO_SOURCE if lang == "ko" else EN_SOURCE
    headings = ["## Source Notes", "## 참고할 자료"]
    for heading in headings:
        idx = text.find(heading)
        if idx != -1:
            section = text[idx : text.find("\n## ", idx + 1) if text.find("\n## ", idx + 1) != -1 else len(text)]
            if "github.com/MouseBall54/easy_labeling" in section:
                return text
            line_end = text.find("\n", idx)
            return text[: line_end + 1] + "\n" + source_line + "\n" + text[line_end + 1 :]
    related = "## Related Reading" if lang == "en" else "## 함께 보면 좋은 글"
    idx = text.find(related)
    if idx != -1:
        heading = "## Source Notes" if lang == "en" else "## 참고할 자료"
        return text[:idx] + f"{heading}\n\n{source_line}\n\n" + text[idx:]
    return text.rstrip() + ("\n\n## Source Notes\n\n" if lang == "en" else "\n\n## 참고할 자료\n\n") + source_line + "\n"


def revise_generated(text: str, lang: str) -> str:
    if lang == "en":
        text = text.replace(OLD_EN_WORKFLOW, NEW_EN_WORKFLOW)
        text = re.sub(
            r"No\. Easy Labeling can make local images and YOLO boxes faster to handle, but the project must define the \*\*(.+?)\*\* rule\. The tool and instruction document need to work together\.",
            r"No. Easy Labeling can speed up local Detection box work and also provides a Segmentation mask workflow, but the project must still define the **\1** rule. The tool and instruction document need to work together.",
            text,
        )
        text = insert_scope_after_workflow(text, lang)
    else:
        text = text.replace(OLD_KO_WORKFLOW, NEW_KO_WORKFLOW)
        text = re.sub(
            r"아닙니다\. Easy Labeling은 로컬 이미지와 YOLO 박스를 다루는 작업을 빠르게 만들 수 있지만, \*\*(.+?)\*\* 기준은 프로젝트가 직접 정해야 합니다\. 도구와 지침서를 같이 써야 재작업이 줄어듭니다\.",
            r"아닙니다. Easy Labeling은 로컬 Detection 박스 작업을 빠르게 만들고 Segmentation 마스크 작업도 제공하지만, **\1** 기준은 프로젝트가 직접 정해야 합니다. 도구와 지침서를 같이 써야 재작업이 줄어듭니다.",
            text,
        )
        text = insert_scope_after_workflow(text, lang)
    return text


def revise_early_posts(text: str, path: Path, lang: str) -> str:
    name = path.name
    if name == "2025-07-13-easy-labeling-development.md":
        if lang == "en":
            text = text.replace(
                'title: "Introducing Easy Labeling: A Free Web-Based Tool for YOLO Object Detection"',
                'title: "Introducing Easy Labeling: Local Detection and Segmentation Annotation Tool"',
            )
            text = text.replace(
                "a web-based image annotation tool I developed to simplify the creation of datasets, especially for **YOLO format** object detection.",
                "a local-first image annotation tool I developed for computer vision datasets. The current repository supports both **Detection** for YOLO bounding boxes and **Segmentation** for brush-based masks.",
            )
            text = text.replace(
                "Easy Labeling was created to streamline the often tedious process of building high-quality datasets for object detection models, particularly those in the YOLO family. Its core philosophy is to be a **\"local-first\" application**. It runs entirely in your browser and uses the File System Access API to work directly with your local image and label folders. This means you never have to upload your data to a server, ensuring both privacy and speed.\n\nThe primary output of the tool is annotation files in the widely-used **YOLO text format (.txt)**, and it includes several convenience features for YOLO users, such as loading class names from `.yaml` files.",
                "Easy Labeling was created to streamline the often tedious process of building high-quality annotation datasets. Its core philosophy is to be a **local-first** application. The browser version uses the File System Access API to work directly with local folders, and the repository also documents a Windows Electron build for teams that prefer an installed app.\n\nThe current tool has two main workflows. **Detection** creates YOLO text labels at `label/<image>.txt`. **Segmentation** supports brush and eraser mask editing, then saves `mask/<image>.png` and `mask/<image>.seg.json`. Class names can be loaded from `.yaml` files.",
            )
            text = text.replace(
                "*   **Full YOLO Format Support:** Natively creates label files in the YOLO format and enhances workflow by loading class definitions from `.yaml` files.",
                "*   **Detection Workflow:** Creates YOLO bounding-box label files and loads class definitions from `.yaml` files.",
            )
            text = text.replace(
                "*   **Comprehensive Annotation Tools:**\n    *   Draw, edit, move, resize, and delete bounding boxes.\n    *   Switch between dedicated \"draw\" and \"edit\" modes for precision.\n    *   Fine-grained canvas control with zoom, pan, and direct coordinate input.",
                "*   **Detection and Segmentation Tools:**\n    *   Draw, edit, move, resize, copy, align, distribute, and delete bounding boxes in Detection.\n    *   Paint and erase masks, adjust brush size, move connected regions, and change region classes in Segmentation.\n    *   Use zoom, pan, crosshair, and preview navigation for detailed work.",
            )
            text = text.replace(
                "## Future Plans\n\nI plan to add more features, including **data augmentation** capabilities and support for other annotation formats. I'll be sharing development progress and technical challenges right here on this blog.\n\nIf you're interested in the project, please check out the [GitHub repository](https://github.com/MouseBall54/easy_labeling). Your interest and feedback on this YOLO annotation tool are greatly appreciated!",
                "## Current Repository Status\n\nThe GitHub repository now documents Easy Labeling as a two-workflow local annotation tool: Detection for YOLO boxes and Segmentation for brush-based masks. Use Desktop Chrome or Edge for the browser version because local folder read/write depends on browser support, or inspect the Electron commands if a Windows app build fits your workflow.\n\nIf you're interested in the project, check the [GitHub repository](https://github.com/MouseBall54/easy_labeling) and compare the README with your dataset requirements before starting a large labeling batch.",
            )
        else:
            text = text.replace(
                "특히 **YOLO 포맷** 데이터셋 생성을 목표로 하는 분들께 유용한 도구가 될 것입니다.",
                "현재 저장소 기준으로는 **Detection**에서 YOLO bounding box를 만들고, **Segmentation**에서 브러시 기반 마스크를 편집할 수 있습니다.",
            )
            text = text.replace(
                "Easy Labeling은 객체 탐지(Object Detection) 모델, 특히 YOLO 계열 모델 학습에 필요한 데이터셋을 구축하는 과정을 간소화하기 위해 탄생했습니다. 가장 큰 특징은 **설치가 필요 없는 웹 기반**이라는 점과, 사용자의 **로컬 파일을 직접 처리**한다는 점입니다. File System Access API를 활용하여 이미지와 라벨 파일을 서버에 업로드하는 과정 없이 작업하므로, 민감한 데이터를 안전하게 다룰 수 있고 속도도 매우 빠릅니다.\n\n주요 출력 포맷은 **YOLO 텍스트 포맷(.txt)**이며, `.yaml` 파일을 통해 클래스 이름을 관리하는 등 YOLO 사용자를 위한 편의 기능을 다수 포함하고 있습니다.",
                "Easy Labeling은 컴퓨터 비전 데이터셋 주석 작업을 로컬에서 빠르게 처리하기 위해 만들었습니다. 브라우저 버전은 File System Access API로 로컬 폴더를 직접 읽고 쓰며, 저장소에는 Windows용 Electron 빌드 방법도 문서화되어 있습니다.\n\n현재 도구는 두 가지 주요 워크플로우를 제공합니다. **Detection**은 YOLO bounding box를 만들고 `label/<image>.txt`로 저장합니다. **Segmentation**은 브러시와 지우개로 마스크를 편집하고 `mask/<image>.png`, `mask/<image>.seg.json`을 저장합니다. 클래스 이름은 `.yaml` 파일로 관리할 수 있습니다.",
            )
            text = text.replace(
                "*   **YOLO 포맷 완벽 지원:** 라벨 파일을 YOLO 포맷으로 생성하고, `.yaml` 클래스 파일을 불러와 작업의 효율성을 높입니다.",
                "*   **Detection 워크플로우:** YOLO bounding box 라벨 파일을 생성하고 `.yaml` 클래스 파일을 불러와 작업합니다.",
            )
            text = text.replace(
                "*   **다양한 주석(Annotation) 도구:**\n    *   경계 상자(Bounding Box) 그리기, 편집, 이동, 크기 조정 및 삭제\n    *   정밀 작업을 위한 '그리기'와 '편집' 모드 전환\n    *   캔버스 확대/축소, 이동(Pan), 좌표 직접 입력",
                "*   **Detection과 Segmentation 도구:**\n    *   Detection에서 bounding box 그리기, 편집, 이동, 크기 조정, 복사, 정렬, 분배, 삭제를 지원합니다.\n    *   Segmentation에서 브러시와 지우개로 마스크를 편집하고, 연결 영역 이동과 클래스 변경을 지원합니다.\n    *   확대/축소, pan, crosshair, 미리보기 이동으로 세부 작업을 돕습니다.",
            )
            text = text.replace(
                "## 향후 계획\n\n앞으로 데이터 증강(Data Augmentation) 관련 기능과 다양한 주석 포맷 지원을 추가할 계획입니다. 개발 진행 상황과 기술적인 도전 과제들을 이 블로그를 통해 꾸준히 공유하겠습니다.\n\n프로젝트에 관심이 있으시다면 [GitHub 저장소](https://github.com/MouseBall54/easy_labeling)를 방문해주세요. 많은 관심과 피드백 부탁드립니다!",
                "## 현재 저장소 기준 상태\n\nGitHub 저장소 README는 Easy Labeling을 Detection과 Segmentation 두 워크플로우를 가진 로컬 주석 도구로 설명합니다. 브라우저 버전은 로컬 폴더 읽기/쓰기 지원 때문에 Desktop Chrome 또는 Edge 사용을 권장하고, Windows 앱이 필요한 경우 Electron 빌드 명령도 확인할 수 있습니다.\n\n프로젝트에 관심이 있으시다면 [GitHub 저장소](https://github.com/MouseBall54/easy_labeling)를 확인하고, 대량 라벨링 전에 README의 기능 범위와 데이터셋 요구사항을 먼저 비교해 보세요.",
            )
    if name == "2025-07-15-easy-labeling-in-depth-features.md":
        if lang == "en":
            text = text.replace(
                "Optimized especially for the YOLO format, Easy Labeling focuses on streamlining the user's workflow with a rich set of features that make the repetitive task of labeling faster, easier, and more accurate.",
                "The current repository documents Easy Labeling as a local annotation tool with two workflow tabs: Detection for YOLO bounding boxes and Segmentation for brush-based masks. This post focuses on the Detection-heavy productivity features, then notes where mask work follows a different flow.",
            )
            text = text.replace(
                "Easy Labeling is equipped with all the essential tools for precise and rapid annotation.",
                "Easy Labeling includes separate tools for box annotation and mask annotation.",
            )
            text = text.replace(
                "-   **Flexible Bounding Box Editing:** Intuitively draw bounding boxes with your mouse, resize them by dragging edges or corners, and easily move or delete them.\n-   **Precision Control:** Freely zoom in and out, pan across the image to examine details, and get real-time coordinate displays for high-precision work.\n-   **Drawing/Edit Mode Toggling:** Boost your efficiency by quickly switching between drawing and editing modes with the `Ctrl+Q` shortcut.",
                "-   **Detection Box Editing:** Draw, resize, move, delete, copy, paste, align, distribute, and change classes for YOLO boxes.\n-   **Segmentation Mask Editing:** Paint and erase masks, adjust brush size, move connected regions, and change the selected region class.\n-   **Precision Control:** Zoom, pan, use crosshair guidance, and switch draw/edit modes with `Ctrl+Q`.",
            )
        else:
            text = text.replace(
                "특히 YOLO 포맷에 최적화되어, 반복적인 라벨링 작업을 더 빠르고, 쉽고, 정확하게 만들 수 있도록 다양한 기능들을 제공합니다.",
                "현재 저장소 기준 Easy Labeling은 Detection과 Segmentation 두 워크플로우 탭을 제공합니다. 이 글은 Detection 중심 생산성 기능을 주로 설명하되, 마스크 작업은 다른 흐름으로 검수해야 한다는 점도 함께 반영합니다.",
            )
            text = text.replace(
                "Easy Labeling은 정밀하고 빠른 주석 작업을 위한 모든 필수 도구를 갖추고 있습니다.",
                "Easy Labeling은 박스 주석과 마스크 주석을 구분해 다룰 수 있는 도구를 제공합니다.",
            )
            text = text.replace(
                "-   **자유로운 경계 상자 편집:** 마우스로 경계 상자를 직관적으로 그리고, 모서리나 변을 드래그하여 크기를 조절하며, 쉽게 이동하거나 삭제할 수 있습니다.\n-   **정밀한 제어:** 이미지를 자유롭게 확대/축소하고, 이동(Pan)하여 세부 영역을 확인하며, 실시간 좌표 표시를 통해 정밀한 작업이 가능합니다.\n-   **그리기/편집 모드 전환:** `Ctrl+Q` 단축키로 그리기 모드와 편집 모드를 빠르게 전환하여 작업 효율을 높일 수 있습니다.",
                "-   **Detection 박스 편집:** YOLO 박스를 그리고, 크기 조정, 이동, 삭제, 복사, 붙여넣기, 정렬, 분배, 클래스 변경을 할 수 있습니다.\n-   **Segmentation 마스크 편집:** 브러시와 지우개로 마스크를 편집하고, 연결 영역을 옮기거나 선택 영역의 클래스를 바꿀 수 있습니다.\n-   **정밀한 제어:** 확대/축소, pan, crosshair, `Ctrl+Q` 그리기/편집 모드 전환으로 세부 영역을 확인합니다.",
            )
    if name == "2025-07-20-easy-labeling-guide-1.md":
        if lang == "en":
            text = text.replace("**Browser**: Chrome 93+, Firefox 91+, Edge 93+", "**Browser**: Desktop Chrome or Edge recommended because local folder read/write uses the File System Access API")
            text = text.replace(
                "Hello! Starting with this post, I will explain in detail how to use **Easy Labeling, a dedicated tool for YOLO data labeling**.",
                "Hello! Starting with this post, I will explain how to use **Easy Labeling**, a local annotation tool that currently supports Detection for YOLO boxes and Segmentation for brush-based masks.",
            )
            text = text.replace(
                "By modifying this file to create your own class list, you can work more intuitively as the specified names (person, car, etc.) will be displayed instead of class numbers during labeling. The feature to edit this file directly within Easy Labeling will be covered in detail in a future guide.",
                "By modifying this file to create your own class list, you can work more intuitively as the specified names (person, car, etc.) will be displayed instead of class numbers during labeling. The current repository also documents class-file selection and create/edit modals, so keep class YAML files versioned when multiple datasets share similar names.",
            )
            text = text.replace(
                "In this post, we have covered the most basic features of Easy Labeling: loading image and label files, and using class files.\n\nIn the next guide, we will provide a detailed explanation of **how to perform the actual labeling work**, so please look forward to it!\n\nIf you have any questions, feel free to ask in the comments.\n\nThank you.",
                "In this post, we covered the most basic setup: loading image folders, loading or creating the `label` folder for Detection, and using class files. If your project needs masks, use the Segmentation workflow separately and check that `mask/<image>.png` and `mask/<image>.seg.json` are created as expected.\n\nBefore a large batch, run one small pilot in Desktop Chrome or Edge and confirm that saves happen in the expected folder.",
            )
        else:
            text = text.replace("**브라우저**: Chrome 93+, Firefox 91+, Edge 93+", "**브라우저**: 로컬 폴더 읽기/쓰기에 File System Access API가 필요하므로 Desktop Chrome 또는 Edge 권장")
            text = text.replace(
                "안녕하세요! 이번 글부터 **YOLO 데이터 라벨링 전용 도구, Easy Labeling**의 사용법을 자세히 소개하려고 합니다.",
                "안녕하세요! 이번 글부터 **Easy Labeling** 사용법을 소개합니다. 현재 저장소 기준 Easy Labeling은 YOLO 박스를 다루는 Detection과 브러시 기반 마스크를 다루는 Segmentation을 함께 제공합니다.",
            )
            text = text.replace(
                "이 파일을 수정하여 자신만의 클래스 목록을 만들면, 라벨링 작업 시 숫자 대신 지정한 이름(예: person, car 등)으로 표시되어 훨씬 직관적으로 작업할 수 있습니다. 이 파일을 Easy Labeling 내에서 직접 편집하는 기능은 추후 가이드에서 자세히 다룰 예정입니다.",
                "이 파일을 수정하여 자신만의 클래스 목록을 만들면, 라벨링 작업 시 숫자 대신 지정한 이름(예: person, car 등)으로 표시되어 훨씬 직관적으로 작업할 수 있습니다. 현재 저장소에는 클래스 파일 선택과 생성/편집 모달도 문서화되어 있으므로, 여러 데이터셋이 비슷한 클래스 이름을 쓸 때는 YAML 파일을 버전으로 관리하는 편이 좋습니다.",
            )
            text = text.replace(
                "이번 글에서는 Easy Labeling의 가장 기본적인 기능인 이미지와 라벨 파일 불러오기, 클래스 파일 사용법을 알아보았습니다.\n\n다음 가이드에서는 **실제 라벨링 작업을 어떻게 수행하는지**에 대해 자세히 설명할 예정이니 기대해주세요!\n\n궁금한 점이 있다면 댓글로 남겨주세요.\n\n감사합니다.",
                "이번 글에서는 이미지 폴더를 열고, Detection용 `label` 폴더를 만들거나 불러오며, 클래스 파일을 사용하는 기본 흐름을 정리했습니다. 프로젝트가 마스크를 필요로 한다면 Segmentation 워크플로우를 별도로 열고 `mask/<image>.png`, `mask/<image>.seg.json` 저장 여부를 확인해야 합니다.\n\n대량 작업 전에는 Desktop Chrome 또는 Edge에서 작은 파일럿 배치를 실행하고 저장 폴더가 예상대로 만들어지는지 먼저 확인하세요.",
            )
    return text


def main() -> None:
    changed = []
    for post_dir in POST_DIRS:
        for path in sorted(post_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if not is_easy_labeling_post(text):
                continue
            lang = lang_of(text)
            original = text
            text = ensure_last_modified(text)
            text = revise_generated(text, lang)
            text = revise_early_posts(text, path, lang)
            text = ensure_source_note(text, lang)
            if text != original:
                path.write_text(text, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))
    print(f"Revised {len(changed)} Easy Labeling posts")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
