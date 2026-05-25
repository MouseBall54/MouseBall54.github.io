---
typora-root-url: ../
layout: single
title: >
  Node.js Cannot find module 오류 해결 방법
seo_title: >
  Node.js Cannot find module 오류 해결 방법
date: 2024-11-09T07:49:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: node-cannot-find-module
header:
   teaser: /images/2026-05-23-node-cannot-find-module/node-cannot-find-module-hero.png
   overlay_image: /images/2026-05-23-node-cannot-find-module/node-cannot-find-module-hero.png
   overlay_filter: 0.5
   image_description: >
     Node.js Cannot find module 오류 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Node.js Cannot find module 오류를 패키지 설치, 상대 경로, 실행 위치, CommonJS와 ESM 문법, package exports 기준으로 해결하는 방법입니다.
seo_description: >
  Node.js Cannot find module 오류를 패키지 설치, 상대 경로, 실행 위치, CommonJS와 ESM 문법, package exports 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - Nodejs
  - npm
  - Modules
---

## 문제 상황

Node.js 스크립트를 실행했는데 다음과 같은 오류가 날 수 있습니다.

![Node.js Cannot find module 오류 해결 방법 설명 이미지](/images/2026-05-23-node-cannot-find-module/node-cannot-find-module-hero.png)

```text
Error: Cannot find module 'package-name'
```

또는 아래처럼 local file path가 표시될 수 있습니다.

```text
Error: Cannot find module './utils/file'
```

이 오류는 Node가 `require()` 또는 `import`에 전달된 값을 실제 package, file, export path로 찾지 못했다는 뜻입니다.
가장 중요한 단서는 따옴표 안에 있는 module 이름입니다.
이 값이 package 설치 문제인지, local file path 문제인지, module 형식 문제인지 판단해야 합니다.

## 원인

`Cannot find module`은 보통 다음 원인 중 하나로 발생합니다.

- 현재 프로젝트에 package가 설치되어 있지 않습니다.
- `node_modules`가 삭제되었거나 다른 폴더에 설치되어 있습니다.
- 명령을 잘못된 working directory에서 실행했습니다.
- local import path에 `./`, `../`, 정확한 file name이 빠졌습니다.
- CommonJS와 ESM 문법을 잘못 섞었습니다.
- package의 `package.json`에서 `exports` 필드로 deep import를 막고 있습니다.
- Windows에서는 통과한 대소문자 차이가 Linux 또는 CI에서 실패합니다.

Node는 package name과 file path를 다르게 해석합니다.
먼저 import 대상이 package인지 local file인지 분류해야 합니다.

## 빠른 해결

빠진 값이 `express`, `react`, `lodash` 같은 package name이라면 프로젝트에 설치합니다.

```bash
npm install package-name
npm ls package-name
```

빠진 값이 `./`, `../`, `/`로 시작한다면 file path입니다.
이 경우 package를 설치하지 말고 실제 파일 이름과 상대 위치를 확인합니다.

Node가 어느 위치에서 실행 중인지 확인합니다.

```bash
node -p "process.cwd()"
```

현재 위치가 project root가 아니라면 `package.json`이 있는 폴더로 이동한 뒤 다시 실행합니다.

## 단계별 해결 방법

### 1. Package인지 File인지 먼저 구분하기

아래는 package import입니다.

```js
const express = require("express");
```

아래는 local file import입니다.

```js
const helper = require("./utils/helper.js");
```

Package import라면 Node는 현재 module 주변의 `node_modules`부터 parent directory 방향으로 package를 찾습니다.
Local file import라면 import하는 파일을 기준으로 상대 경로를 따라갑니다.

`npm install utils/helper` 같은 명령을 실행하지 마세요.
경로가 local file이라면 설치가 아니라 path 수정이 필요합니다.

### 2. 빠진 Package 다시 설치하기

Package import라면 다음을 실행합니다.

```bash
npm install package-name
npm ls package-name
```

`npm ls`가 `(empty)` 또는 오류를 보여주면 이 프로젝트에 해당 package가 설치되지 않은 것입니다.

Lockfile이 있는 프로젝트라면 repo에서 이미 쓰는 package manager를 따르는 것이 좋습니다.

```bash
npm install
```

Yarn 또는 pnpm 프로젝트라면 lockfile을 섞지 말고 해당 명령을 사용합니다.

```bash
yarn install
pnpm install
```

### 3. Working Directory 확인하기

많은 `Cannot find module` 오류는 명령을 잘못된 폴더에서 실행해서 발생합니다.

macOS와 Linux:

```bash
pwd
node -p "process.cwd()"
ls package.json
```

Windows PowerShell:

```powershell
Get-Location
node -p "process.cwd()"
Get-ChildItem package.json
```

현재 폴더에 `package.json`이 없다면 project root로 이동합니다.

