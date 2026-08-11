【全局MD约束：Token节流 & 高命中规则】
## Skill: pdf_reporter
- 触发关键词：`export_pdf`
- 适用场景：将 Markdown 渲染为 A4 PDF 报告
- 输入参数：{"source_files": ["output/audit/audit_report.md"], "title": "SEO Audit Report"}
- 工作流步骤：
  1. 读取源 Markdown 文件
  2. 使用 markitdown 转换
  3. 生成带封面、目录的 PDF
  4. 输出到 output/reports/Final_Report.pdf
- 质量审核标准：PDF 包含封面（网站截图）；包含技术错误表格；包含修复建议
- 产出路径：output/reports/Final_Report.pdf
- 缓存复用标记：[REUSE:pdf_template_id]
