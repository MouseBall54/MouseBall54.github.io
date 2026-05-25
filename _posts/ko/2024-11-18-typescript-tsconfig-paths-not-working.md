---
typora-root-url: ../
layout: single
title: >
  tsconfig paths가 동작하지 않을 때 해결 방법
seo_title: >
  tsconfig paths가 동작하지 않을 때 해결 방법
date: 2024-11-18T07:13:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: typescript-tsconfig-paths-not-working
header:
   teaser: /images/2026-05-23-typescript-tsconfig-paths-not-working/typescript-tsconfig-paths-not-working-hero.png
   overlay_image: /images/2026-05-23-typescript-tsconfig-paths-not-working/typescript-tsconfig-paths-not-working-hero.png
   overlay_filter: 0.5
   image_description: >
     tsconfig paths가 동작하지 않을 때 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  tsconfig paths가 동작하지 않을 때 baseUrl, paths pattern, 실제 tsconfig, Vite alias, test runner alias, Node runtime resolution을 확인하는 방법입니다.
seo_description: >
  tsconfig paths가 동작하지 않을 때 baseUrl, paths pattern, 실제 tsconfig, Vite alias, test runner alias, Node runtime resolution을 확인하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - TypeScript
  - tsconfig
  - Vite
  - Nodejs
---

## 문제 상황

`tsconfig.json`에 path alias를 설정했는데 import가 계속 실패할 수 있습니다.

![tsconfig paths가 동작하지 않을 때 해결 방법 설명 이미지](/images/2026-05-23-typescript-tsconfig-paths-not-working/typescript-tsconfig-paths-not-working-hero.png)

```ts
import Button from "@/components/Button";
```

Editor에서는 정상처럼 보이지만 app 실행이 실패할 수 있고, 반대로 app은 실행되는데 `tsc`만 실패할 수도 있습니다.
TypeScript, bundler, test runner, Node runtime이 하나의 alias 설정을 자동으로 공유하지 않기 때문입니다.

## 원인

`tsconfig` paths는 여러 이유로 동작하지 않을 수 있습니다.

- `baseUrl` 또는 `paths`가 없거나 잘못 작성되었습니다.
- Alias pattern이 실제 import와 맞지 않습니다.
- Framework가 `tsconfig.app.json` 같은 다른 config를 사용합니다.
- Vite, Webpack, Jest, Vitest, Node에 같은 alias가 설정되지 않았습니다.
- Compile된 JavaScript를 Node에서 실행하지만 Node는 TypeScript path alias를 모릅니다.
- 파일 이동 후 alias가 잘못된 폴더를 가리킵니다.

핵심 규칙은 간단합니다.
TypeScript `paths`는 TypeScript가 type과 import를 이해하도록 돕지만, 그 자체로 emitted import path를 바꾸지는 않습니다.

## 빠른 해결

먼저 최소한의 `tsconfig.json` alias를 확인합니다.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

그다음 bundler 설정도 맞춥니다.
Vite 예시:

```ts
import { defineConfig } from "vite";
import path from "node:path";

export default defineConfig({
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  }
});
```

Config를 바꾼 뒤에는 dev server와 editor의 TypeScript server를 다시 시작합니다.

## 단계별 해결 방법

### 1. Alias Pattern 확인하기

`paths`의 key와 value는 import 문과 맞아야 합니다.

아래 import를 사용한다면:

```ts
import Button from "@/components/Button";
```

다음처럼 설정합니다.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

`@/` import를 쓰는데 아래처럼 작성하면 맞지 않습니다.

```json
{
  "paths": {
    "@": ["src"]
  }
}
```

이 설정은 `import x from "@"`만 match하고 `@/components/Button`에는 맞지 않습니다.

### 2. 실제 tsconfig 파일 확인하기

많은 프로젝트에는 TypeScript config가 여러 개 있습니다.

- `tsconfig.json`
- `tsconfig.app.json`
- `tsconfig.node.json`
- `tsconfig.spec.json`
- `tsconfig.test.json`

App source가 `tsconfig.app.json`으로 compile된다면 `tsconfig.json`에만 `paths`를 추가해도 현재 파일에 적용되지 않을 수 있습니다.

최종 config를 확인합니다.

```bash
npx tsc --noEmit --showConfig
```

출력에 alias가 없다면 source file을 실제로 포함하는 config에 넣거나, 여러 config가 extend하는 shared base config로 옮깁니다.

