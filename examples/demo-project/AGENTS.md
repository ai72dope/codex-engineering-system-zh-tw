# Codex Engineering System｜專案指令

本專案使用 Codex Engineering System。

## 核心工程規則
- 非簡單修改前，先理解相關程式碼、依賴、測試與資料流。
- 優先採用 Minimum Necessary Change，只修改完成任務必要的部分。
- 除非使用者明確要求，不改變公開 API、資料格式、業務規則或無關程式碼。
- 不用 `TODO`、`pass`、`... existing code ...` 等占位內容代替要求完成的實作。
- 不確定時說明假設、缺少資訊與風險，不編造專案事實。
- 修改後實際執行適用的測試、Lint、Type Check 或 Build；未執行不得聲稱通過。
- 遵循專案既有命名、格式、Lint 與架構慣例。
- 不記錄密碼、Token、API Key、Private Key 或其他 Secret。

## Workflow Routing
工程規範位於 `codex-system/`。只讀取目前任務需要的文件，不要預設一次載入全部。

### 完整 Workflow
- 新增／修改功能 → `codex-system/workflows/new_feature.md`
- Bug／錯誤／Regression → `codex-system/workflows/bug_fix.md`
- 重構 → `codex-system/workflows/refactor.md`
- 新專案／大型新模組 → `codex-system/workflows/project_setup.md`

### 專項規範
- Root Cause Debugging → `codex-system/prompts/debugging.md`
- Testing → `codex-system/prompts/testing.md`
- Code Review → `codex-system/prompts/code_review.md`
- Security Review → `codex-system/prompts/security_audit.md`
- Architecture → `codex-system/prompts/architecture.md`
- Refactoring Analysis → `codex-system/prompts/refactoring.md`
- 結構化任務描述 → `codex-system/prompts/docstring_templates.md`
- 日常快速任務 → `codex-system/prompts/codex_task_library.md`

## Routing 原則
1. 明確的新功能、Bug、重構或專案建立任務，先讀對應 Workflow。
2. 需要更深入的 Debug、Testing、Review、安全或架構分析時，再讀對應專項文件。
3. 簡單、低風險修改不必機械執行全部階段，但仍保留必要理解與驗證。
4. 複雜或高風險任務優先使用：
   `Understand → Plan → Implement → Test → Review → Verify`
5. Workflow 與使用者目前明確要求衝突時，以使用者要求為準，但不得虛構驗證結果。

## 完成任務時
簡短回報：
- **Changed**：改了什麼
- **Why**：為什麼改
- **Validation**：實際執行了哪些驗證
- **Remaining**：未驗證事項、假設或風險
