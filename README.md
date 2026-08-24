# Codex Engineering System v1.3.3 — 繁體中文版

一套可直接安裝到程式碼儲存庫（repository）的 Codex 工程工作流程系統。

安裝一次之後，你仍然可以像平常一樣向 Codex 提出需求。系統會根據 **任務類型、複雜度與風險** 自動決定工程流程深度，而不是讓所有任務都跑同一套流程。

> **重要：** 本繁體中文版將「使用者說明文件」中文化，但 `INSTALL_TO_YOUR_PROJECT/` 內實際給 Codex 執行的 Runtime Instructions 保留英文原文。這是刻意的設計：v1.3.3 的 Demo 驗證是基於英文 Runtime 規則完成，直接翻譯這些規則可能改變 Codex 行為，因此不在未重新驗證前修改核心執行層。

## 安裝

將 `INSTALL_TO_YOUR_PROJECT/` 裡的這兩個項目複製到你的專案根目錄：

```text
AGENTS.md
codex-system/
```

例如：

```text
your-project/
├── AGENTS.md
├── codex-system/
├── src/
└── tests/
```

安裝後不需要特殊指令，也不需要每次複製 Prompt。

你仍然可以直接說：

> Fix this login bug.

> Add password reset.

> Refactor this module without changing its public API.

## 它解決什麼問題？

Codex 能寫程式，但不同任務需要的工程深度並不相同。小修改不需要完整規格流程；模糊的大型功能、高風險授權邏輯或資料破壞操作，則需要更嚴格的規格、測試與驗證。

Codex Engineering System 的目標，是讓 Codex 根據任務情境選擇適合的工程流程，同時降低過度工程、亂猜產品規則、擴大修改範圍，以及未實際執行驗證卻宣稱成功等問題。

## Adaptive Routing（自適應路由）

```text
你的需求
   ↓
任務類型 + 複雜度 + 風險
   ↓
┌──────────────┬────────────────┬──────────────────────────┐
│ Simple       │ Standard       │ Complex                  │
│ 理解         │ 理解           │ 理解                     │
│ 修改         │ 規劃           │ Spec                     │
│ 定向驗證     │ 實作           │ Acceptance Criteria      │
│              │ 測試           │ 適合時使用 TDD           │
│              │ 驗證           │ 實作 → Review → Verify   │
└──────────────┴────────────────┴──────────────────────────┘
```

Authentication、Authorization、Payments、Secrets、Database Migration、Destructive Operations、Security Boundaries、Concurrency、Production Infrastructure 等高風險工作，會提高 Specification、Testing、Security 與 Verification 的深度。

## 核心功能

- **Adaptive Routing** — 依 Task Type、Complexity、Risk 選擇流程深度。
- **Scope Control** — 缺少 Repository Context 時，不自行發明不存在的 API 或架構。
- **Spec-Driven Development** — 需求模糊時先釐清 Requirements、Acceptance Criteria、Edge Cases 與 Out of Scope。
- **Bug Fix Discipline** — Reproduce → Root Cause → Regression Test → Minimal Fix → Verify。
- **Selective TDD** — 適合時才使用 RED → GREEN → REFACTOR → FULL SUITE。
- **Verification Contract** — 明確區分 Passed / Failed / Not run / Manual-Static check。
- **Routing Trace / Observability** — 非 Simple 任務嘗試顯示所選 Route，讓使用者知道系統採用了什麼流程。

## v1.3.3 的主要變更

v1.3.3 主要改善 **Routing Visibility**。

對非 Simple 任務，規則要求 Codex 在分類後、進入 clarification、planning、blocker message 或 implementation 之前先顯示 Route，例如：

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: High
- Spec: Yes
- TDD: Pending
- Specialist: Security, Testing
```

### Beta 已知限制

目前 Demo 驗證顯示：核心 Routing 決策、Spec 行為、Risk Awareness、TDD Trace 與 Verification Honesty 均能運作；但 **Routing Trace 的顯示時機不是每次都完全一致**。特別是在 Codex 需要立即詢問澄清問題或因 Repository 缺少必要 Context 而停止時，有時會先回覆問題／Blocker，而沒有先顯示 Route。

這屬於目前 Beta 的 Observability 已知限制，不代表核心 Routing Decision 沒有發生。

## Verification Contract

Codex 必須區分：

- **Passed** — 實際執行且成功。
- **Failed** — 實際執行且失敗。
- **Not run** — 未執行。
- **Manual/Static check** — 僅人工／靜態檢查，沒有實際執行。

不能把「看起來應該可以」或未執行的命令寫成 Passed。

## 內含內容

- Feature Development Workflow
- Root-Cause Bug Fix Workflow
- Refactoring / Project Setup
- Complexity Routing
- Risk Routing
- Spec-Driven Development
- Optional TDD Workflow
- Debugging / Testing / Code Review / Security / Architecture / Refactoring Guidance
- Issue / PR / Changelog Templates
- Demo Project

## 產品定位

這不是 Codex Plugin，也不是官方 Skill。

比較準確的定位是：

> **A repository-level adaptive engineering workflow and instruction system for Codex.**

中文可以理解為：

> **一套安裝在程式專案內，依任務類型、複雜度與風險，自動調整 Codex 工程流程深度的工作流程系統。**

## 重要聲明

這套系統提供的是工程 Workflow 與 Project Instructions。它不能保證 AI 產生的程式碼零錯誤、安全或可直接投入 Production。正式環境的變更仍需要適當測試、Code Review 與人工判斷。
