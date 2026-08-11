#!/usr/bin/env python3
"""
Token 统计 - 查看各模型消耗和缓存命中率
"""
import json
from pathlib import Path
from datetime import datetime

CACHE_DIR = Path(__file__).parent.parent / "_cache" / "token_stat"
CONFIG_DIR = Path(__file__).parent.parent / "_config"


def get_token_stats():
    """获取 Token 统计"""
    stats = {}
    today = datetime.now().strftime("%Y%m%d")
    month = datetime.now().strftime("%Y%m")

    for log_file in CACHE_DIR.glob("token_log_*.jsonl"):
        model = None
        daily = 0
        monthly = 0
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    m = entry.get("model")
                    t = entry.get("tokens_used", 0)
                    if m:
                        if m not in stats:
                            stats[m] = {"daily": 0, "monthly": 0}
                        stats[m]["daily"] += t
                        stats[m]["monthly"] += t
                except:
                    pass

    return stats


def get_cache_stats():
    """获取缓存统计"""
    reuse_dir = Path(__file__).parent.parent / "_cache" / "reuse_fragments"
    files = list(reuse_dir.glob("*.json")) if reuse_dir.exists() else []
    return {"cached_fragments": len(files)}


def print_status():
    """打印状态"""
    token_stats = get_token_stats()
    cache_stats = get_cache_stats()

    print("\n=== Token 消耗统计 ===\n")
    if token_stats:
        for model, s in token_stats.items():
            print(f"{model}: 日 {s['daily']}, 月 {s['monthly']}")
    else:
        print("暂无数据（首次运行后开始记录）")

    print(f"\n=== 缓存统计 ===\n")
    print(f"已缓存片段: {cache_stats['cached_fragments']}")
    print()


if __name__ == "__main__":
    print_status()