### 3. Vite 또는 Bundler 설정하기

TypeScript는 alias를 이해하지만 Vite는 모를 수 있습니다.
`vite.config.ts`에 같은 alias를 추가합니다.

```ts
import { defineConfig } from "vite";
import path from "node:path";

export default defineConfig({
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  }
});
```

최근 Vite에는 `resolve.tsconfigPaths` option도 있습니다.
이 option을 사용한다면 현재 Vite version이 해당 option을 지원하는지, 그리고 active `tsconfig.json`에 alias가 있는지 확인해야 합니다.

다른 bundler를 사용한다면 `tsconfig`만 믿지 말고 해당 bundler의 alias 설정을 추가해야 합니다.

### 4. Test 설정 따로 확인하기

Test runner는 별도 alias mapping이 필요할 수 있습니다.

Vitest는 보통 Vite config를 읽지만 프로젝트 설정에 따라 다를 수 있습니다.
Test만 실패한다면 `vitest.config.ts`를 확인하세요.

Jest는 보통 `moduleNameMapper`가 필요합니다.

```js
module.exports = {
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1"
  }
};
```

`tsc`와 app은 통과하는데 test만 실패한다면 TypeScript alias가 아니라 test runner resolver 문제일 가능성이 큽니다.

### 5. Node Runtime 처리하기

Node는 기본적으로 `tsconfig.json`의 paths를 읽지 않습니다.
Script, CLI, server code, compile된 JavaScript를 직접 실행할 때 중요합니다.

선택지는 다음과 같습니다.

- Runtime Node script에서는 relative import를 사용합니다.
- 실행 전에 bundling합니다.
- `ts-node`와 함께 `tsconfig-paths` 같은 runtime helper를 사용합니다.
- Framework의 server build tool이 alias를 resolve하도록 설정합니다.

`npx tsc --noEmit`은 통과하지만 `node dist/index.js`가 실패한다면 emitted JavaScript import path를 확인하세요.
출력 파일에 여전히 `@/`가 남아 있다면 Node는 추가 설정 없이 resolve하지 못합니다.

### 6. Cache된 도구 다시 시작하기

Config를 바꾼 뒤 아래 도구를 재시작합니다.

- Vite dev server
- test watcher
- VS Code TypeScript server
- ESLint server

`tsconfig` 변경 후 editor diagnostic이 오래 남는 경우가 흔합니다.
Editor만 믿지 말고 terminal command로 확인해야 합니다.

## 해결 확인 방법

다음을 실행합니다.

```bash
npx tsc --noEmit
npm run build
```

Test가 있다면 실행합니다.

```bash
npm test
```

Vite app이라면 dev server도 확인합니다.

```bash
npm run dev
```

TypeScript, bundler, 그리고 실패했던 runtime 또는 test command가 모두 alias를 resolve해야 해결된 것입니다.

## 흔한 실수

- `paths`가 JavaScript import를 자동으로 rewrite한다고 기대합니다.
- `"@/..."` import를 쓰면서 `"@": ["src"]`만 설정합니다.
- Framework가 `tsconfig.app.json`을 쓰는데 `tsconfig.json`만 수정합니다.
- Vite는 설정했지만 Jest 같은 test runner 설정을 빠뜨립니다.
- Compile된 JavaScript를 Node에서 실행하면서 unresolved `@/` import를 남깁니다.
- Config 변경 후 dev server를 재시작하지 않습니다.

## 공식 문서

- [TypeScript TSConfig paths option](https://www.typescriptlang.org/tsconfig/paths.html)
- [Vite resolve.alias option](https://vite.dev/config/shared-options/#resolve-alias)

## 전문 보완 체크

**tsconfig paths가 동작하지 않을 때 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 실행 환경, 정확한 오류 경계, 최소 재현 예제, 되돌릴 수 있는 경로를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 전체 명령 출력, 버전 번호, 변경된 파일, 기대 동작과 실제 동작가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

## 관련 글

- [JavaScript jQuery is not defined 오류 해결 방법](/ko_troubleshooting/javascript-jquery-is-not-defined/)
- [JavaScript var, let, const 차이 정리](/ko_troubleshooting/javascript-variables-var-vs-let-vs-const/)
- [JavaScript TypeError: '...' is not a function 해결 방법](/ko_troubleshooting/javascript-typeerror-is-not-a-function/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "tsconfig paths가 동작하지 않을 때 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
