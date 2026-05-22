# P0 Content Briefs

These briefs are the first writing sprint from `planning/p0-content-queue.md`. Each brief must become a Korean and English post with the same `translation_id`.

## Brief 1: pip install failed

- Translation ID: `python-pip-install-failed`
- Primary keyword: `pip install failed`
- Search intent: The reader tried `pip install ...` and needs a fast diagnosis path.
- Korean title: `Python pip install 실패 해결 방법`
- English title: `How to Fix pip install Failed in Python`
- Header image: `/images/header_images/overlay_image_python.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `Python`, `pip`, `PackageInstall`, `VirtualEnvironment`

Required sections:

1. Problem: show common outputs such as `ERROR: Could not find a version that satisfies the requirement`, `Failed building wheel`, and permission errors.
2. Cause: separate package name typo, unsupported Python version, stale pip, virtual environment mismatch, network/proxy, and OS build dependency issues.
3. Quick fix: upgrade pip, confirm active Python, install inside venv.
4. Windows commands:
   ```powershell
   py -m pip --version
   py -m pip install --upgrade pip setuptools wheel
   py -m pip install package-name
   ```
5. macOS/Linux commands:
   ```bash
   python3 -m pip --version
   python3 -m pip install --upgrade pip setuptools wheel
   python3 -m pip install package-name
   ```
6. Verification: import the package and check `python -m pip show package-name`.
7. Common mistakes: using `pip` from another interpreter, installing globally while running venv Python, copying smart quotes from a blog.

Internal links to add:

- `_posts/en/2025-07-30-python-modulenotfounderror.md`
- `_posts/en/2025-07-23-python-modulenotfounderror-no-module-named.md`
- `_posts/en/2025-08-05-python-permissionerror-errno-13-permission-denied.md`

Ad notes:

- Eligible for normal in-article ads because the topic is long-form and task-oriented.
- Do not place ads between a command and its explanation.

## Brief 2: No module named pip

- Translation ID: `python-no-module-named-pip`
- Primary keyword: `No module named pip`
- Search intent: Python exists, but `python -m pip` fails.
- Korean title: `Python No module named pip 오류 해결 방법`
- English title: `How to Fix No module named pip`
- Header image: `/images/header_images/overlay_image_python.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `Python`, `pip`, `ensurepip`, `Environment`

Required sections:

1. Problem: include `No module named pip` and explain why plain `pip` can be misleading.
2. Cause: pip was not installed, Python installation is incomplete, virtual environment was created without pip, or PATH points to a different Python.
3. Quick fix with `ensurepip`.
4. Commands:
   ```bash
   python -m ensurepip --upgrade
   python -m pip install --upgrade pip
   python -m pip --version
   ```
5. Windows fallback:
   ```powershell
   py -m ensurepip --upgrade
   py -m pip install --upgrade pip
   ```
6. Verification: `python -m pip --version` points to the expected Python directory.
7. Prevention: always use `python -m pip` in posts.

Internal links to add:

- `_posts/en/2025-07-30-python-modulenotfounderror.md`
- `_posts/en/2025-08-05-python-notadirectoryerror-errno-20-not-a-directory.md`
- `_posts/en/2025-08-05-python-permissionerror-errno-13-permission-denied.md`

Ad notes:

- Shorter than Brief 1, so include only one in-article ad after the first substantial troubleshooting section.

## Brief 3: Python venv not activating

- Translation ID: `python-venv-not-activating`
- Primary keyword: `python venv not activating`
- Search intent: The reader created a venv but the shell prompt or interpreter did not change.
- Korean title: `Python venv가 활성화되지 않을 때 해결 방법`
- English title: `Python venv Not Activating: How to Fix It`
- Header image: `/images/header_images/overlay_image_python.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `Python`, `venv`, `PowerShell`, `VirtualEnvironment`

Required sections:

1. Problem: explain expected prompt changes and why prompt changes are not the only proof.
2. Cause: wrong activation script, PowerShell execution policy, wrong terminal, deleted venv, or IDE interpreter mismatch.
3. Activation commands by shell:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   ```cmd
   .venv\Scripts\activate.bat
   ```
   ```bash
   source .venv/bin/activate
   ```
4. PowerShell policy fix:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
5. Verification:
   ```bash
   python -c "import sys; print(sys.executable)"
   ```
6. Common mistakes: activating from the wrong directory, using VS Code before selecting interpreter, mixing Conda and venv.

Internal links to add:

- `_posts/en/2025-08-05-python-permissionerror-errno-13-permission-denied.md`
- `_posts/en/2025-07-30-python-modulenotfounderror.md`
- `_posts/en/2025-08-05-python-systemerror-returned-null-without-setting-error.md`

Ad notes:

- Place ad after shell-specific commands, not between Windows and macOS/Linux command blocks.

## Brief 4: Python command not found on Windows

- Translation ID: `python-command-not-found-windows`
- Primary keyword: `python command not found windows`
- Search intent: The reader installed Python or expects it to exist, but terminal commands fail.
- Korean title: `Windows에서 python 명령어가 안 될 때 해결 방법`
- English title: `Python Command Not Found on Windows: How to Fix It`
- Header image: `/images/header_images/overlay_image_python.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `Python`, `Windows`, `PATH`, `py`

