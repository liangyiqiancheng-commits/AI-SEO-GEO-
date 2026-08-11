#!/usr/bin/env python3
"""工具网关 - 统一调用第三方 API"""
import os, json, sys, requests
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent.parent / "_config"
REGISTRY_FILE = CONFIG_DIR / "tools_registry.json"
ENV_FILE = CONFIG_DIR / ".env"

def load_env():
    env_vars = {}
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip('"').strip("'")
    return env_vars

def load_registry():
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def call(tool_id: str, params: dict) -> dict:
    registry = load_registry()
    env_vars = load_env()
    tool_config = next((t for t in registry["tools"] if t["tool_id"] == tool_id), None)
    if not tool_config:
        return {"error": f"未找到工具: {tool_id}"}
    api_key = env_vars.get(tool_config.get("env_key", "")) if tool_config.get("env_key") else None
    if not api_key and tool_config.get("api_source") != "local":
        return {"error": f"缺少 API Key: {tool_config.get('env_key')}"}
    try:
        if tool_id == "firecrawl_scrape":
            return _firecrawl(tool_config, api_key, params)
        elif tool_id == "serper_search":
            return _serper(tool_config, api_key, params)
        elif tool_id == "pagespeed_insights":
            return _pagespeed(tool_config, api_key, params)
        elif tool_id == "perplexity_factcheck":
            return _perplexity(tool_config, api_key, params)
        elif tool_id == "gemini_quality":
            return _gemini(tool_config, api_key, params)
        elif tool_id == "playwright_screenshot":
            return _playwright(params)
        else:
            return {"error": f"未实现: {tool_id}"}
    except Exception as e:
        return {"error": str(e)}

def _firecrawl(c, key, p):
    r = requests.post(c["endpoint"], json={"url": p.get("url"), "formats": ["markdown"]},
                      headers={"Authorization": f"Bearer {key}"}, timeout=30)
    return r.json()

def _serper(c, key, p):
    r = requests.post(c["endpoint"], json={"q": p.get("query", p.get("url", "")), "num": 10},
                      headers={"X-API-KEY": key}, timeout=30)
    return r.json()

def _pagespeed(c, key, p):
    r = requests.get(c["endpoint"], params={"url": p.get("url"), "strategy": "DESKTOP", "key": key}, timeout=30)
    return r.json()

def _perplexity(c, key, p):
    r = requests.post(c["endpoint"], json={"model": "sonar", "messages": [{"role": "user", "content": p.get("query", "")}]},
                      headers={"Authorization": f"Bearer {key}"}, timeout=60)
    return r.json()

def _gemini(c, key, p):
    url = c["endpoint"].replace(":generateContent", "") + f":generateContent?key={key}"
    r = requests.post(url, json={"contents": [{"parts": [{"text": p.get("prompt", "")}]}]}, timeout=60)
    return r.json()

def _playwright(p):
    import subprocess
    url, out = p.get("url"), p.get("output", "output/audit/screenshot.png")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["npx", "playwright", "screenshot", "--full-page", url, out],
                       capture_output=True, timeout=60)
    return {"success": r.returncode == 0, "output": out} if r.returncode == 0 else {"error": r.stderr.decode()}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tool_gateway.py <tool_id> '<params_json>'")
        sys.exit(1)
    print(json.dumps(call(sys.argv[1], json.loads(sys.argv[2])), ensure_ascii=False, indent=2))
