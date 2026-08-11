【全局MD约束：Token节流 & 高命中规则】
## Skill: mark_slides
- 触发关键词：`to_slides`
- 适用场景：生成 Marp 格式幻灯片
- 输入参数：{"source": "output/reports/Final_Report.pdf", "theme": "default"}
- 工作流步骤：
  1. 读取源报告内容
  2. 提取关键发现和建议
  3. 生成 Marp 格式幻灯片
  4. 输出到 output/reports/presentation.marp.md
- 质量审核标准：每页不超过5行内容；包含标题页、问题页、建议页
- 产出路径：output/reports/presentation.marp.md
- 缓存复用标记：[REUSE:slide_template_id]
