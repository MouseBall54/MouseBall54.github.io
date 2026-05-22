---
typora-root-url: ../
layout: single
title: >
  Fix TypeScript Cannot Find Name
seo_title: >
  Fix TypeScript Cannot Find Name
date: 2026-05-23T16:00:00+09:00
lang: en
translation_id: typescript-cannot-find-name
header:
   teaser: /images/header_images/overlay_image_js.png
   overlay_image: /images/header_images/overlay_image_js.png
   overlay_filter: 0.5
excerpt: >
  Fix TS2304 Cannot find name in TypeScript by checking imports, type packages, tsconfig lib and types settings, globals, and the correct project config.
seo_description: >
  Fix TS2304 Cannot find name in TypeScript by checking imports, type packages, tsconfig lib and types settings, globals, and the correct project config.
categories:
  - en_Troubleshooting
tags:
  - TypeScript
  - JavaScript
  - tsconfig
  - Types
---

## Problem

TypeScript shows an error like this:

```text
TS2304: Cannot find name 'process'.
```

or:

```text
TS2304: Cannot find name 'describe'.
```

The same code may still run in Node.js, a browser, Jest, Vitest, or another runtime.
That is what makes this error confusing.
`Cannot find name` means the TypeScript compiler cannot see a variable, function, type, or global name at compile time.

The fix is not always to create a new variable.
Often the correct fix is to add an import, install the right type package, or adjust `tsconfig.json`.

## Cause

Common causes include:

- A missing import.
- A typo in a variable, function, type, or interface name.
- A package is installed but its type definitions are missing.
- Node globals such as `process`, `Buffer`, or `__dirname` are used without Node types.
- Test globals such as `describe`, `it`, or `expect` are used without test framework types.
- Browser globals such as `document` or `window` are unavailable because `DOM` is missing from `lib`.
- The file is checked by a different `tsconfig.json` than the one you edited.
- The `types` option is present and excludes the global type package you expected.

Start with the exact name in the error message.
The fix for `process` is different from the fix for `User`, `document`, or `describe`.

## Quick Fix

If the missing name is your own function, class, type, or value, import it:

```ts
import { createUser } from "./create-user";
```

If the missing name is a Node global, install Node type definitions:

```bash
npm install -D @types/node
```

Then make sure your `tsconfig.json` allows Node types:

```json
{
  "compilerOptions": {
    "types": ["node"]
  }
}
```

If the project already has a `types` array, add `node` to the existing array instead of replacing everything.

## Step-by-Step Fix

### 1. Check for a Missing Import

If the error points to a name from another file, TypeScript needs an import.

Wrong:

```ts
const user = createUser("Ada");
```

Right:

```ts
import { createUser } from "./create-user";

const user = createUser("Ada");
```

Do the same for types:

```ts
import type { User } from "./types";

function printUser(user: User) {
  console.log(user.name);
}
```

If your editor suggests an auto-import, still check that it imported from the intended file.

### 2. Check for a Typo or Scope Problem

TypeScript is case-sensitive.

```ts
const userName = "Ada";

console.log(username);
```

`userName` and `username` are different names.

Also check scope:

```ts
if (ready) {
  const token = "abc";
}

console.log(token);
```

`token` only exists inside the `if` block.
Move the declaration to the scope where it is needed, or pass the value explicitly.

### 3. Fix Node Globals

If the missing name is `process`, `Buffer`, `__dirname`, or `require`, the project probably needs Node types.

Install:

```bash
npm install -D @types/node
```

If `tsconfig.json` does not specify `types`, TypeScript normally includes visible `@types` packages automatically.
But if `types` is set, only the packages listed there are added to the global scope.

Example:

```json
{
  "compilerOptions": {
    "types": ["node"]
  }
}
```

For a mixed project, include all required globals:

```json
{
  "compilerOptions": {
    "types": ["node", "vitest/globals"]
  }
}
```

### 4. Fix Test Globals

If `describe`, `it`, `test`, or `expect` cannot be found, install or enable the test framework types.

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

Vitest with globals:

```json
{
  "compilerOptions": {
    "types": ["vitest/globals"]
  }
}
```

Another safe option is to import the test functions explicitly:

```ts
import { describe, expect, it } from "vitest";
```

This keeps globals out of the whole project.

### 5. Fix Browser Globals

If `document`, `window`, `HTMLElement`, or `Event` cannot be found, check the `lib` setting.

For browser code, include `DOM`:

```json
{
  "compilerOptions": {
    "lib": ["ES2022", "DOM"]
  }
}
```

For Node-only code, you may intentionally omit `DOM`.
Do not add browser globals to server code unless the runtime really provides them.

### 6. Check the Right tsconfig File

Frameworks often use more than one config file:

- `tsconfig.json`
- `tsconfig.app.json`
- `tsconfig.node.json`
- `tsconfig.spec.json`
- `tsconfig.test.json`

If you edited `tsconfig.json` but the error comes from test files, the active config may be `tsconfig.spec.json` or `tsconfig.test.json`.

Run:

```bash
npx tsc --noEmit --showConfig
```

This prints the resolved compiler configuration.
If your expected `types`, `lib`, or `include` setting is missing, edit the config that actually owns the file.

### 7. Avoid Hiding the Error

These are usually not real fixes:

```ts
// @ts-ignore
unknownName();
```

```ts
declare const unknownName: any;
```

Use them only when you are intentionally integrating a runtime global that TypeScript cannot know about yet.
For normal app code, import the name or add the correct type definition.

## How to Verify

Run the TypeScript compiler without emitting files:

```bash
npx tsc --noEmit
```

If the project has a dedicated typecheck script, use it:

```bash
npm run typecheck
```

Also run the relevant app or test command:

```bash
npm test
npm run build
```

The fix is complete when `TS2304: Cannot find name` is gone for the intended symbol and no new config-wide type errors were introduced.

## Common Mistakes

- Installing `@types/node` but forgetting that the `types` array excludes it.
- Adding `DOM` types to a Node-only project without checking runtime behavior.
- Editing `tsconfig.json` while the file is compiled by `tsconfig.app.json` or `tsconfig.spec.json`.
- Using `// @ts-ignore` instead of importing the missing name.
- Adding `any` to make the error disappear.
- Assuming editor auto-imports always choose the correct source file.

## Official References

- [TypeScript TSConfig types option](https://www.typescriptlang.org/tsconfig/types)
- [TypeScript TSConfig lib option](https://www.typescriptlang.org/tsconfig/#lib)
- [TypeScript compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

## Related Posts

- [How to Fix 'Uncaught ReferenceError: is not defined' in JavaScript](/en_Troubleshooting/javascript-uncaught-referenceerror-is-not-defined/)
- [JavaScript var vs let vs const: What's the Difference?](/en_Troubleshooting/javascript-variables-var-vs-let-vs-const/)
- [innerHTML vs textContent in JavaScript](/en_Troubleshooting/javascript-innerhtml-vs-textcontent/)
