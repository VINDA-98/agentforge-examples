from __future__ import annotations

from dataclasses import dataclass

from workflow_steps import analyze_request, assess_risk, build_plan, load_templates


@dataclass
class StepRecord:
    name: str
    status: str
    detail: str


@dataclass
class WorkflowResult:
    status: str
    summary: str
    next_action: str
    plan: list[str]
    steps: list[StepRecord]


class WorkflowAgent:
    def __init__(self, template_path: str):
        self.template_path = template_path
        self.templates = load_templates(template_path)

    def run(self, request: str) -> WorkflowResult:
        steps: list[StepRecord] = []
        context = analyze_request(request, self.templates)
        audience = context["audience"] or "未提供"
        deadline = context["deadline"] or "未提供"

        steps.append(
            StepRecord(
                name="收集需求",
                status="completed",
                detail=(
                    f"已识别任务类型：{context['task_label']}；"
                    f"目标人群：{audience}；截止时间：{deadline}。"
                ),
            )
        )

        risk_notes = assess_risk(request)
        if risk_notes:
            plan = build_plan(context, self.templates)
            steps.append(
                StepRecord(
                    name="生成计划",
                    status="completed",
                    detail=f"已生成 {len(plan)} 条执行任务。",
                )
            )
            steps.append(
                StepRecord(
                    name="风险检查",
                    status="warning",
                    detail=f"检测到风险：{'、'.join(risk_notes)}。",
                )
            )
            steps.append(
                StepRecord(
                    name="人工确认",
                    status="pending",
                    detail="即使信息不完整，也不建议自动继续执行高风险请求。",
                )
            )
            return WorkflowResult(
                status="needs_human_review",
                summary="流程已经生成基础计划，但高风险步骤必须人工复核。",
                next_action="请先由负责人确认风险和回滚方案，再继续执行。",
                plan=plan,
                steps=steps,
            )

        missing_fields = list(context["missing_fields"])
        if missing_fields:
            steps.append(
                StepRecord(
                    name="补充信息",
                    status="waiting",
                    detail=f"还缺少：{', '.join(missing_fields)}。",
                )
            )
            return WorkflowResult(
                status="needs_info",
                summary="信息还不够完整，暂时不能继续生成可靠计划。",
                next_action=f"请先补充：{', '.join(missing_fields)}。",
                plan=[],
                steps=steps,
            )

        plan = build_plan(context, self.templates)
        steps.append(
            StepRecord(
                name="生成计划",
                status="completed",
                detail=f"已生成 {len(plan)} 条执行任务。",
            )
        )

        steps.append(
            StepRecord(
                name="风险检查",
                status="completed",
                detail="没有发现必须人工复核的高风险关键词。",
            )
        )
        steps.append(
            StepRecord(
                name="输出结果",
                status="completed",
                detail="计划已经整理完成，可以直接执行。",
            )
        )
        return WorkflowResult(
            status="ready",
            summary="工作流已完成任务拆解和风险检查。",
            next_action="直接按计划推进，并把每一步落到你的任务系统中。",
            plan=plan,
            steps=steps,
        )