Required sections:

1. Problem: include `python is not recognized`, Microsoft Store alias behavior, and `py` launcher.
2. Cause: PATH missing, App Execution Alias conflict, terminal not restarted, multiple Python installs.
3. Quick fix: try `py --version` first.
4. Commands:
   ```powershell
   py --version
   py -0p
   where python
   where py
   ```
5. PATH fix: describe adding Python and Scripts directories through Windows settings.
6. Verification:
   ```powershell
   py -m pip --version
   python --version
   ```
7. Common mistakes: editing system PATH without reopening terminal, installing from Store unintentionally, using `pip` before confirming interpreter.

Internal links to add:

- `_posts/en/2025-07-30-python-modulenotfounderror.md`
- `_posts/en/2025-08-05-python-permissionerror-errno-13-permission-denied.md`
- `_posts/en/2025-08-05-python-timeouterror-winerror-10060.md`

Ad notes:

- Strong Windows beginner query. Keep the first screen ad-free until the `py --version` quick check is shown.

## Brief 5: externally-managed-environment

- Translation ID: `python-externally-managed-environment`
- Primary keyword: `externally-managed-environment`
- Search intent: The reader hit pip's externally managed environment protection on Linux/macOS package-managed Python.
- Korean title: `Python externally-managed-environment 오류 해결 방법`
- English title: `How to Fix externally-managed-environment in Python`
- Header image: `/images/header_images/overlay_image_python.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `Python`, `pip`, `venv`, `Linux`

Required sections:

1. Problem: quote the error name and explain it appears when pip protects system-managed Python.
2. Cause: distro or package manager owns the Python environment.
3. Quick fix: create a project venv and install there.
4. Commands:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install package-name
   ```
5. Alternatives: use `pipx` for CLI tools; use package manager for system packages.
6. Warning: mention `--break-system-packages` only as a last resort and explain risk.
7. Verification: `which python`, `python -m pip --version`, and package import.

Internal links to add:

- `_posts/en/2025-07-30-python-modulenotfounderror.md`
- `_posts/en/2025-08-05-python-permissionerror-errno-13-permission-denied.md`
- `_posts/en/2025-08-05-python-notadirectoryerror-errno-20-not-a-directory.md`

Ad notes:

- Avoid placing ads immediately before the warning about system packages.

## Brief 6: npm ERR ERESOLVE

- Translation ID: `javascript-npm-err-eresolve`
- Primary keyword: `npm ERR ERESOLVE`
- Search intent: npm install failed because dependency versions conflict.
- Korean title: `npm ERR! ERESOLVE 오류 해결 방법`
- English title: `How to Fix npm ERR ERESOLVE`
- Header image: `/images/header_images/overlay_image_js.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `JavaScript`, `npm`, `Dependency`, `Nodejs`

Required sections:

1. Problem: show `ERESOLVE unable to resolve dependency tree`.
2. Cause: peer dependency conflict, old package, incompatible React/Angular/Vite plugin version, stale lockfile.
3. Quick diagnosis:
   ```bash
   node -v
   npm -v
   npm explain package-name
   ```
4. Safe fix: align package versions and reinstall.
5. Cleanup command:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```
   Add Windows PowerShell equivalent.
6. Last resort: explain when `--legacy-peer-deps` is acceptable and what it hides.
7. Verification: run app tests or `npm run build`.

Internal links to add:

- `_posts/en/2025-08-01-javascript-failed-to-fetch.md`
- `_posts/en/2025-08-05-javascript-variables-var-vs-let-vs-const.md`
- `_posts/en/2025-08-05-javascript-promise-all-vs-promise-race.md`

Ad notes:

- Keep the lockfile cleanup and reinstall commands adjacent.

## Brief 7: Cannot find module in Node.js

