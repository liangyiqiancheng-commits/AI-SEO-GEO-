# 工作流说明

## 审计工作流 (audit_flow)
触发: `audit <url>`
流程: 爬取网页 → PageSpeed 检测 → 关键词研究 → 截图 → 质量检查
输出: output/audit/audit_report.md + screenshot.png

## 策略与内容工作流 (strategy_content_flow)
触发: `generate <url>`
流程: 12周策略 → AI搜索分析 → 博客撰写 → GEO优化 → Schema生成
输出: output/strategy/12-week-roadmap.md + output/content/blog_*.md

## QA与交付工作流 (qa_delivery_flow)
触发: `qa` 或 `deliver`
流程: 质量检测 → 自动优化 → PDF报告 → 幻灯片 → 仪表盘
输出: output/reports/Final_Report.pdf + output/dashboard/index.html
