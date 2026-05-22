# P0 Content Queue

This queue converts the weekly 100k traffic master plan into publishable paired posts. Each item requires a Korean and English post with matching `translation_id`.

Status values:

- `todo`: not started
- `draft`: content exists but not verified
- `review`: ready for quality pass
- `published`: merged and deployed
- `refresh`: existing post should be updated instead of duplicated

## Python

| Status | Translation ID | Primary keyword | Korean title direction | English title direction |
| --- | --- | --- | --- | --- |
| review | python-pip-install-failed | pip install failed | Python `pip install` 실패 해결 | How to Fix pip install Failed in Python |
| review | python-no-module-named-pip | No module named pip | `No module named pip` 해결 | How to Fix No module named pip |
| review | python-venv-not-activating | python venv not activating | Python 가상환경이 활성화되지 않을 때 | Python venv Not Activating |
| review | python-command-not-found-windows | python command not found windows | Windows에서 `python` 명령어가 안 될 때 | Python Command Not Found on Windows |
| review | python-externally-managed-environment | externally-managed-environment | `externally-managed-environment` 해결 | Fix externally-managed-environment in Python |
| todo | python-vscode-interpreter-not-showing | VS Code Python interpreter not showing | VS Code Python interpreter 선택 문제 | VS Code Python Interpreter Not Showing |
| todo | python-pytorch-cuda-install-error | PyTorch CUDA install error | PyTorch CUDA 설치 오류 해결 | Fix PyTorch CUDA Installation Errors |
| todo | python-fastapi-422 | FastAPI 422 | FastAPI `422 Unprocessable Entity` 해결 | Fix FastAPI 422 Unprocessable Entity |
| todo | python-pydantic-validationerror | Pydantic ValidationError | Pydantic validation error 읽는 법 | How to Read Pydantic ValidationError |
| todo | python-uv-package-manager | uv python package manager | `uv` 설치와 기존 pip 차이 | uv vs pip for Python Projects |

## JavaScript and TypeScript

| Status | Translation ID | Primary keyword | Korean title direction | English title direction |
| --- | --- | --- | --- | --- |
| review | javascript-npm-err-eresolve | npm ERR ERESOLVE | `npm ERR! ERESOLVE` 해결 | How to Fix npm ERR ERESOLVE |
| review | node-cannot-find-module | Cannot find module node | `Cannot find module` 해결 | Fix Cannot Find Module in Node.js |
| review | typescript-cannot-find-name | TypeScript Cannot find name | TypeScript `Cannot find name` 해결 | Fix TypeScript Cannot Find Name |
| review | typescript-property-does-not-exist | Property does not exist on type | `Property does not exist on type` 해결 | Fix Property Does Not Exist on Type |
| review | typescript-tsconfig-paths-not-working | tsconfig paths not working | `tsconfig` paths가 동작하지 않을 때 | tsconfig Paths Not Working |
| todo | vite-dev-server-not-starting | Vite dev server not starting | Vite dev server가 뜨지 않을 때 | Vite Dev Server Not Starting |
| todo | react-useeffect-infinite-loop | React useEffect infinite loop | React `useEffect` 무한 반복 해결 | Fix React useEffect Infinite Loop |
| todo | nextjs-hydration-error | Next.js hydration error | Next.js hydration error 해결 | Fix Next.js Hydration Error |
| todo | pnpm-lockfile-error | pnpm lockfile error | pnpm lockfile 오류 해결 | Fix pnpm Lockfile Errors |
| todo | cors-preflight-error | CORS preflight error | CORS preflight 오류 해결 | Fix CORS Preflight Error |

## Git and GitHub

