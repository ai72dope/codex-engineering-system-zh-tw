# Codex Engineering System v1.2｜繁體中文版

一套可直接安裝到專案中的 Codex 工程工作流程系統。

你不需要每次複製一大段 Prompt。安裝一次後，照平常方式使用 Codex 即可。

## 安裝
把 `INSTALL_TO_YOUR_PROJECT/` 裡的 `AGENTS.md` 與 `codex-system/` 複製到你的專案根目錄。

## 運作方式
```text
你的需求
    ↓
AGENTS.md
    ↓
判斷任務類型
    ↓
codex-system/
├── workflows/
└── prompts/
    ↓
對應的工程流程
```

例如：
- 新增功能 → New Feature Workflow
- 修 Bug → Bug Fix Workflow
- 重構 → Refactor Workflow
- Review 修改 → Code Review
- 安全檢查 → Security Audit

核心流程：
`理解 → 規劃 → 實作 → 測試 → Review → 驗證`

這套系統不會讓 AI 突然變得不會犯錯；它的目的，是讓 Codex 有一套更一致、可預期的工程流程。
