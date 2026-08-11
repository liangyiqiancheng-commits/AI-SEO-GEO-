# 🤖 SEO/GEO 自动化增长工厂

<div align="center">

**AI 驱动的网站 SEO 审计 · GEO 内容生成 · 智能优化一体化平台** — 一键驱动网站审计 → 内容策略 → AI 写作 → 质量检测 → 报告交付

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Workflow: 3](https://img.shields.io/badge/Workflow-3-green.svg)]()
[![Skills: 12](https://img.shields.io/badge/Skills-12-purple.svg)]()

[项目概述](#-项目概述) · [快速开始](#-快速开始) · [技能模块](#-技能模块) · [工作流](#-工作流) · [贡献指南](#-贡献指南)

</div>

---

## 📋 项目概述

`SEO_GEO` 是一套完整的 AI 驱动网站增长自动化系统，专为 SEO 从业者和内容运营团队设计。通过 **标准化技能模块 + 工作流引擎** 的架构，实现从网站审计到内容产出的全链路自动化。

### ✨ 核心能力

| 能力 | 说明 | 对应模块 |
|------|------|---------|
| 🔍 SEO 审计 | 爬取网站 → PageSpeed 检测 → 关键词研究 → 质量检查 | `audit` Workflow |
| 📊 策略生成 | 12周增长路线 → AI 搜索意图分析 → 博客撰写 | `generate` Workflow |
| 🤖 GEO 优化 | 生成式引擎优化 → Schema 标记 → 内容重构 | `geo_optimize` Skill |
| ✅ QA 交付 | 质量检测 → 自动优化 → PDF 报告 → 仪表盘 | `qa` Workflow |
| 🔄 自优化 | 基于反馈闭环持续迭代内容质量 | `auto_optimize` Skill |

---
层级	功能描述
Layer 1 地基	全局配置（.env）、品牌资产（_context）、JSON 注册表
Layer 2 积木	视觉风格指南（STYLE-GUIDE）、竞品素材库、标准模板
Layer 3 技能	12 个标准化内容生产单元（见下文功能矩阵）
Layer 4 工具	第三方 API 网关（飞书/Notion/爬虫/性能检测）
Layer 5 路由	多模型额度监控、故障转移、Token 成本权重分配
Layer 6 工作流	串行/并行流程编排，支持条件分支与工具节点插入
Layer 7 项目	临时产出归档、交付物打包、看板渲染

## ✨ 核心亮点

- **🎯 目标驱动**：精准提升 ChatGPT、Perplexity 等 AI 搜索引擎的引用流量，访客平均停留时长 ≥ 7 分钟。
- **🏗️ 七层解耦架构**：严格遵循 Foundation → Blocks → Skills → Tools → Router → Workflow → Projects，逻辑清晰，易于维护。
- **🤖 智能模型路由（Router）**：内置额度监控与熔断机制。Claude 额度耗尽时自动降级切换至 Grok / GPT-4o，杜绝超额扣费。
- **💰 Token 极致节约（V4.1）**：全局缓存复用（`_cache`）+ 成本权重分流，相比传统方案降低 40%~70% Token 消耗。
- **🔧 统一工具网关**：Firecrawl、Serper、PageSpeed、Perplexity、Gemini 等外部 API 统一封装，禁止硬编码。


## 🗂️ 目录结构

```
SEO_GEO/
│
├── _config/                              # 配置中心
│   ├── .env.example                      # 环境变量模板
│   ├── brand_config.json                 # 品牌配置
│   ├── router_registry.json              # 模型路由表
│   ├── skill_triggers.json               # 技能触发词映射
│   ├── tools_registry.json               # 工具注册表
│   ├── platform_rules.json               # 平台规则
│   └── workflow_index.json               # 工作流索引
│
├── _context/                             # 业务语境
│   ├── brand/                            #    品牌指南
│   ├── audience/                         #    受众画像
│   ├── business/                         #    业务说明
│   └── platform/                         #    平台策略
│
├── _blocks/                              # 素材库
│   └── style/                            #    风格指南
│
├── _skills/                              # 技能文件 (12个)
│   ├── skill_site_strategy.md
│   ├── skill_seo_research.md
│   ├── skill_geo_analysis.md
│   ├── skill_blog_writer.md
│   ├── skill_geo_optimizer.md
│   ├── skill_schema_generator.md
│   ├── skill_mockup_gen.md
│   ├── skill_qa_validator.md
│   ├── skill_self_optimize.md
│   ├── skill_pdf_reporter.md
│   ├── skill_mark_slides.md
│   └── skill_dashboard_builder.md
│
├── _tools/                               # 工具网关
│   └── gateway/
│       └── tool_gateway.py
│
├── _router/                              # 模型路由
│   ├── gateway/
│   │   ├── model_router.py
│   │   └── route_alarm.py
│   ├── router_json/
│   └── router_md/
│
├── _workflow/                            # 工作流定义
│   ├── flow_json/
│   │   ├── flow_audit.json
│   │   ├── flow_strategy_content.json
│   │   └── flow_qa_delivery.json
│   └── flow_md/
│       └── workflow_guide.md
│
├── _scripts/                             # Python 脚本
│   ├── init.py
│   ├── workflow_scheduler.py
│   ├── dashboard_render.py
│   ├── token_stat.py
│   ├── validate_output.py
│   ├── asset_sync.py
│   └── batch_export.py
│
├── _cache/                               # 缓存系统
│   └── reuse_fragments/                  # 复用片段
│
├── output/                               # 产出目录
│   ├── audit/
│   ├── strategy/
│   ├── content/
│   ├── reports/
│   └── dashboard/
│
├── .gitignore
└── README.md
```

---

## 🚀 快速开始

### 1️⃣ 环境准备

```bash
# 克隆项目
git clone https://github.com/your-username/seo-geo-growth-factory.git
cd seo-geo-growth-factory

# 初始化项目
python _scripts/init.py
```

### 2️⃣ 配置 API Key

编辑 `_config/.env` 文件，填入你的 API 密钥：

```bash
# 复制模板并修改
cp _config/.env.example _config/.env
```

> 💡 获取 API Key：访问 [Anthropic](https://console.anthropic.com)、[OpenAI](https://platform.openai.com)、[Google AI](https://ai.google.dev) 等平台注册获取

### 3️⃣ 触发技能

**常用命令示例：**

```bash
# 运行完整审计工作流
python _scripts/run_workflow.py audit https://example.com

# 生成策略与内容
python _scripts/run_workflow.py generate https://example.com

# QA 质检与交付
python _scripts/run_workflow.py qa

# 单独执行技能
strategy https://example.com
keyword_research https://example.com
write_blog "最佳SEO实践"
geo_optimize output/content/blog_01.md
```

---

## 📖 技能模块

每个 Skill 是一个独立的可复用能力单元：

| Skill | 功能 | 触发词 | 产出 |
|-------|------|--------|------|
| [skill_site_strategy](./_skills/skill_site_strategy.md) | 网站策略分析 | `strategy` | `output/strategy/*_roadmap.md` |
| [skill_seo_research](./_skills/skill_seo_research.md) | SEO 关键词研究 | `keyword_research` | `output/strategy/*_keywords.md` |
| [skill_geo_analysis](./_skills/skill_geo_analysis.md) | AI 搜索意图分析 | `geo_intent` | `output/content/*_intent.md` |
| [skill_blog_writer](./_skills/skill_blog_writer.md) | 博客文章撰写 | `write_blog <topic>` | `output/content/blog_*.md` |
| [skill_geo_optimizer](./_skills/skill_geo_optimizer.md) | GEO 内容优化 | `geo_optimize` | `output/content/*_geo.md` |
| [skill_schema_generator](./_skills/skill_schema_generator.md) | Schema 标记生成 | `generate_schema` | `output/content/*_schema.json` |
| [skill_mockup_gen](./_skills/skill_mockup_gen.md) | 原型截图 | `screenshot` | `output/audit/*_screenshot.png` |
| [skill_qa_validator](./_skills/skill_qa_validator.md) | 质量检测 | `qa_check` | `output/reports/*_qa.md` |
| [skill_self_optimize](./_skills/skill_self_optimize.md) | 自优化循环 | `auto_optimize` | 迭代优化版本 |
| [skill_pdf_reporter](./_skills/skill_pdf_reporter.md) | PDF 报告导出 | `export_pdf` | `output/reports/Final_Report.pdf` |
| [skill_mark_slides](./_skills/skill_mark_slides.md) | 幻灯片生成 | `to_slides` | `output/reports/presentation.*` |
| [skill_dashboard_builder](./_skills/skill_dashboard_builder.md) | 交互式仪表盘 | `build_dashboard` | `output/dashboard/index.html` |

---

## 🔄 工作流

Workflow 串联多个 Skill，实现端到端的自动化流程：

| Workflow | 流程 | 触发词 |
|----------|------|--------|
| [audit_flow](./_workflow/flow_json/flow_audit.json) | 爬取 → PageSpeed检测 → 关键词研究 → 截图 → QA检查 | `audit <url>` |
| [strategy_content_flow](./_workflow/flow_json/flow_strategy_content.json) | 12周策略 → AI意图分析 → 博客撰写 → GEO优化 → Schema生成 | `generate <url>` |
| [qa_delivery_flow](./_workflow/flow_json/flow_qa_delivery.json) | 质量检测 → 自动优化 → PDF报告 → 幻灯片 → 仪表盘 | `qa` / `deliver` |

---

## 📝 全局约束

> 所有层必须遵守的核心规则

| # | 规则 | 说明 |
|:-:|------|------|
| ① | **上下文复用** | 历史参数仅用 ID/简称指代，禁止重复复述 |
| ② | **缓存优先** | 可复用片段存入 `_cache/reuse_fragments/`，标记 `[REUSE:xxx_id]` |
| ③ | **路由强制** | 所有 AI 请求经 `_router/gateway/model_router.py` 分配 |
| ④ | **工具强制** | 所有 API 调用经 `_tools/gateway/tool_gateway.py` |
| ⑤ | **高命中规则** | 触发词精确匹配，不自行改写 |

---

## 📊 输出文件说明

所有生成内容自动归档到 `output/` 对应子目录：

| 目录 | 内容 | 格式 |
|------|------|------|
| `output/audit/` | 技术 SEO 评分、性能数据、问题清单 | `.md` / `.json` |
| `output/strategy/` | 12周增长路线图、关键词策略 | `.md` |
| `output/content/` | AI 撰写的博客文章、落地页 | `.md` / `.html` |
| `output/reports/` | 完整交付报告 | `.pdf` |
| `output/dashboard/` | 交互式数据可视化面板 | `.html` |

---

## ⚙️ 自定义指南

- **添加新的技能**：在 `_skills/` 下创建新的 `.md` 文件，并在 `_config/skill_triggers.json` 中注册
- **修改路由策略**：编辑 `_config/router_registry.json` 调整模型分配规则
- **配置平台规则**：更新 `_config/platform_rules.json` 定义不同平台的发布规范
- **调整品牌声音**：编辑 `_context/brand/Brand_Voice_Guide.md`

---

## 🔒 安全注意事项

1. **`.env` 文件**包含 API 密钥，已加入 `.gitignore`，不会提交到版本控制
2. **不要**将 API Key 硬编码在任何代码文件中
3. **如果**密钥泄露，立即到相应平台重置
4. **生成内容的版权**遵循各 LLM 服务商的使用条款

---

## 🐛 问题反馈 & 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

<div align="center">
Made with ❤️ by SEO/GEO Team<br>
Build your growth with AI automation 🚀
</div>
