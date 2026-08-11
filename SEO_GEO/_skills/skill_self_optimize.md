【全局MD约束：Token节流 & 高命中规则】
## Skill: self_optimize
- 触发关键词：`auto_optimize`
- 适用场景：根据 QA 检测结果自动重写内容
- 输入参数：{"source_file": "output/content/blog_xxx.md", "qa_report": "output/reports/qa_report_xxx.md"}
- 工作流步骤：
  1. 读取源文件和 QA 报告
  2. 调用 Router 分配模型（优先 Claude）
  3. 针对每个问题行进行重写
  4. 输出优化后版本
- 质量审核标准：所有 QA 问题得到修复；保持原文核心信息；字数变化不超过±20%
- 产出路径：output/content/blog_<topic>_optimized.md
- 缓存复用标记：[REUSE:rewrite_pattern_id]
