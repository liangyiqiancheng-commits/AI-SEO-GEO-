#!/usr/bin/env python3
"""批次导出 - 批量导出产出物"""
import json
from pathlib import Path
import subprocess

OUTPUT_DIR = Path(__file__).parent.parent / "output"


def export_all():
    """导出所有产出物"""
    results = {}
    for category in ["audit", "strategy", "content", "reports", "dashboard"]:
        cat_dir = OUTPUT_DIR / category
        if cat_dir.exists():
            files = list(cat_dir.glob("*"))
            results[category] = [str(f.relative_to(OUTPUT_DIR)) for f in files]
    return results


def export_pdf_report():
    """导出 PDF 报告"""
    content_dir = OUTPUT_DIR / "content"
    audit_dir = OUTPUT_DIR / "audit"
    files = []
    if content_dir.exists():
        files.extend(content_dir.glob("*.md"))
    if audit_dir.exists():
        files.extend(audit_dir.glob("*.md"))
    return [str(f) for f in files]


if __name__ == "__main__":
    result = export_all()
    print(json.dumps(result, ensure_ascii=False, indent=2))
