---
typora-root-url: ../
layout: single
title: >
  TypeScript Cannot find name 오류 해결 방법
seo_title: >
  TypeScript Cannot find name 오류 해결 방법
date: 2026-05-23T16:00:00+09:00
lang: ko
translation_id: typescript-cannot-find-name
header:
   teaser: /images/2026-05-23-typescript-cannot-find-name/typescript-cannot-find-name-hero.png
   overlay_image: /images/2026-05-23-typescript-cannot-find-name/typescript-cannot-find-name-hero.png
   overlay_filter: 0.5
excerpt: >
  TypeScript TS2304 Cannot find name 오류를 import, type package, tsconfig lib와 types 설정, global name, 실제 config 기준으로 해결하는 방법입니다.
seo_description: >
  TypeScript TS2304 Cannot find name 오류를 import, type package, tsconfig lib와 types 설정, global name, 실제 config 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - TypeScript
  - JavaScript
  - tsconfig
  - Types
---

## 문제 상황

TypeScript에서 다음과 같은 오류가 표시될 수 있습니다.

![TypeScript Cannot find name 오류 해결 방법 설명 이미지](/images/2026-05-23-typescript-cannot-find-name/typescript-cannot-find-name-hero.png)

```text
TS2304: Cannot find name 'process'.
```

또는 아래처럼 test global이 잡히지 않을 수 있습니다.

```text
TS2304: Cannot find name 'describe'.
```

같은 코드가 Node.js, browser, Jest, Vitest 같은 runtime에서는 실행될 수도 있습니다.
그래서 이 오류가 헷갈립니다.
`Cannot find name`은 TypeScript compiler가 compile time에 변수, 함수, type, global name을 볼 수 없다는 뜻입니다.

해결책이 항상 새 변수를 만드는 것은 아닙니다.
대부분은 import를 추가하거나, 올바른 type package를 설치하거나, `tsconfig.json` 설정을 바로잡아야 합니다.

## 원인

주요 원인은 다음과 같습니다.

- 필요한 import가 빠졌습니다.
- 변수, 함수, type, interface 이름에 오타가 있습니다.
- package는 설치했지만 type definition이 없습니다.
- `process`, `Buffer`, `__dirname` 같은 Node global을 Node type 없이 사용했습니다.
- `describe`, `it`, `expect` 같은 test global을 test framework type 없이 사용했습니다.
- `document`, `window` 같은 browser global을 쓰는데 `lib`에 `DOM`이 없습니다.
- 수정한 `tsconfig.json`이 실제로 해당 파일을 검사하는 config가 아닙니다.
- `types` option이 있고, 기대한 global type package가 그 목록에서 빠져 있습니다.

오류 메시지에 나온 정확한 이름부터 봐야 합니다.
`process`, `User`, `document`, `describe`의 해결 방법은 서로 다릅니다.

## 빠른 해결

빠진 이름이 직접 만든 함수, class, type, value라면 import를 추가합니다.

```ts
import { createUser } from "./create-user";
```

빠진 이름이 Node global이라면 Node type definition을 설치합니다.

```bash
npm install -D @types/node
```

그리고 `tsconfig.json`에서 Node type을 허용하는지 확인합니다.

```json
{
  "compilerOptions": {
    "types": ["node"]
  }
}
```

이미 `types` 배열이 있다면 전체를 바꾸지 말고 기존 배열에 `node`를 추가합니다.

## 단계별 해결 방법

### 1. 빠진 Import 확인하기

오류가 다른 파일에서 가져와야 하는 이름을 가리킨다면 TypeScript에는 import가 필요합니다.

잘못된 예:

```ts
const user = createUser("Ada");
```

올바른 예:

```ts
import { createUser } from "./create-user";

const user = createUser("Ada");
```

Type도 마찬가지입니다.

```ts
import type { User } from "./types";

function printUser(user: User) {
  console.log(user.name);
}
```

Editor가 auto-import를 제안하더라도 의도한 파일에서 가져왔는지 확인해야 합니다.

### 2. 오타와 Scope 문제 확인하기

TypeScript는 대소문자를 구분합니다.

```ts
const userName = "Ada";

console.log(username);
```

`userName`과 `username`은 다른 이름입니다.

Scope도 확인합니다.

```ts
if (ready) {
  const token = "abc";
}

console.log(token);
```

`token`은 `if` block 안에서만 존재합니다.
필요한 위치에서 사용할 수 있도록 선언 위치를 옮기거나 값을 명시적으로 전달해야 합니다.

### 3. Node Global 해결하기

빠진 이름이 `process`, `Buffer`, `__dirname`, `require`라면 Node type이 필요할 가능성이 큽니다.

설치합니다.

