# START HERE｜安裝一次，之後正常使用 Codex

不需要每次打開 Markdown 複製 Prompt。

## 安裝
將以下兩個項目複製到你的程式專案根目錄：

```text
INSTALL_TO_YOUR_PROJECT/
├── AGENTS.md
└── codex-system/
```

安裝後：

```text
your-project/
├── AGENTS.md
├── codex-system/
├── src/
└── tests/
```

完成。

## 怎麼用？
照平常方式跟 Codex 說需求：

- 「幫我新增忘記密碼功能。」
- 「幫我修登入偶爾出現 500 的 Bug。」
- 「重構這個模組，但不要改公開 API。」
- 「Review 我目前的修改。」

`AGENTS.md` 會依任務引導 Codex 讀取 `codex-system/` 裡對應的 Workflow 或專項規範。

## 裡面有什麼？
- `workflows/`：新功能、Bug Fix、重構、專案建立流程
- `prompts/`：Debug、Testing、Code Review、安全、架構等專項規範
- `templates/`：Issue、PR、Changelog 模板
- `docs/`：使用與工程指南

核心流程：

`理解 → 規劃 → 實作 → 測試 → Review → 驗證`

簡單任務可以縮短流程；複雜或高風險任務應保留更完整的驗證。

## 注意
這套系統提供的是工程規範與工作流程，不保證 AI 產出的程式碼零錯誤。正式環境修改仍應進行實際測試與必要的人工 Review。
