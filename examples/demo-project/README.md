# Demo Project — v1.3.2

這個小型專案用來示範 Codex Engineering System 的安裝方式與 Adaptive Routing 行為。

Repository 內包含：

- `AGENTS.md`
- `codex-system/`
- 範例 Source Code 與 Tests

你可以嘗試不同深度的需求：

- Simple：`Rename a local variable for clarity without changing behavior.`
- Bug：`Find and fix the order total bug and add a regression test.`
- Complex Feature：`Add discount rules with explicit acceptance criteria and tests.`

觀察重點是：小任務保持輕量；模糊、複雜或高風險工作則增加 Specification、Testing 與 Verification 深度。

若要測 TDD，請確認最後回覆包含真實 `TDD Trace`，而不只是說「using TDD」。

若要測 Routing Visibility，每個 Case 請使用乾淨的 Demo 副本，避免前一題修改造成 Test Environment Contamination。
