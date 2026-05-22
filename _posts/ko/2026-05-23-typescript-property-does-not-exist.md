---
typora-root-url: ../
layout: single
title: >
  TypeScript Property does not exist on type 오류 해결 방법
seo_title: >
  TypeScript Property does not exist on type 오류 해결 방법
date: 2026-05-23T17:00:00+09:00
lang: ko
translation_id: typescript-property-does-not-exist
header:
   teaser: /images/2026-05-23-typescript-property-does-not-exist/typescript-property-does-not-exist-hero.png
   overlay_image: /images/2026-05-23-typescript-property-does-not-exist/typescript-property-does-not-exist-hero.png
   overlay_filter: 0.5
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

## 관련 글

- [JavaScript TypeError: Cannot Read Properties of Null 해결 방법](/ko_Troubleshooting/javascript-typeerror-cannot-read-properties-of-null/)
- [JavaScript Uncaught TypeError: Cannot Read Properties of Undefined 해결 방법](/ko_Troubleshooting/javascript-uncaught-typeerror-cannot-read-properties-of-undefined/)
- [JavaScript innerHTML과 textContent 차이](/ko_Troubleshooting/javascript-innerhtml-vs-textcontent/)
