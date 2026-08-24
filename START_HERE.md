# START HERE — Codex Engineering System v1.3.3 繁體中文版

## 1. 安裝一次

將：

```text
INSTALL_TO_YOUR_PROJECT/
├── AGENTS.md
└── codex-system/
```

複製到你的 Repository 根目錄：

```text
your-project/
├── AGENTS.md
├── codex-system/
├── src/
└── tests/
```

## 2. 像平常一樣使用 Codex

不需要特殊語法，也不需要複製固定 Prompt。

例如：

- `Fix this login bug.`
- `Add a password reset feature.`
- `Refactor this module without changing its public API.`
- `Review my current changes for security issues.`

你也可以直接用中文向 Codex 描述 Coding 需求；核心 Runtime Instructions 保留英文，不影響你使用中文下需求。

## 3. 背後會發生什麼？

系統會先考慮：

1. 這是什麼 Task Type？
2. Complexity 是 Simple、Standard 還是 Complex？
3. Risk 是 Normal 還是 High？
4. 是否需要 Spec？
5. TDD 是否能提供有效回饋？

因此小修改可以保持輕量，而複雜或高風險工作會獲得更完整的工程流程。

## 4. 你應該注意的核心行為

- 小修改不應被過度工程化。
- Bug 應優先找 Root Cause，而不是看到可疑位置就直接 Patch。
- 模糊的產品規則不應由 Codex 自己發明。
- 高風險變更應提高測試與驗證深度。
- 使用 TDD 時，應有實際 RED / GREEN / REFACTOR 執行證據。
- 沒有跑 Test，就不能聲稱 Tests Passed。

## 5. v1.3.3 Routing Visibility

非 Simple 任務理想上會先看到：

```text
Route
- Task: Bug
- Complexity: Standard
- Risk: Normal
- Spec: No
- TDD: Yes
```

目前 Beta 已知 Route 顯示時機並非 100% 穩定，尤其是需要 clarification 或遇到 missing repository context 時。請把它視為 Observability 功能，而不是核心工程決策本身。

## 6. Demo

`examples/demo-project/` 提供一個小型測試專案。若要做 Regression Test，請每個 Case 使用乾淨的 Demo 副本，避免前一個測試修改 Repository 後污染下一個結果。

## 7. 語言版本說明

本 ZH-TW Edition 中文化的是使用者閱讀與發佈所需文件。`INSTALL_TO_YOUR_PROJECT/` 中實際控制 Codex 行為的規則維持 v1.3.3 英文版原文，以避免未重新驗證的翻譯改變 Routing / TDD / Verification 行為。
