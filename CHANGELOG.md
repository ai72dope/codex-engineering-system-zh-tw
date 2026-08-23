# 更新紀錄（Changelog）

## [1.3.2] - 2026-08-23
### 修正
- 非 Simple 任務完成分類後，Routing Trace 應立即顯示。
- 只有 clarification 的回覆也應先顯示 Route block。
- Missing-context 與「already fixed」回覆也應先顯示 Route block。
- Spec / TDD 尚未決定時可使用 `Pending`。
- TDD Trace 明確要求真實執行證據。

## [1.3.1] - 2026-08-23
### 新增
- Standard、Complex、High-Risk 任務的 Compact Routing Trace。
- Simple 任務的一行 Route Trace。
- 包含真實 RED / GREEN / REFACTOR / Full Suite 證據的 TDD Trace。
- 新增 `docs/OBSERVABILITY.md`。

### 變更
- Completion Report 加入所選 Route。
- 沒有可觀察的執行證據，不應宣稱完成 TDD。
- Feature 與 Bug Workflow 加入 Routing / TDD Trace 規則。

## [1.3.0] - 2026-08-23
### 新增
- Simple / Standard / Complex Complexity Routing。
- 獨立 High-Risk Routing。
- Spec-Driven Development 與 Acceptance Criteria / Out-of-Scope 邊界。
- Optional TDD：Red → Green → Refactor。
- Verification Contract：Passed / Failed / Not run / Manual-Static check。

### 變更
- Feature Workflow 會依 Complexity 與 Risk 調整深度。
- Bug Workflow 強調 Reproduction、Root Cause、Regression Test 與 Minimal Fix。
- `AGENTS.md` 改為 Adaptive Router，而不是所有任務強制同一深度。
- 採 Progressive Disclosure，只載入當前任務需要的 Workflow / Guidance。

## [1.2.0] - 2026-08-22
- 改用 `codex-system/` 目錄，避免 Hidden Folder 的上傳與可見性問題。
- 安裝方式統一為 Repository Root 下的 `AGENTS.md` + `codex-system/`。
- 導入 Install-Once 架構與 AGENTS.md Workflow Routing。
- 不再以手動複製 Prompt 作為預設使用方式。

## [1.0.0] - 2026-08-22
- 初始版本。
