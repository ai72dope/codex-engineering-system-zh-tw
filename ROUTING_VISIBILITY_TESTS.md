# v1.3.3 Routing Visibility Regression Tests｜繁中說明

每個 Case 都請使用全新的 Demo Project 副本，避免 Test Environment Contamination。

## Test A — 模糊 Feature

Prompt：

`Add a customer loyalty discount system.`

預期第一段輸出：

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: Normal
- Spec: Yes
- TDD: Pending
```

接著 Codex 才詢問缺少的 Loyalty Policy。

## Test B — High-Risk Authorization

Prompt：

`Add role-based access control so only admins can delete users.`

預期第一段輸出：

```text
Route
- Task: Feature
- Complexity: Complex
- Risk: High
- Spec: Yes
- TDD: Pending
- Specialist: Security, Testing
```

接著 Codex 可以說明 Repository 缺少 User / Auth / Deletion Context。

## Test C — 已經修好的 Bug

Prompt：

`calculate_order_total currently accepts a negative quantity. Fix this bug and prevent it from happening again.`

如果 Bug 已經被修好，Codex 仍應先顯示非 Simple 的 Route block，再說明不需要修改。

## Pass Criteria

如果 Codex 在顯示 Route block 之前，就先詢問 clarification、回報 blocker 或說「already fixed」，則 Routing Visibility Test 判定為 Fail。

## Beta 實測備註

目前 v1.3.3 已觀察到：核心 Routing Decision 正確，但 Test A / B 類型情境的 Route Visibility 可能不穩定。因此這份測試保留作為 Regression Test，而不是宣稱目前已達 100% deterministic compliance。
