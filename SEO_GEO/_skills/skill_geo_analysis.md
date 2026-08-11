【全局MD约束：Token节流 & 高命中规则】
## Skill: geo_analysis
- 触发关键词：`geo_intent`
- 适用场景：分析 ChatGPT/Perplexity 等 AI 引擎的引用来源和搜索意图
- 输入参数：{"topic": "AI SEO tools", "url": "https://example.com"}
- 工作流步骤：
  1. 调用 Router 分配模型（优先 Perplexity）
  2. 搜索该主题在 AI 引擎中的常见引用来源
  3. 分析 AI 回答结构：FAQ、数据引用、摘要框
  4. 输出分析结果到 output/strategy/geo-analysis.md
- 质量审核标准：识别至少5个高频引用来源；标注 AI 回答中的结构化元素
- 产出路径：output/strategy/geo-analysis.md
- 缓存复用标记：[REUSE:geo_pattern_id]
