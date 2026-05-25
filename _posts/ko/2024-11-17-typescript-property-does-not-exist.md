---
typora-root-url: ../
layout: single
title: >
  TypeScript Property does not exist on type 오류 해결 방법
seo_title: >
  TypeScript Property does not exist on type 오류 해결 방법
date: 2024-11-17T07:12:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: typescript-property-does-not-exist
header:
   teaser: /images/2026-05-23-typescript-property-does-not-exist/typescript-property-does-not-exist-hero.png
   overlay_image: /images/2026-05-23-typescript-property-does-not-exist/typescript-property-does-not-exist-hero.png
   overlay_filter: 0.5
   image_description: >
     TypeScript Property does not exist on type 오류 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  TypeScript Property does not exist on type 오류를 object type, API response type, union narrowing, nullable DOM value, unsafe any cast 기준으로 해결하는 방법입니다.
seo_description: >
  TypeScript Property does not exist on type 오류를 object type, API response type, union narrowing, nullable DOM value, unsafe any cast 기준으로 해결하는 방법입니다.
categories:
  - ko_Troubleshooting
tags:
  - TypeScript
  - Types
  - Interface
  - JavaScript
---

## 문제 상황

TypeScript에서 다음과 같은 오류가 날 수 있습니다.

![TypeScript Property does not exist on type 오류 해결 방법 설명 이미지](/images/2026-05-23-typescript-property-does-not-exist/typescript-property-does-not-exist-hero.png)

```text
TS2339: Property 'email' does not exist on type 'User'.
```

또는 DOM 코드에서 아래처럼 표시될 수 있습니다.

```text
TS2339: Property 'value' does not exist on type 'HTMLElement'.
```

Runtime object에는 실제로 해당 property가 있을 수도 있습니다.
하지만 TypeScript는 선언된 type이 허용하는 property만 확인합니다.
해결하려면 실제 데이터 형태에 맞게 type을 고치거나, 접근 전에 값을 좁히거나, 더 구체적인 DOM/API type을 사용해야 합니다.

## 원인

이 오류는 보통 다음 상황에서 발생합니다.

- interface 또는 type에 property가 빠졌습니다.
- object type이 실제보다 너무 좁게 선언되었습니다.
- API response type이 실제 응답과 맞지 않습니다.
- union type을 좁히지 않고 특정 member의 property를 읽었습니다.
- DOM query 결과가 너무 넓은 type이거나 null일 수 있습니다.
- runtime data shape을 검증하지 않고 가정했습니다.

바로 `as any`를 추가하지 마세요.
먼저 그 property가 해당 type의 모든 값에 존재해야 하는지 판단해야 합니다.

## 빠른 해결

해당 property가 object에 항상 있어야 한다면 type을 수정합니다.

```ts
type User = {
  id: number;
  name: string;
  email: string;
};

const user: User = {
  id: 1,
  name: "Ada",
  email: "ada@example.com"
};

console.log(user.email);
```

일부 값에만 property가 있다면 읽기 전에 type을 좁힙니다.

```ts
type User = { id: number; name: string };
type UserWithEmail = User & { email: string };

function printEmail(user: User | UserWithEmail) {
  if ("email" in user) {
    console.log(user.email);
  }
}
```

## 단계별 해결 방법

### 1. Object Type 수정하기

모든 `User`에 `email`이 있다면 type도 그렇게 선언해야 합니다.

잘못된 예:

```ts
type User = {
  id: number;
  name: string;
};

function sendEmail(user: User) {
  console.log(user.email);
}
```

올바른 예:

```ts
type User = {
  id: number;
  name: string;
  email: string;
};
```

Property가 실제 model의 일부라면 이 방식이 가장 명확합니다.

### 2. Optional Property를 정확히 표시하기

Property가 없을 수 있다면 optional로 표시하고 그 경우를 처리합니다.

```ts
type User = {
  id: number;
  name: string;
  email?: string;
};

function sendEmail(user: User) {
  if (!user.email) {
    return;
  }

  console.log(user.email.toLowerCase());
}
```

데이터가 정말 없을 수 있을 때만 optional property를 사용하세요.
TypeScript 오류를 없애려고 모든 property를 optional로 만드는 것은 좋지 않습니다.

### 3. Union Type 좁히기

값이 여러 shape 중 하나라면, member-specific property를 읽기 전에 check가 필요합니다.

```ts
type Success = { ok: true; data: string };
type Failure = { ok: false; error: string };

function handle(result: Success | Failure) {
  if (result.ok) {
    console.log(result.data);
    return;
  }

  console.log(result.error);
}
```

특정 union member에만 있는 property라면 `in` operator를 사용할 수 있습니다.

```ts
type Admin = { id: number; role: "admin"; permissions: string[] };
type Guest = { id: number; role: "guest" };

function printPermissions(user: Admin | Guest) {
  if ("permissions" in user) {
    console.log(user.permissions.join(", "));
  }
}
```

### 4. API Response Type 수정하기

API 데이터에서 이 오류가 자주 발생합니다.

코드가 아래 응답을 기대한다면:

```json
{
  "id": 1,
  "name": "Ada",
  "email": "ada@example.com"
}
```

TypeScript type에도 `email`이 있어야 합니다.

```ts
type UserResponse = {
  id: number;
  name: string;
  email: string;
};
```

API가 `email`을 생략할 수 있다면 `email?: string`으로 두고 missing case를 처리합니다.
외부 API라면 type만 믿지 말고 runtime validation도 고려해야 합니다.

### 5. 구체적인 DOM Type 사용하기

DOM query는 넓은 type을 반환합니다.

아래 코드는 실패할 수 있습니다.