- Translation ID: `node-cannot-find-module`
- Primary keyword: `Cannot find module node`
- Search intent: Node.js throws an import/require resolution error.
- Korean title: `Node.js Cannot find module 오류 해결 방법`
- English title: `Fix Cannot Find Module in Node.js`
- Header image: `/images/header_images/overlay_image_js.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `JavaScript`, `Nodejs`, `npm`, `Modules`

Required sections:

1. Problem: show `Error: Cannot find module '...'`.
2. Cause: missing install, wrong file path, wrong working directory, CommonJS/ESM mismatch, package export path.
3. Quick fix: install missing package or correct relative path.
4. Commands:
   ```bash
   npm install package-name
   npm ls package-name
   node -p "process.cwd()"
   ```
5. Path examples: `./utils/file.js` vs `utils/file.js`.
6. ESM notes: `type: module`, file extensions, `import` vs `require`.
7. Verification: rerun the exact Node command or test script.

Internal links to add:

- `_posts/en/2025-07-30-javascript-uncaught-referenceerror-is-not-defined.md`
- `_posts/en/2025-07-31-javascript-typeerror-is-not-a-function.md`
- `_posts/en/2025-08-05-javascript-jquery-is-not-defined.md`

Ad notes:

- Good mid-article ad after package vs path causes are separated.

## Brief 8: TypeScript Cannot find name

- Translation ID: `typescript-cannot-find-name`
- Primary keyword: `TypeScript Cannot find name`
- Search intent: TypeScript cannot see a variable, type, global, or library type.
- Korean title: `TypeScript Cannot find name 오류 해결 방법`
- English title: `Fix TypeScript Cannot Find Name`
- Header image: `/images/header_images/overlay_image_js.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `TypeScript`, `JavaScript`, `tsconfig`, `Types`

Required sections:

1. Problem: include `TS2304: Cannot find name`.
2. Cause: missing import, missing type package, wrong `lib`, wrong `types`, typo, test environment globals.
3. Quick fix: import the symbol or install `@types/...`.
4. Examples:
   ```bash
   npm install -D @types/node
   ```
   ```json
   {
     "compilerOptions": {
       "types": ["node"]
     }
   }
   ```
5. Browser vs Node globals: `document`, `process`, `Buffer`.
6. Verification: `npx tsc --noEmit`.
7. Common mistakes: adding `any`, suppressing with `// @ts-ignore`, editing the wrong tsconfig.

Internal links to add:

- `_posts/en/2025-07-30-javascript-uncaught-referenceerror-is-not-defined.md`
- `_posts/en/2025-08-05-javascript-variables-var-vs-let-vs-const.md`
- `_posts/en/2025-08-05-javascript-innerhtml-vs-textcontent.md`

Ad notes:

- Keep JSON config blocks together without ads between them.

## Brief 9: Property does not exist on type

- Translation ID: `typescript-property-does-not-exist`
- Primary keyword: `Property does not exist on type`
- Search intent: TypeScript knows an object type but the requested property is not declared.
- Korean title: `TypeScript Property does not exist on type 오류 해결 방법`
- English title: `Fix Property Does Not Exist on Type`
- Header image: `/images/header_images/overlay_image_js.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `TypeScript`, `Types`, `Interface`, `JavaScript`

Required sections:

1. Problem: include `TS2339: Property 'x' does not exist on type`.
2. Cause: object type is too narrow, API response type incomplete, union type not narrowed, DOM query result nullable.
3. Safe fixes: update interface, narrow the union, use optional chaining when appropriate.
4. Examples:
   ```ts
   type User = { id: number; name: string };
   ```
   ```ts
   if ("email" in user) {
     console.log(user.email);
   }
   ```
5. Explain what not to do: avoid `as any` as a default answer.
6. Verification: `npx tsc --noEmit`.
7. Related mistakes: confusing runtime object shape with compile-time type.

Internal links to add:

- `_posts/en/2025-07-30-javascript-typeerror-cannot-read-properties-of-null.md`
- `_posts/en/2025-07-30-javascript-uncaught-typeerror-cannot-read-properties-of-undefined.md`
- `_posts/en/2025-08-05-javascript-innerhtml-vs-textcontent.md`

Ad notes:

- Works as a longer educational troubleshooting post. One mid-article ad is acceptable.

## Brief 10: tsconfig paths not working

- Translation ID: `typescript-tsconfig-paths-not-working`
- Primary keyword: `tsconfig paths not working`
- Search intent: path aliases compile in one tool but fail in another, or do not work at all.
- Korean title: `tsconfig paths가 동작하지 않을 때 해결 방법`
- English title: `tsconfig Paths Not Working: How to Fix Path Aliases`
- Header image: `/images/header_images/overlay_image_js.png`
- Category: `ko_Troubleshooting` / `en_Troubleshooting`
- Tags: `TypeScript`, `tsconfig`, `Vite`, `Nodejs`

Required sections:

1. Problem: imports like `@/components/Button` fail.
2. Cause: missing `baseUrl`, wrong `paths`, runtime bundler not configured, test runner not configured, Node does not understand TS paths by itself.
3. tsconfig example:
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
4. Vite example: mention matching alias in `vite.config.ts`.
5. Node runtime: explain `tsconfig-paths`, bundling, or relative imports.
6. Verification: `npx tsc --noEmit` plus app/test command.
7. Common mistakes: editing `tsconfig.json` while framework uses `tsconfig.app.json`.

Internal links to add:

- `_posts/en/2025-08-05-javascript-jquery-is-not-defined.md`
- `_posts/en/2025-08-05-javascript-variables-var-vs-let-vs-const.md`
- `_posts/en/2025-07-31-javascript-typeerror-is-not-a-function.md`

Ad notes:

- Keep TypeScript and Vite config examples close together.