```bash
npm install -D @types/node
```

`tsconfig.json`에 `types`가 없다면 TypeScript는 보통 보이는 `@types` package를 자동으로 포함합니다.
하지만 `types`가 설정되어 있으면 그 목록에 있는 package만 global scope에 추가됩니다.

예시:

```json
{
  "compilerOptions": {
    "types": ["node"]
  }
}
```

여러 global이 필요한 프로젝트라면 모두 포함합니다.

```json
{
  "compilerOptions": {
    "types": ["node", "vitest/globals"]
  }
}
```

### 4. Test Global 해결하기

`describe`, `it`, `test`, `expect`를 찾지 못한다면 test framework type을 설치하거나 활성화해야 합니다.

Jest:

```bash
npm install -D @types/jest
```

```json
{
  "compilerOptions": {
    "types": ["jest"]
  }
}
```

Vitest globals:

```json
{
  "compilerOptions": {
    "types": ["vitest/globals"]
  }
}
```

또 다른 안전한 방법은 test function을 명시적으로 import하는 것입니다.

```ts
import { describe, expect, it } from "vitest";
```

이 방식은 project 전체에 global을 늘리지 않습니다.

### 5. Browser Global 해결하기

`document`, `window`, `HTMLElement`, `Event`를 찾지 못한다면 `lib` 설정을 확인합니다.

Browser code라면 `DOM`을 포함합니다.

```json
{
  "compilerOptions": {
    "lib": ["ES2022", "DOM"]
  }
}
```

Node-only code라면 `DOM`을 일부러 제외했을 수 있습니다.
Runtime이 실제로 browser API를 제공하지 않는다면 server code에 browser global type을 추가하지 않는 것이 좋습니다.

### 6. 실제 tsconfig 파일 확인하기

Framework 프로젝트는 config 파일이 여러 개일 수 있습니다.

- `tsconfig.json`
- `tsconfig.app.json`
- `tsconfig.node.json`
- `tsconfig.spec.json`
- `tsconfig.test.json`

`tsconfig.json`을 수정했지만 오류가 test file에서 난다면 실제 config는 `tsconfig.spec.json` 또는 `tsconfig.test.json`일 수 있습니다.

다음 명령으로 최종 compiler 설정을 확인합니다.

```bash
npx tsc --noEmit --showConfig
```

기대한 `types`, `lib`, `include` 설정이 없다면 해당 파일을 실제로 포함하는 config를 수정해야 합니다.

### 7. 오류를 숨기지 않기

아래 코드는 대부분 실제 해결책이 아닙니다.

```ts
// @ts-ignore
unknownName();
```

```ts
declare const unknownName: any;
```

Runtime global을 의도적으로 연결하는 상황이 아니라면 이런 방식은 피하는 것이 좋습니다.
일반적인 app code에서는 빠진 이름을 import하거나 올바른 type definition을 추가해야 합니다.

## 해결 확인 방법

파일을 생성하지 않고 TypeScript compiler만 실행합니다.

```bash
npx tsc --noEmit
```

Project에 typecheck script가 있다면 그 명령을 사용합니다.

```bash
npm run typecheck
```

관련 app 또는 test 명령도 함께 확인합니다.

```bash
npm test
npm run build
```

대상 symbol에 대한 `TS2304: Cannot find name`이 사라지고, 설정 변경으로 새로운 type error가 대량으로 생기지 않아야 해결된 것입니다.

## 흔한 실수

- `@types/node`를 설치했지만 `types` 배열에서 `node`를 빠뜨립니다.
- Runtime 확인 없이 Node-only 프로젝트에 `DOM` type을 추가합니다.
- 실제로는 `tsconfig.app.json`이나 `tsconfig.spec.json`이 쓰이는데 `tsconfig.json`만 수정합니다.
- 빠진 import 대신 `// @ts-ignore`를 사용합니다.
- 오류를 없애기 위해 `any`를 추가합니다.
- Editor auto-import가 항상 올바른 파일을 고른다고 가정합니다.

## 공식 문서

- [TypeScript TSConfig types option](https://www.typescriptlang.org/tsconfig/types)
- [TypeScript TSConfig lib option](https://www.typescriptlang.org/tsconfig/#lib)
- [TypeScript compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

## 관련 글

- [JavaScript 오류 'Uncaught ReferenceError: is not defined' 해결 방법](/ko_Troubleshooting/javascript-uncaught-referenceerror-is-not-defined/)
- [JavaScript var, let, const 차이 정리](/ko_Troubleshooting/javascript-variables-var-vs-let-vs-const/)
- [JavaScript innerHTML과 textContent 차이](/ko_Troubleshooting/javascript-innerhtml-vs-textcontent/)
