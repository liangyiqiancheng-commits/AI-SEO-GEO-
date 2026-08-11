【全局MD约束：Token节流 & 高命中规则】
## Skill: schema_generator
- 触发关键词：`generate_schema`
- 适用场景：为博客文章生成 JSON-LD 结构化数据
- 输入参数：{"source_file": "output/content/blog_xxx.md", "schema_type": "Article"}
- 工作流步骤：
  1. 读取源文章，提取标题、作者、发布日期、关键词
  2. 生成 Article / FAQPage JSON-LD
  3. 输出到 output/content/blog_<topic>_schema.json
- 质量审核标准：JSON-LD 格式合法；包含必要的 required 字段
- 产出路径：output/content/blog_*_schema.json
- 缓存复用标记：[REUSE:schema_template_id]
