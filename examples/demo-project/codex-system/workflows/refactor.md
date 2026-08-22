# Refactor Workflow
1. **Baseline**：確認目前行為與既有測試；重要行為缺乏測試時，先考慮 Characterization Test。
2. **Plan**：明確定義重構目的，例如可讀性、責任邊界、重複、耦合或可測試性。
3. **Refactor**：小步驟、保持行為不變；避免無關依賴升級或業務規則修改。
4. **Validate**：執行相關測試與適用的 Lint／Type Check／Build。
5. **Review**：檢查過度抽象、碎片化、新耦合、效能 Regression 與脆弱測試。
