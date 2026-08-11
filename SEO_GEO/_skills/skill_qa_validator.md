【全局MD约束：Token节流 & 高命中规则】
## Skill: qa_validator
- 触发关键词：`qa_check`
- 适用场景：四层质量检测（AI痕迹、SEO合规、事实、GEO适配）
- 输入参数：{"source_file": "output/content/blog_xxx.md", "check_type": "full"}
- 工作流步骤：
  1. 读取源文件
  2. 调用 Router 分配模型（Gemini 质量评分）
  3. 执行四层检测：AI痕迹/SEO合规/事实核查/GEO适配
  4. 输出检测报告
- 质量审核标准：每层检测必须输出评分；发现问题需标注行号；提供修复建议
- 产出路径：output/reports/qa_report_<topic>.md
- 缓存复用标记：[REUSE:qa_checklist_id]
