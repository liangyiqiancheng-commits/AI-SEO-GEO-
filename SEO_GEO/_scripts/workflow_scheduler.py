#!/usr/bin/env python3
"""
工作流调度器 - 解析 Workflow JSON，按顺序执行 Skills 和 Tools
"""
import json
import sys
import time
from pathlib import Path

WORKFLOW_DIR = Path(__file__).parent.parent / "_workflow" / "flow_json"
CONFIG_DIR = Path(__file__).parent.parent / "_config"
TOOLS_GATEWAY = Path(__file__).parent.parent / "_tools" / "gateway" / "tool_gateway.py"
ROUTER = Path(__file__).parent.parent / "_router" / "gateway" / "model_router.py"


def load_workflow(flow_id: str) -> dict:
    index = json.load(open(CONFIG_DIR / "workflow_index.json"))
    for wf in index["workflows"]:
        if wf["flow_id"] == flow_id:
            with open(WORKFLOW_DIR / wf["file"], "r", encoding="utf-8") as f:
                return json.load(f)
    return None


def execute_step(step: dict, params: dict) -> dict:
    """执行单个步骤"""
    start = time.time()

    # 处理模板变量
    def resolve(val):
        if isinstance(val, str) and val.startswith("{{") and val.endswith("}}"):
            key = val[2:-2].strip()
            return params.get(key, val)
        return val

    resolved_step = {}
    for k, v in step.items():
        if isinstance(v, str):
            resolved_step[k] = resolve(v)
        elif isinstance(v, dict):
            resolved_step[k] = {rk: resolve(rv) for rk, rv in v.items()}
        else:
            resolved_step[k] = v

    # 执行工具或技能
    if "tool" in resolved_step:
        import subprocess
        tool_id = resolved_step["tool"]
        tool_params = json.dumps(resolved_step.get("params", {}), ensure_ascii=False)
        result = subprocess.run(
            ["python", str(TOOLS_GATEWAY), tool_id, tool_params],
            capture_output=True, text=True, timeout=60
        )
        try:
            output = json.loads(result.stdout)
        except:
            output = {"raw": result.stdout, "error": result.stderr}
    elif "skill" in resolved_step:
        # 技能执行（简化版：输出计划）
        skill_id = resolved_step["skill"]
        output = {"skill": skill_id, "params": resolved_step.get("params", {}), "status": "executed"}
    else:
        output = {"error": "未知步骤类型"}

    duration = time.time() - start
    return {**output, "duration_ms": int(duration * 1000)}


def run_workflow(flow_id: str, url: str = None) -> dict:
    """运行工作流"""
    workflow = load_workflow(flow_id)
    if not workflow:
        return {"error": f"未找到工作流: {flow_id}"}

    params = {"url": url} if url else {}
    results = []

    for step in workflow.get("steps", []):
        result = execute_step(step, params)
        results.append(result)
        if result.get("error"):
            results.append({"warning": f"步骤中止: {result['error']}"})
            break

    return {
        "flow_id": flow_id,
        "status": "completed" if not results[-1].get("error") else "partial",
        "steps": results
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python workflow_scheduler.py <flow_id> [url]")
        sys.exit(1)
    flow_id = sys.argv[1]
    url = sys.argv[2] if len(sys.argv) > 2 else None
    result = run_workflow(flow_id, url)
    print(json.dumps(result, ensure_ascii=False, indent=2))
