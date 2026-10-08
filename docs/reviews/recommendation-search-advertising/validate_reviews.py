#!/usr/bin/env python3
"""检查交付结构与冻结版本；不代替评审证据的人工核查。"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKTREE = ROOT.parents[2]
DIMENSIONS = {
    "结构与文字表述", "图表呈现", "内容与论证正确性", "全面性与无偏性",
    "演进脉络", "分类整理", "深度理解与洞察",
}
VERDICTS = {"通过", "部分通过", "不通过", "无法核验"}
CONFIDENCE = {"高", "中", "低"}


def inspect_review(task):
    directory = ROOT / task["directory"]
    absent = [name for name in ("workbook.md", "report.md", "findings.json")
              if not (directory / name).is_file()]
    if absent:
        return {"review": task["directory"], "state": "pending", "missing": absent}
    errors = []
    try:
        data = json.loads((directory / "findings.json").read_text())
    except (ValueError, OSError) as exc:
        return {"review": task["directory"], "state": "invalid", "errors": [str(exc)]}
    for key, expected in (("chapter", task["chapter"]), ("reviewer", task["role"]),
                          ("reading_complete", True), ("search_performed", True)):
        if data.get(key) != expected:
            errors.append(f"{key}: {data.get(key)!r}，期望{expected!r}")
    dimensions = data.get("dimensions", [])
    if len(dimensions) != 7 or {d.get("dimension") for d in dimensions} != DIMENSIONS:
        errors.append("七维字段不完整或不一致")
    for dimension in dimensions:
        if dimension.get("verdict") not in VERDICTS:
            errors.append(f"非法结论：{dimension}")
        if dimension.get("confidence") not in CONFIDENCE:
            errors.append(f"非法置信度：{dimension}")
        if dimension.get("verdict") == "无法核验" and dimension.get("confidence") != "低":
            errors.append("无法核验必须使用低置信度")
        if not dimension.get("evidence") or "limitations" not in dimension:
            errors.append(f"维度缺证据或限制：{dimension.get('dimension')}")
    ids = []
    for finding in data.get("findings", []):
        ids.append(finding.get("id"))
        for key in ("id", "severity", "dimensions", "location", "quote", "issue",
                    "evidence", "impact", "recommendation", "status"):
            if not finding.get(key):
                errors.append(f"{finding.get('id')}缺{key}")
        if finding.get("severity") not in {"阻断性", "主要", "次要"}:
            errors.append(f"{finding.get('id')}严重程度非法")
        if finding.get("status") not in {"已核实问题", "证据缺口", "建议增强"}:
            errors.append(f"{finding.get('id')}状态非法")
        if not set(finding.get("dimensions", [])) <= DIMENSIONS:
            errors.append(f"{finding.get('id')}维度名称非法")
        location = finding.get("location", {})
        source = location.get("file") if isinstance(location, dict) else None
        if not source or not (WORKTREE / source).is_file():
            errors.append(f"{finding.get('id')}位置文件不存在：{source}")
        if not isinstance(location, dict) or not location.get("lines"):
            errors.append(f"{finding.get('id')}缺少定位行号")
    if len(ids) != len(set(ids)):
        errors.append("发现ID重复")
    for name in ("workbook.md", "report.md"):
        if not (directory / name).read_text().strip():
            errors.append(f"{name}为空")
    if not data.get("sources"):
        errors.append("没有外部来源记录")
    if "limitations" not in data:
        errors.append("没有核验限制字段")
    workbook = (directory / "workbook.md").read_text()
    for field in ("同级职责", "论证链"):
        if field not in workbook:
            errors.append(f"底稿未找到{field}")
    report_rows = {}
    for line in (directory / "report.md").read_text().splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip().strip("*`").strip()
                 for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0] in DIMENSIONS:
            report_rows.setdefault(cells[0], []).append(tuple(cells[1:3]))
    for dimension in dimensions:
        name = dimension.get("dimension")
        expected = (dimension.get("verdict"), dimension.get("confidence"))
        if report_rows.get(name) != [expected]:
            errors.append(f"报告与JSON的维度判断不一致或不唯一：{name}")
    return {
        "review": task["directory"], "state": "invalid" if errors else "ready",
        "findings": len(ids), "dimensions": len(dimensions), "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--complete", action="store_true")
    parser.add_argument("--hashes", action="store_true")
    args = parser.parse_args()
    registry = json.loads((ROOT / "task-registry.json").read_text())
    tasks = registry["tasks"]
    registry_errors = []
    expected = {(f"{chapter:02d}", role) for chapter in range(1, 11) for role in "abc"}
    if len(tasks) != 30 or {(t["chapter"], t["role"]) for t in tasks} != expected:
        registry_errors.append("注册表未恰好覆盖十章各a/b/c三个角色")
    agent_ids = [t["agent_run_id"] for t in tasks if t.get("agent_run_id")]
    if len(agent_ids) != len(set(agent_ids)):
        registry_errors.append("不同任务复用了同一代理ID")
    if args.complete and (len(agent_ids) != 30 or any(
            t["status"] not in {"completed", "delivered"} for t in tasks)):
        registry_errors.append("尚未登记三十个独立代理的完成/交付状态")
    rows = [inspect_review(task) for task in tasks]
    changes = []
    checked_hashes = 0
    if args.hashes:
        manifest = json.loads((ROOT / "manifest.json").read_text())
        checked_hashes = len(manifest["files"])
        for name, digest in manifest["files"].items():
            path = WORKTREE / name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                changes.append(name)
    result = {
        "ready": sum(row["state"] == "ready" for row in rows),
        "delivered_artifacts": sum(
            (ROOT / task["directory"] / name).is_file()
            for task in tasks for name in ("workbook.md", "report.md", "findings.json")),
        "checked_dimensions": sum(row.get("dimensions", 0) for row in rows),
        "checked_frozen_files": checked_hashes,
        "total": len(rows), "changed_frozen_files": changes, "reviews": rows,
        "registered_agents": len(agent_ids), "registry_errors": registry_errors,
        "note": "ready仅代表交付结构完整；原文、来源层级、底稿和判断仍需人工复核。",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return bool(changes or registry_errors or any(row["state"] == "invalid" for row in rows)
                or (args.complete and result["ready"] != 30))


if __name__ == "__main__":
    raise SystemExit(main())
