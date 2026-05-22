---
typora-root-url: ../
layout: single
title: >
  npm ERR! ERESOLVE 오류 해결 방법
seo_title: >
  npm ERR! ERESOLVE 오류 해결 방법
date: 2026-05-23T14:00:00+09:00
lang: ko
translation_id: javascript-npm-err-eresolve
header:
   teaser: /images/2026-05-23-javascript-npm-err-eresolve/javascript-npm-err-eresolve-hero.png
   overlay_image: /images/2026-05-23-javascript-npm-err-eresolve/javascript-npm-err-eresolve-hero.png
   overlay_filter: 0.5
excerpt: >
  npm ERR ERESOLVE 오류를 peer dependency 충돌 확인, 패키지 버전 정렬, lockfile 갱신, legacy-peer-deps 임시 사용 기준으로 해결하는 방법입니다.
seo_description: >
  npm ERR ERESOLVE 오류를 peer dependency 충돌 확인, 패키지 버전 정렬, lockfile 갱신, legacy-peer-deps 임시 사용 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - JavaScript
  - npm
  - Dependency
  - Nodejs
---

## 문제 상황

`npm install`을 실행했는데 npm이 다음과 같은 오류로 중단될 수 있습니다.

![npm ERR! ERESOLVE 오류 해결 방법 설명 이미지](/images/2026-05-23-javascript-npm-err-eresolve/javascript-npm-err-eresolve-hero.png)

```text
npm ERR! ERESOLVE unable to resolve dependency tree
```

아래와 같은 내용이 함께 보일 수도 있습니다.

```text
npm ERR! Found: react@18.2.0
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.0" from some-package
```

`npm ERR ERESOLVE`는 npm이 동시에 만족할 수 없는 dependency 요구사항을 발견했다는 뜻입니다.
React, Angular, Vite, ESLint, TypeScript, testing-library 같은 프로젝트에서 plugin과 framework 버전이 맞지 않을 때 자주 발생합니다.

## 원인

가장 흔한 원인은 peer dependency 충돌입니다.

예를 들어 어떤 패키지는 "React 17과 함께 동작한다"고 선언했는데, 현재 프로젝트는 React 18을 사용할 수 있습니다.
또 다른 패키지는 특정 TypeScript, ESLint, framework 버전을 요구할 수 있습니다.

다른 원인은 다음과 같습니다.

- lockfile이 다른 패키지 버전 기준으로 만들어졌습니다.
- `package.json`은 수정했지만 `package-lock.json`이 갱신되지 않았습니다.
- plugin이 현재 framework 버전에 비해 너무 오래되었습니다.
- npm 버전이 바뀌면서 peer dependency 검사가 더 엄격해졌습니다.
- 과거에 `--legacy-peer-deps`로 설치해서 충돌이 숨겨져 있었습니다.

가장 안전한 해결은 충돌하는 패키지를 찾고 버전을 맞추는 것입니다.

## 빠른 진단

먼저 다음 명령을 실행합니다.

```bash
node -v
npm -v
npm explain package-name
```

`package-name`은 오류 메시지에 나온 패키지 이름으로 바꿉니다.

npm이 peer dependency 문제를 말한다면 해당 패키지 정보를 확인합니다.

```bash
npm view package-name peerDependencies
npm view package-name version
```

이 명령으로 패키지가 요구하는 버전 범위를 확인할 수 있습니다.

## 단계별 해결 방법

### 1. 첫 번째 ERESOLVE 블록 읽기

마지막 줄만 검색하지 마세요.
보통 중요한 정보는 첫 번째 `Found:`와 `Could not resolve dependency:` 블록 근처에 있습니다.

확인할 내용은 다음과 같습니다.

- 현재 설치된 패키지
- 다른 버전을 요구하는 패키지
- peer dependency 범위

예시:

```text
Found: react@18.2.0
Could not resolve dependency:
peer react@"^17.0.0" from old-component-library
```

이는 `old-component-library`가 React 18 호환성을 선언하지 않았다는 뜻입니다.

### 2. 패키지 버전 맞추기

아래 중 하나를 선택합니다.

