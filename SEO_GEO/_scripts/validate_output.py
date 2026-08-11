#!/usr/bin/env python3
"""输出验证 - 检查产出文件是否符合规范"""
import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "output"


def validate_blog(filepath: str) -> dict:
    """验证博客文章"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    issues = []
    if len(content) < 1500:
        issues.append(f"字数不足: {len(content)} < 1500")
    if "##" not in content:
        issues.append("缺少 H2 标题")
    if "FAQ" not in content.upper():
        issues.append("缺少 FAQ 章节")
    return {"valid": len(issues) == 0, "issues": issues}


def validate_schema(filepath: str) -> dict:
    """验证 Schema JSON"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "@context" not in data:
            return {"valid": False, "issues": ["缺少 @context"]}
        return {"valid": True, "issues": []}
    except Exception as e:
        return {"valid": False, "issues": [str(e)]}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python validate_output.py <file_path>")
        sys.exit(1)
    filepath = sys.argv[1]
    if filepath.endswith(".json") and "schema" in filepath:
        result = validate_schema(filepath)
    else:
        result = validate_blog(filepath)
    print(json.dumps(result, ensure_ascii=False, indent=2))
