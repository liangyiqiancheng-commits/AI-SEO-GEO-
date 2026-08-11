【全局MD约束：Token节流 & 高命中规则】
## Skill: geo_optimizer
- 触发关键词：`geo_optimize`
- 适用场景：将现有内容重构为 GEO 友好格式
- 输入参数：{"source_file": "output/content/blog_xxx.md"}
- 工作流步骤：
  1. 读取源文件
  2. 调用 Router 分配模型
  3. 重构内容：增加 FAQ、数据引用、摘要框
  4. 优化开头段落（AI 引擎常用引用位置）
  5. 输出优化后版本
- 质量审核标准：新增 FAQ 至少5个问题；包含至少3个数据引用点
- 产出路径：output/content/blog_<topic>_geo.md
- 缓存复用标记：[REUSE:geo_opt_template_id]
