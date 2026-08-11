【全局MD约束：Token节流 & 高命中规则】
## Skill: mockup_gen
- 触发关键词：`screenshot`
- 适用场景：使用 Playwright 截取网页全屏 PNG
- 输入参数：{"url": "https://example.com", "output_path": "output/audit/screenshot.png"}
- 工作流步骤：
  1. 读取 _config/tools_registry.json 获取 Playwright 配置
  2. 调用 tool_gateway.py 执行 playwright_screenshot
  3. 等待页面加载完成，截取全屏 PNG
- 质量审核标准：截图清晰，无截断；包含页面主要内容区域
- 产出路径：output/audit/screenshot.png
- 缓存复用标记：无
