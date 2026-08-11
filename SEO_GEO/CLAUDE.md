# SEO/GEO 自动化增长工厂 — 顶层约束

## 全局 Token 节流 & 高命中规则（所有层必须遵守）
1. **上下文复用**：历史已输出品牌/风格/流程参数仅用 ID/简称指代，禁止重复完整复述。
2. **输出精简**：禁止寒暄、铺垫、多余解释；数据用极简表格或数组；单段文字不超过 5 行。
3. **指令高命中**：工作流、触发词必须使用固定标准化关键词（精确匹配），禁止同义改写；查询优先使用 registry 中的 ID 匹配。
4. **缓存优先**：所有可复用的品牌话术、模板、告警文案必须存入 `_cache/reuse_fragments/`，调用时标记 `[REUSE:xxx_id]`。
5. **路由强制**：所有 AI 生成请求必须经过 `_router/gateway/model_router.py` 分配模型；禁止在 Skill/Workflow 中硬编码模型名。
6. **工具强制**：所有第三方 API 调用必须经过 `_tools/gateway/tool_gateway.py`；禁止在 Skill 中直接调用外部接口。
7. **输出格式**：配置类纯 JSON（无注释）；流程类编号极简；模板只保留填充点位。
8. **错误处理**：指令歧义时优先读 registry 匹配 ID，匹配失败则返回「参数缺失/不匹配」，不自行臆测。

## 标准触发词（精准匹配，大小写敏感）
| 触发词 | 动作 |
|--------|------|
| `init` | 初始化项目（已执行） |
| `audit <url>` | 审计工作流 |
| `generate <url>` | 策略与内容生产工作流 |
| `qa` 或 `deliver` | QA 与交付工作流 |
| `start-dashboard` | 构建交互式仪表盘 |
| `write_blog <topic>` | 单技能：撰写博客 |
| `keyword_research` | 单技能：SEO 关键词研究 |
| `geo_intent` | 单技能：AI 搜索意图分析 |
| `geo_optimize` | 单技能：GEO 内容优化 |
| `generate_schema` | 单技能：Schema 标记生成 |
| `screenshot` | 单技能：原型截图 |
| `qa_check` | 单技能：质量检测 |
| `auto_optimize` | 单技能：自优化 |
| `export_pdf` | 单技能：PDF 报告 |
| `to_slides` | 单技能：幻灯片生成 |
| `build_dashboard` | 单技能：仪表盘构建 |
| `strategy` | 单技能：网站策略 |
| `status` | 查看额度消耗与缓存命中率 |

## 目录用途速查
```
_config/        → 密钥、路由、工具、技能注册表
_context/       → 品牌、受众、平台、业务语境
_blocks/        → 风格指南、模板、竞品参考
_skills/        → 12 个独立技能文件
_tools/         → 工具说明 + 网关脚本
_router/        → 模型路由 + 配额监控
_workflow/      → 三大工作流 JSON
_scripts/       → Python 调度脚本
_cache/         → 复用片段、Token 统计、匹配缓存
output/         → 所有产出（audit, strategy, content, reports, dashboard）
```