- 오래된 peer dependency를 가진 패키지를 업그레이드합니다.
- 프로젝트가 특정 framework 버전에 머물러야 한다면 framework 버전을 낮춥니다.
- 호환되지 않는 패키지를 교체합니다.
- framework major version과 맞는 패키지 버전을 사용합니다.

예시:

```bash
npm install old-component-library@latest
```

또는 호환되는 특정 버전을 설치합니다.

```bash
npm install old-component-library@2.4.0
```

버전을 바꾼 뒤 다시 실행합니다.

```bash
npm install
```

### 3. node_modules와 package-lock.json 갱신

버전을 맞췄는데도 npm이 계속 실패한다면 설치 상태를 새로 만듭니다.

macOS와 Linux:

```bash
rm -rf node_modules package-lock.json
npm install
```

Windows PowerShell:

```powershell
Remove-Item -Recurse -Force node_modules
Remove-Item -Force package-lock.json
npm install
```

`node_modules` 정리와 lockfile 재생성은 함께 다루는 것이 좋습니다.
dependency tree가 왜 바뀌었는지 이해하지 않은 채 lockfile만 반복해서 삭제하지 마세요.

### 4. npm 버전 차이 확인

npm 버전에 따라 peer dependency 처리 방식이 다를 수 있습니다.

확인합니다.

```bash
npm -v
```

팀이나 CI와 함께 쓰는 프로젝트라면 모든 환경에서 같은 Node/npm 버전을 사용해야 합니다.
프로젝트에 `.nvmrc`, `packageManager`, Volta 설정, CI Node 설정이 있다면 그 버전을 따르세요.

### 5. --legacy-peer-deps는 임시 우회로만 사용

다음과 같은 조언을 볼 수 있습니다.

```bash
npm install --legacy-peer-deps
```

이 옵션은 아래 상황에서 임시로 유용할 수 있습니다.

- 오래된 프로젝트를 빨리 복구해야 합니다.
- dependency migration을 단계적으로 진행 중입니다.
- 실제 런타임에서는 동작하지만 패키지의 peer dependency metadata가 오래되었습니다.

하지만 이 옵션은 충돌을 숨깁니다.
패키지들이 실제로 호환되지 않는다면 build나 runtime에서 앱이 실패할 수 있습니다.

임시 우회로 사용하되, 이후 실제 dependency 업데이트 계획을 세우는 것이 좋습니다.

### 6. --force를 기본 해결책으로 쓰지 않기

`npm install --force`는 더 공격적인 옵션입니다.
npm에게 잠재적으로 깨진 dependency tree를 받아들이라고 지시합니다.

위험을 이해하고, 테스트나 build 단계로 문제를 잡을 수 있을 때만 사용하세요.

일반적인 프로젝트 유지보수에서는 버전 정렬이 더 좋은 해결책입니다.

## 해결 확인 방법

dependency tree를 고친 뒤 다음을 실행합니다.

```bash
npm install
npm ls
npm run build
```

테스트가 있다면 함께 실행합니다.

```bash
npm test
```

프론트엔드 프로젝트라면 dev server도 확인합니다.

```bash
npm run dev
```

`npm install`만 통과했다고 해결이 끝난 것은 아닙니다.
해결된 버전 조합으로 앱이 build되고 실행되어야 합니다.

## 흔한 실수

- 충돌 내용을 읽지 않고 `npm install --legacy-peer-deps`부터 실행합니다.
- `node_modules`는 삭제했지만 오래된 lockfile은 그대로 둡니다.
- `package-lock.json`을 삭제하고 재생성한 파일을 commit하지 않습니다.
- 같은 프로젝트에서 npm, yarn, pnpm lockfile을 섞어 사용합니다.
- React, Angular, Vite, ESLint, TypeScript를 올리면서 관련 plugin은 그대로 둡니다.
- 모든 패키지의 최신 버전이 항상 서로 호환된다고 가정합니다.

## 관련 글

- [JavaScript Failed to Fetch 오류 해결 방법](/ko_Troubleshooting/javascript-failed-to-fetch/)
- [JavaScript var, let, const 차이 정리](/ko_Troubleshooting/javascript-variables-var-vs-let-vs-const/)
- [JavaScript Promise.all과 Promise.race 차이](/ko_Troubleshooting/javascript-promise-all-vs-promise-race/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "npm ERR! ERESOLVE 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