| Status | Translation ID | Primary keyword | Korean title direction | English title direction |
| --- | --- | --- | --- | --- |
| todo | github-actions-build-failed | GitHub Actions build failed | GitHub Actions build failed 해결 | How to Fix GitHub Actions Build Failed |
| todo | github-pages-jekyll-build-failed | GitHub Pages Jekyll build failed | GitHub Pages Jekyll build 실패 | Fix GitHub Pages Jekyll Build Failed |
| todo | git-fatal-authentication-failed | git fatal authentication failed | `fatal: authentication failed` 해결 | Fix Git fatal authentication failed |
| todo | git-gh006-protected-branch | GH006 protected branch | `GH006 protected branch hook declined` 해결 | Fix GH006 Protected Branch Hook Declined |
| todo | git-rebase-conflict | git rebase conflict | rebase conflict 안전하게 해결 | How to Resolve Git Rebase Conflicts |
| todo | git-non-fast-forward | git non-fast-forward | `non-fast-forward` push rejected 해결 | Fix Git Non-Fast-Forward Push Rejected |
| todo | git-lfs-quota-exceeded | Git LFS quota exceeded | Git LFS quota exceeded 해결 | Fix Git LFS Quota Exceeded |
| todo | github-token-permission | GitHub token permission | GitHub token permission 오류 | Fix GitHub Token Permission Errors |
| todo | git-safe-directory | git safe.directory | `safe.directory` 오류 해결 | Fix Git safe.directory Error |
| refresh | gitignore-not-working | gitignore not working | `.gitignore`가 적용되지 않을 때 | Gitignore Not Working |

## Java and Spring Boot

| Status | Translation ID | Primary keyword | Korean title direction | English title direction |
| --- | --- | --- | --- | --- |
| todo | spring-boot-port-8080-already-in-use | Spring Boot port 8080 already in use | Spring Boot port 8080 already in use 해결 | Fix Spring Boot Port 8080 Already in Use |
| todo | gradle-build-failed | Gradle build failed | Gradle build failed 해결 | How to Fix Gradle Build Failed |
| todo | maven-dependency-not-found | Maven dependency not found | Maven dependency not found 해결 | Fix Maven Dependency Not Found |
| todo | java-unsupported-class-file-major-version | unsupported class file major version | Unsupported class file major version 해결 | Fix Unsupported Class File Major Version |
| todo | lombok-not-working-intellij | Lombok not working IntelliJ | Lombok이 IDE에서 동작하지 않을 때 | Lombok Not Working in IntelliJ |
| todo | spring-boot-bean-could-not-be-found | Spring Boot bean could not be found | Spring Boot bean could not be found 해결 | Fix Spring Boot Bean Could Not Be Found |
| todo | jpa-lazyinitializationexception | LazyInitializationException | JPA lazy initialization exception 해결 | Fix LazyInitializationException in JPA |
| todo | intellij-cannot-resolve-symbol | IntelliJ cannot resolve symbol | `Cannot resolve symbol` 해결 | Fix Cannot Resolve Symbol in IntelliJ |
| todo | java-heap-space | Java heap space | Java heap space와 GC 로그 확인 | Fix Java Heap Space Error |
| todo | spring-boot-connection-refused | Spring Boot connection refused | `Connection refused` in Spring Boot | Fix Spring Boot Connection Refused |

## Easy Labeling and Computer Vision

| Status | Translation ID | Primary keyword | Korean title direction | English title direction |
| --- | --- | --- | --- | --- |
| todo | yolo-label-format | YOLO label format | YOLO label format 읽는 법 | How to Read YOLO Label Format |
| todo | coco-to-yolo-conversion | COCO to YOLO | COCO to YOLO 변환 실수 | COCO to YOLO Conversion Mistakes |
| todo | image-labeling-classes | image labeling classes | 이미지 라벨링 클래스 관리법 | How to Manage Classes for Image Labeling |
| todo | local-image-labeling-workflow | local image labeling | 로컬 이미지 라벨링 워크플로우 | Local Image Labeling Workflow |
| todo | easy-labeling-yolo-dataset | Easy Labeling YOLO | Easy Labeling으로 YOLO 데이터셋 만들기 | Build a YOLO Dataset with Easy Labeling |
