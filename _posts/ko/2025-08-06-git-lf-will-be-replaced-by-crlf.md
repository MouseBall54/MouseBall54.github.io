---
typora-root-url: ../
layout: single
title: >
   Git 경고 해결: "LF will be replaced by CRLF"
date: 2025-08-06T10:40:00+09:00
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    크로스 플랫폼 프로젝트를 위한 줄 바꿈 정규화를 구성하여 Git의 "LF will be replaced by CRLF" 경고를 이해하고 해결하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Line Endings
  - CRLF
  - LF
  - Windows
  - macOS
  - Linux
---

## 경고 이해하기

`warning: LF will be replaced by CRLF in <filename>` 경고는 운영 체제가 텍스트 파일의 줄 바꿈을 처리하는 방식의 차이 때문에 나타납니다.

-   **Windows**는 두 개의 문자 시퀀스인 캐리지 리턴(CR)과 라인 피드(LF)를 사용합니다. 이를 **CRLF**라고 합니다.
-   **macOS 및 Linux**는 단일 문자인 라인 피드(LF)를 사용합니다.

Git에는 이를 관리하기 위한 `core.autocrlf` 구성 설정이 있습니다. 이 경고는 Git이 운영 체제(이 경우 Windows)의 표준과 일치하도록 LF 줄 바꿈을 CRLF로 자동 변환하려고 함을 의미합니다.

## 문제 상황

Windows에서 파일을 스테이징할 때 macOS 또는 Linux 시스템에서 생성된 모든 파일에 대해 이 경고가 표시됩니다. 이는 작업 중단을 유발하지는 않는 경고일 뿐이지만 성가시고 콘솔 출력을 복잡하게 만들 수 있습니다.

더 중요한 것은 일관되지 않은 줄 바꿈은 올바르게 처리되지 않으면 일부 스크립트, 도구 또는 diff에 문제를 일으킬 수 있다는 것입니다.

## 해결 방법: `core.autocrlf` 구성하기

이를 처리하는 가장 좋은 방법은 Git의 `core.autocrlf` 설정을 구성하는 것입니다. 이는 Git에게 줄 바꿈을 자동으로 처리하는 방법을 알려줍니다.

### Windows 사용자용 (권장)

파일을 체크아웃할 때 LF를 CRLF로 변환하고 커밋할 때 CRLF를 다시 LF로 변환하도록 Git을 구성합니다. 이렇게 하면 저장소는 LF 엔딩(대부분의 프로젝트 표준)으로 파일을 저장하지만 Windows 기본 CRLF 엔딩을 사용하여 작업할 수 있습니다.

```bash
git config --global core.autocrlf true
```

이 설정을 사용하면 Git이 자동으로 변환을 수행하고 경고가 사라집니다.

### macOS 및 Linux 사용자용 (권장)

커밋 시에만 CRLF를 LF로 변환하고 그 반대는 변환하지 않도록 Git을 구성합니다. 이렇게 하면 Windows 사용자의 파일을 작업하게 될 경우 실수로 CRLF 엔딩으로 파일을 커밋하는 것을 방지할 수 있습니다.

```bash
git config --global core.autocrlf input
```

### 프로젝트 전체 구성

팀의 모든 사람이 동일한 줄 바꿈 구성을 사용하도록 하려면 저장소의 루트에 `.gitattributes` 파일을 추가할 수 있습니다.

`.gitattributes`라는 파일을 만들고 다음 줄을 추가합니다.

```gitattributes
# core.autocrlf가 설정되지 않은 경우를 대비한 기본 동작 설정
* text=auto

# 항상 정규화하려는 텍스트 파일을 명시적으로 선언
*.txt text
*.html text
*.css text
*.js text

# 체크아웃 시 항상 CRLF 줄 바꿈을 갖는 파일 선언
*.sln text eol=crlf

# 체크아웃 시 항상 LF 줄 바꿈을 갖는 파일 선언
*.sh text eol=lf

# 실제로 바이너리이며 수정해서는 안 되는 모든 파일 표시
*.png binary
*.jpg binary
```

-   `* text=auto`: 이것이 주요 설정입니다. Git에게 텍스트로 간주하는 모든 파일에 대해 줄 바꿈을 자동으로 처리하도록 지시합니다.
-   `eol=crlf` 또는 `eol=lf`: 특정 파일 유형에 대해 특정 줄 바꿈을 강제할 수 있습니다.
-   `binary`: Git에게 바이너리 파일의 줄 바꿈을 건드리지 않도록 지시합니다.

`.gitattributes` 파일을 저장소에 커밋하면 개인 Git 구성에 관계없이 모든 협업자에게 일관된 동작이 보장됩니다.

## 결론

"LF will be replaced by CRLF" 경고는 Git이 여러 운영 체제에서 줄 바꿈을 관리하는 데 도움을 주고 있음을 알려주는 방법입니다. `core.autocrlf`를 올바르게 설정하거나 `.gitattributes` 파일을 사용하여 이 경고를 해결하고 프로젝트에 모든 사람에게 일관된 줄 바꿈이 있도록 할 수 있습니다.
