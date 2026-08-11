【全局MD约束：Token节流 & 高命中规则】
## Skill: seo_research
- 触发关键词：`keyword_research`
- 适用场景：关键词研究、竞品关键词分析
- 输入参数：{"url": "https://example.com", "keywords": ["seed1", "seed2"]}
- 工作流步骤：
  1. 读取 _config/tools_registry.json 获取 Serper 配置
  2. 调用 tool_gateway.py 执行 serper_search
  3. 解析搜索结果，提取关键词、搜索量、竞争度
  4. 输出 CSV 到 output/strategy/keywords.csv
- 质量审核标准：至少返回20个相关关键词；包含长尾词和短尾词；标注搜索意图
- 产出路径：output/strategy/keywords.csv
- 缓存复用标记：[REUSE:keyword_list_id]
