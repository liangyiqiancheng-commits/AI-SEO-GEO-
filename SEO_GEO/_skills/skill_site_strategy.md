【全局MD约束：Token节流 & 高命中规则】
## Skill: site_strategy
- 触发关键词：`strategy`
- 适用场景：为新网站制定12周SEO/GEO增长路线图
- 输入参数：{"url": "https://example.com", "target_market": "zh-CN"}
- 工作流步骤：
  1. 读取 _config/brand_config.json 品牌语境
  2. 调用 Router 分配模型（优先 Claude）
  3. 生成12周路线图（技术修复+内容主题+外链建设）
  4. 输出到 output/strategy/12-week-roadmap.md
- 质量审核标准：必须覆盖技术SEO基础修复；内容主题需匹配目标受众搜索意图
- 产出路径：output/strategy/12-week-roadmap.md
- 缓存复用标记：[REUSE:brand_voice_id]
