#!/usr/bin/env python3
"""
路由告警 - 配额超限时触发飞书/邮件告警
"""
import json
import os
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent.parent / "_config"
ENV_FILE = CONFIG_DIR / ".env"


def load_env():
    env_vars = {}
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key, val = line.split("=", 1)
                        env_vars[key.strip()] = val.strip().strip('"').strip("'")
    return env_vars


def send_alarm(model: str, message: str):
    """发送告警（支持飞书/Webhook）"""
    registry = json.load(open(CONFIG_DIR / "router_registry.json"))
    webhook = registry.get("alarm_webhook", "")
    if not webhook:
        print(f"[ALARM] {model}: {message}")
        return
    import requests
    requests.post(webhook, json={"text": f"[SEO/GEO Router] {model}: {message}"})


def check_and_alarm():
    """检查配额并触发告警"""
    from quota_monitor import check_quotas
    results = check_quotas()
    for r in results:
        if r["status"] == "exceeded":
            send_alarm(r["model"], f"配额已耗尽: 月度 {r['monthly_ratio']*100:.0f}%, 每日 {r['daily_ratio']*100:.0f}%")
        elif r["status"] == "warning":
            send_alarm(r["model"], f"配额接近上限: 月度 {r['monthly_ratio']*100:.0f}%, 每日 {r['daily_ratio']*100:.0f}%")


if __name__ == "__main__":
    check_and_alarm()
