#!/usr/bin/env python3
"""资产同步 - 将高频片段存入缓存供后续复用"""
import json
import hashlib
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / "_cache" / "reuse_fragments"
CONTEXT_DIR = Path(__file__).parent.parent / "_context"


def hash_content(content: str) -> str:
    return hashlib.md5(content.encode()).hexdigest()[:8]


def sync_brand_fragments():
    """同步品牌片段"""
    brand_dir = CONTEXT_DIR / "brand"
    if not brand_dir.exists():
        return []
    synced = []
    for f in brand_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8")
        frag_id = f"brand_{f.stem}_{hash_content(content)}"
        frag_file = CACHE_DIR / f"{frag_id}.json"
        if not frag_file.exists():
            frag_file.write_text(json.dumps({
                "id": frag_id,
                "type": "brand",
                "source": str(f.relative_to(Path(__file__).parent.parent)),
                "content": content[:500] + "..." if len(content) > 500 else content
            }, ensure_ascii=False, indent=2))
            synced.append(frag_id)
    return synced


def sync_style_fragments():
    """同步风格片段"""
    style_file = Path(__file__).parent.parent / "_blocks" / "style" / "STYLE-GUIDE.md"
    if not style_file.exists():
        return []
    content = style_file.read_text(encoding="utf-8")
    frag_id = f"style_guide_{hash_content(content)}"
    frag_file = CACHE_DIR / f"{frag_id}.json"
    if not frag_file.exists():
        frag_file.write_text(json.dumps({
            "id": frag_id,
            "type": "style",
            "content": content
        }, ensure_ascii=False))
        return [frag_id]
    return []


if __name__ == "__main__":
    brand = sync_brand_fragments()
    style = sync_style_fragments()
    print(f"同步完成: 品牌 {len(brand)} 个, 风格 {len(style)} 个")