```bash
cd path/to/project
npm install
node app.js
```

### 4. Relative Path 수정하기

Local file에서 가장 흔한 실수는 `./`를 빠뜨리는 것입니다.

잘못된 예:

```js
const helper = require("utils/helper");
```

올바른 예:

```js
const helper = require("./utils/helper.js");
```

`utils/helper`는 package name처럼 해석됩니다.
`./utils/helper.js`는 현재 module 기준의 local file을 읽으라는 뜻입니다.

파일 이름의 대소문자도 확인해야 합니다.

```js
require("./UserService.js");
```

실제 파일 이름이 `userService.js`라면 Windows에서는 동작할 수 있지만 Linux CI나 production server에서는 실패할 수 있습니다.

### 5. CommonJS와 ESM 규칙 확인하기

CommonJS는 `require()`를 사용합니다.

```js
const helper = require("./helper.js");
```

ESM은 `import`를 사용합니다.

```js
import helper from "./helper.js";
```

`package.json`에 `"type": "module"`이 있으면 `.js` 파일은 기본적으로 ESM으로 처리됩니다.
ESM에서 local import를 할 때는 file extension을 포함하는 편이 안전합니다.

```js
import { formatName } from "./format-name.js";
```

ESM 프로젝트에서 CommonJS 파일이 필요하면 `.cjs`를 사용합니다.

```js
const config = require("./config.cjs");
```

CommonJS 프로젝트에서 ESM 파일이 필요하면 `.mjs`를 사용하거나 프로젝트 전체 전환을 의도적으로 진행합니다.
오류 하나를 없애기 위해 `"type": "module"`만 바꾸면 다른 import가 연쇄적으로 깨질 수 있습니다.

### 6. Package Export Path 확인하기

어떤 package는 아래 import만 허용할 수 있습니다.

```js
import thing from "some-package";
```

하지만 아래 deep import는 막을 수 있습니다.

```js
import thing from "some-package/internal/file";
```

최근 package들은 `exports` 필드로 외부에서 접근 가능한 public path를 제한할 수 있습니다.
Deep import가 실패한다면 package 문서를 확인하고 지원되는 public path로 import해야 합니다.

Package를 업그레이드한 뒤 예전 internal path가 사라져 이 오류가 나는 경우도 많습니다.

### 7. require.resolve로 진단하기

CommonJS 환경에서는 Node가 package를 어디서 읽는지 직접 확인할 수 있습니다.

```bash
node -p "require.resolve('package-name')"
```

Node가 찾지 못하면 이 명령도 `MODULE_NOT_FOUND` 오류를 냅니다.
이 경우 application logic 문제가 아니라 module resolution 문제라는 점을 확인할 수 있습니다.

Local path도 같은 방식으로 테스트할 수 있습니다.

```bash
node -p "require.resolve('./utils/helper.js')"
```

처음 오류가 난 명령과 같은 폴더, 같은 실행 방식에서 테스트해야 합니다.

## 해결 확인 방법

수정 후 처음 실패했던 명령을 그대로 다시 실행합니다.

```bash
node app.js
```

프로젝트에 script가 있다면 함께 확인합니다.

```bash
npm test
npm run build
npm start
```

같은 import에 대해 더 이상 `Cannot find module`이 발생하지 않으면 해결된 것입니다.
다른 오류가 난다면 이제 module resolution 다음 단계의 문제를 별도로 보면 됩니다.

## 흔한 실수

- 실제로는 relative path 문제인데 package를 설치합니다.
- project root가 아닌 parent folder에서 `node app.js`를 실행합니다.
- 한 repo에서 `npm install`, `yarn install`, `pnpm install`을 섞어 사용합니다.
- local file import에 `./`를 빠뜨립니다.
- ESM local import에서 `.js` 확장자를 생략합니다.
- 문서화된 public export가 아닌 package 내부 경로를 import합니다.
- Linux에서만 실패하는 파일 이름 대소문자 차이를 놓칩니다.

## 공식 문서

- [Node.js CommonJS modules documentation](https://nodejs.org/api/modules.html)
- [Node.js ECMAScript modules documentation](https://nodejs.org/api/esm.html)

## 전문 보완 체크

**Node.js Cannot find module 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 콘솔 stack trace, `node --version`, Network 탭 출력, 최소 재현 예제가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

## 관련 글

- [JavaScript 오류 'Uncaught ReferenceError: is not defined' 해결 방법](/ko_troubleshooting/javascript-uncaught-referenceerror-is-not-defined/)
- [JavaScript TypeError: '...' is not a function 해결 방법](/ko_troubleshooting/javascript-typeerror-is-not-a-function/)
- [JavaScript jQuery is not defined 오류 해결 방법](/ko_troubleshooting/javascript-jquery-is-not-defined/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Node.js Cannot find module 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
