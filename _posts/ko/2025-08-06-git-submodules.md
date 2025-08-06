---
typora-root-url: ../
layout: single
title: >
   Git 서브모듈(Submodule)로 프로젝트 의존성 관리하기

lang: ko
translation_id: git-submodules
header:
   teaser: /images/header_images/overlay_image_git.png
   overlay_image: /images/header_images/overlay_image_git.png
   overlay_filter: 0.5
excerpt: >
    `git submodule`을 사용하여 외부 저장소를 메인 프로젝트의 하위 디렉터리로 포함하고 관리하는 방법을 알아보세요.
categories:
  - ko_Troubleshooting
tags:
  - Git
  - Submodule
  - Dependency
  - Repository
---

## Git 서브모듈이란?

Git 서브모듈을 사용하면 Git 저장소를 다른 Git 저장소의 하위 디렉터리로 유지할 수 있습니다. 이는 별도로 개발 및 유지 관리되는 외부 라이브러리나 다른 구성 요소에 대한 의존성을 포함하고 관리하는 좋은 방법입니다.

서브모듈은 특정 커밋에 고정된 별도의 Git 저장소입니다. 종종 "슈퍼프로젝트"라고 불리는 메인 저장소는 해당 커밋에 대한 참조를 저장합니다.

## 문제 상황

타사 라이브러리를 사용하는 프로젝트에서 작업하고 있습니다. 라이브러리의 소스 코드를 프로젝트에 직접 포함하고 싶지만, 새 버전이 출시될 때 라이브러리를 쉽게 업데이트할 수도 있기를 원합니다.

라이브러리 코드를 저장소에 복사할 수도 있지만, 그렇게 하면 업데이트가 수동적이고 오류가 발생하기 쉬운 프로세스가 됩니다.

## 해결 방법

### 1. 서브모듈 추가하기

새 서브모듈을 추가하려면 `git submodule add` 명령을 사용합니다. 저장소의 URL과 배치할 경로가 필요합니다.

```bash
git submodule add https://github.com/example/library.git external/library
```

이 명령은 두 가지 작업을 수행합니다.
1.  `library` 저장소를 `external/library` 디렉터리로 복제합니다.
2.  루트 디렉터리에 `.gitmodules` 파일을 생성(또는 업데이트)합니다. 이 파일은 서브모듈 경로를 URL에 매핑합니다.
3.  새 서브모듈 디렉터리와 `.gitmodules` 파일을 스테이징합니다.

이제 슈퍼프로젝트에 변경 사항을 커밋합니다.
```bash
git commit -m "Add the library submodule"
```

### 2. 서브모듈이 있는 프로젝트 복제하기

다른 사람이 프로젝트를 복제하면 서브모듈 디렉터리가 생성되지만 비어 있습니다.

서브모듈의 내용을 초기화하고 복제하려면 다음을 실행해야 합니다.
```bash
git submodule init
git submodule update
```

또는 `--recurse-submodules` 플래그를 사용하여 슈퍼프로젝트를 복제하여 한 단계로 수행할 수 있습니다.
```bash
git clone --recurse-submodules https://github.com/your/project.git
```

### 3. 서브모듈 업데이트하기

시간이 지남에 따라 사용 중인 라이브러리가 업데이트됩니다. 최신 변경 사항을 서브모듈로 가져오려면:

1.  서브모듈 디렉터리로 이동합니다.
    ```bash
    cd external/library
    ```
2.  최신 변경 사항을 가져오고 원하는 브랜치(예: `main`)를 체크아웃합니다.
    ```bash
    git fetch
    git checkout main
    git pull
    ```
3.  슈퍼프로젝트의 루트 디렉터리로 돌아갑니다.
    ```bash
    cd ../..
    ```
4.  `external/library`에 새로운 변경 사항이 있음을 알 수 있습니다. 슈퍼프로젝트에서 이 업데이트를 스테이징하고 커밋합니다.
    ```bash
    git add external/library
    git commit -m "Update library to the latest version"
    ```

이렇게 하면 슈퍼프로젝트의 포인터가 서브모듈의 새 커밋으로 업데이트됩니다. 다른 협업자는 `git submodule update --remote`를 실행하여 이 업데이트를 받을 수 있습니다.

## 서브모듈 제거하기

서브모듈 제거는 여러 단계의 프로세스입니다.
1.  서브모듈 초기화 해제: `git submodule deinit -f external/library`
2.  `.gitmodules`에서 서브모듈 항목 제거 및 인덱스에서 디렉터리 제거: `git rm -f external/library`
3.  `.git` 디렉터리에서 서브모듈 디렉터리 제거: `rm -rf .git/modules/external/library`
4.  변경 사항을 커밋합니다.

## 결론

Git 서브모듈은 외부 Git 저장소에 대한 의존성을 관리하는 강력한 방법입니다. 외부 코드를 별도로 유지하면서 프로젝트에 깔끔하게 통합할 수 있습니다. 때때로 작업하기 까다로울 수 있지만, 버전 관리되는 다른 구성 요소에 의존하는 프로젝트에는 매우 유용합니다.
