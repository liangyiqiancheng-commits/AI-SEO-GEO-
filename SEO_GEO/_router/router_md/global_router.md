# 模型路由层说明

## 路由逻辑
1. 读取 `_config/router_registry.json` 获取模型列表和权重
2. 读取 `_config/.env` 获取当前配额使用情况
3. 根据任务复杂度选择模型：
   - **简单任务**（关键词列表、元描述生成）→ 优先 Grok（权重低、成本低）
   - **中等任务**（文章初稿、Schema 生成）→ 优先 GPT-4o
   - **复杂任务**（策略规划、内容润色、多步推理）→ 优先 Claude
4. 若主模型配额超过 `QUOTA_TRIGGER_RATIO`，自动降级到备用模型
5. 所有调用经过 `_router/gateway/model_router.py`

## 配额监控
- 每日调用 `quota_monitor.py` 统计消耗
- 超出月度限额时触发熔断，输出告警