```ts
const input = document.querySelector("#email");
console.log(input.value);
```

`querySelector`는 `Element | null`을 반환할 수 있고, 모든 `Element`에 `value`가 있는 것은 아닙니다.

먼저 좁힙니다.

```ts
const input = document.querySelector("#email");

if (input instanceof HTMLInputElement) {
  console.log(input.value);
}
```

Markup을 직접 통제하는 경우 type assertion을 사용할 수 있습니다.

```ts
const input = document.getElementById("email") as HTMLInputElement | null;

if (input) {
  console.log(input.value);
}
```

그래도 null check는 유지해야 합니다.

### 6. as any를 기본 해결책으로 쓰지 않기

아래 코드는 compiler error를 없애지만 TypeScript의 유용한 검사를 함께 없앱니다.

```ts
console.log((user as any).email);
```

`any`는 정말 알 수 없는 경계에서만 제한적으로 쓰고, 이후 안전한 type으로 변환하는 것이 좋습니다.
Application code 내부에서는 올바른 interface, type guard, runtime validation을 우선 사용하세요.

## 해결 확인 방법

다음을 실행합니다.

```bash
npx tsc --noEmit
```

Project에 script가 있다면 함께 실행합니다.

```bash
npm run typecheck
npm test
npm run build
```

`TS2339`가 사라지고, 수정한 type이 실제 runtime data를 여전히 정확히 설명하면 해결된 것입니다.

## 흔한 실수

- 실제 object shape을 확인하기 전에 `as any`를 추가합니다.
- domain model상 필수인 property를 optional로 바꿉니다.
- Union type을 좁히지 않고 특정 member의 field를 읽습니다.
- `querySelector`가 항상 non-null `HTMLInputElement`를 반환한다고 가정합니다.
- 실제 API 응답이 아니라 기억으로 response type을 작성합니다.
- Runtime object와 compile-time type을 혼동합니다.

## 공식 문서

- [TypeScript narrowing documentation](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [TypeScript object types documentation](https://www.typescriptlang.org/docs/handbook/2/objects.html)

## 전문 보완 체크

**TypeScript Property does not exist on type 오류 해결 방법**에서 중요한 기준은 독자가 한 번 따라 해서 성공했는지가 아닙니다. 이 주제는 재현 가능한 디버깅 절차로 다루는 편이 안전합니다. 결론을 내리기 전에 브라우저 또는 Node 버전, 번들러 설정, 비동기 경계, DOM 또는 API 상태를 확인해야 합니다. 또한 나중에 같은 문제가 반복될 수 있으므로, 관찰한 사실과 사용한 가정, 결론이 바뀔 조건을 짧은 결정 기록으로 남기는 것이 좋습니다.

### 신뢰도를 높이는 증거

작업을 바꾸기 전에는 객관적인 증거를 먼저 확인해야 합니다. 쓸 만한 증거에는 콘솔 stack trace, `node --version`, Network 탭 출력, 최소 재현 예제가 포함됩니다. 증거가 서로 맞지 않으면 억지로 하나의 이야기로 합치지 말고 충돌 자체를 남겨야 합니다. 빠른 해결이 한 번 성공했더라도 같은 입력, 계정, 의존성, 기기 상태에서 다시 확인하지 않았다면 아직 확정된 해결책이라고 보기 어렵습니다.

### 검토 표

| 검토 항목 | 확인할 내용 | 중요한 이유 |
| --- | --- | --- |
| 범위 | 이 글이 다루는 정확한 사례 | 조언을 과도하게 적용하지 않게 합니다 |
| 기준 상태 | 변경 전 상태 | 되돌리기와 비교를 가능하게 합니다 |
| 변경 | 실제로 수행한 가장 작은 조치 | 숨은 부작용을 줄입니다 |
| 결과 | 변경 뒤 관찰한 출력 또는 반응 | 기대와 증거를 구분합니다 |
| 재확인 | 결론을 다시 볼 시점 | 글의 정확도를 유지합니다 |

### 예외 상황과 실패 모드

주요 위험은 증상만 고치고 원인을 남기는 상황, 서로 무관한 변경을 같은 테스트에 섞는 상황입니다. 생산 데이터, 개인정보, 돈, 건강, 법적 권리, 보안 복구가 관련되어 있다면 넓은 해결책을 바로 적용하기보다 먼저 증거를 모으는 보수적인 접근이 낫습니다. 같은 제목의 문제라도 환경이 다르면 원인이 달라질 수 있으므로, 독자는 명령이나 결정을 복사하기 전에 자신의 조건이 글의 가정과 맞는지 비교해야 합니다.

### 유지보수 기준

이 안내는 의존성, 운영체제, 빌드 도구가 바뀐 뒤 다시 확인해야 합니다. 좋은 업데이트는 글 전체를 다시 쓰는 것이 아니라 예시, 링크, 명령, 화면, 판단 기준이 현재 동작과 여전히 맞는지 확인하는 일입니다. 기존 결론이 유효하면 확인 날짜를 남기고, 바뀌었다면 무엇이 바뀌었고 왜 이전 조언만으로 부족한지 설명해야 합니다.

## 관련 글

- [JavaScript TypeError: Cannot Read Properties of Null 해결 방법](/ko_troubleshooting/javascript-typeerror-cannot-read-properties-of-null/)
- [JavaScript Uncaught TypeError: Cannot Read Properties of Undefined 해결 방법](/ko_troubleshooting/javascript-uncaught-typeerror-cannot-read-properties-of-undefined/)
- [JavaScript innerHTML과 textContent 차이](/ko_troubleshooting/javascript-innerhtml-vs-textcontent/)

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "TypeScript Property does not exist on type 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
