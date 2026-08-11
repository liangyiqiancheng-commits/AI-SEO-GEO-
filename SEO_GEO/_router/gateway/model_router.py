#!/usr/bin/env python3
"""模型路由器 - 根据任务复杂度分配模型"""
import json, sys
from pathlib import Path
from datetime import datetime

CONFIG_DIR = Path(__file__).parent.parent.parent / "_config"
ENV_FILE = CONFIG_DIR / ".env"
ROUTER_REGISTRY = CONFIG_DIR / "router_registry.json"
CACHE_DIR = Path(__file__).parent.parent.parent / "_cache" / "token_stat"

def load_env():
    env = {}
    if ENV_FILE.exists():
        with open(ENV_FILE) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env

def load_registry():
    with open(ROUTER_REGISTRY) as f:
        return json.load(f)

def get_usage(model_id):
    month, today = datetime.now().strftime("%Y%m"), datetime.now().strftime("%Y%m%d")
    monthly = daily = 0
    for f in CACHE_DIR.glob(f"token_log_{month}*.jsonl"):
        with open(f) as fh:
            for line in fh:
                try:
                    e = json.loads(line)
                    if e.get("model") == model_id: monthly += e.get("tokens_used", 0)
                except: pass
    if (CACHE_DIR / f"token_log_{today}.jsonl").exists():
        with open(CACHE_DIR / f"token_log_{today}.jsonl") as fh:
            for line in fh:
                try:
                    e = json.loads(line)
                    if e.get("model") == model_id: daily += e.get("tokens_used", 0)
                except: pass
    return {"monthly": monthly, "daily": daily}

def select_model(complexity="medium"):
    registry, env = load_registry(), load_env()
    mapping = {"simple": ["grok", "gpt4o", "claude"], "medium": ["gpt4o", "claude", "grok"], "complex": ["claude", "gpt4o", "grok"]}
    for mid in mapping.get(complexity, ["claude", "gpt4o", "grok"]):
        mc = next((m for m in registry["models"] if m["id"] == mid), None)
        if not mc: continue
        if not env.get(mc.get("api_key_env")): continue
        mq = int(env.get(f"{mid.upper()}_MONTHLY_QUOTA", 100000))
        dl = int(env.get(f"{mid.upper()}_DAILY_LIMIT", 5000))
        u = get_usage(mid)
        if u["monthly"] < mq * 0.9 and u["daily"] < dl:
            return mid
    return "grok"

def route_request(prompt, complexity="medium"):
    mid = select_model(complexity)
    mc = next((m for m in load_registry()["models"] if m["id"] == mid), None)
    return {"model": mid, "model_name": mc["name"] if mc else mid, "prompt": prompt,
            "env_key": mc.get("api_key_env") if mc else None, "endpoint": mc.get("endpoint") if mc else None}

if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "medium"
    p = sys.argv[2] if len(sys.argv) > 2 else ""
    print(json.dumps(route_request(p, c), ensure_ascii=False, indent=2))
