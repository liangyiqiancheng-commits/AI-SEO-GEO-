【全局MD约束：Token节流 & 高命中规则】
## Skill: blog_writer
- 触发关键词：`write_blog`
- 适用场景：生成1500+字结构化博客文章
- 输入参数：{"topic": "AI SEO tools", "url": "https://example.com", "tone": "professional"}
- 工作流步骤：
  1. 读取品牌语境 _context/brand/Brand_Voice_Guide.md
  2. 调用 Router 分配模型（优先 Claude）
  3. 生成 H2/H3 结构化文章（1500+字）
  4. 包含内部链接建议、FAQ 部分
  5. 输出到 output/content/blog_<topic>.md
- 质量审核标准：至少1500字；H2 不超过5个；包含 FAQ 章节；语气符合品牌指南
- 产出路径：output/content/blog_*.md
- 缓存复用标记：[REUSE:blog_template_id]
