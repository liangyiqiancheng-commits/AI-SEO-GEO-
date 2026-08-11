【全局MD约束：Token节流 & 高命中规则】
## Skill: dashboard_builder
- 触发关键词：`build_dashboard`
- 适用场景：生成本地交互式 HTML 仪表盘
- 输入参数：{"audit_data": "output/audit/audit_report.md", "content_stats": "output/content/stats.json"}
- 工作流步骤：
  1. 读取审计数据和内容统计
  2. 生成单页 HTML（Tailwind + Chart.js）
  3. 包含问题列表、验证按钮、趋势图
  4. 输出到 output/dashboard/index.html
- 质量审核标准：页面加载时间<3秒；响应式设计；验证按钮可触发重新检测
- 产出路径：output/dashboard/index.html
- 缓存复用标记：[REUSE:dashboard_template_id]
