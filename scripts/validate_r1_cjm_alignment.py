#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    ".github/ISSUE_TEMPLATE/audit_request.md",
    "commerce/product-card.json",
    "commerce/payment_mandate_template.json",
    "commerce/quote_response_template.json",
    "commerce/base_usdc_audit_invoice_template.json",
    "deliverables/agent_fiscal_autonomy_audit_template.md",
    "deliverables/agent_fiscal_autonomy_audit_summary.schema.json",
    "docs/one-page-offer.md",
    "docs/retention-trigger-map.md",
]

QUALIFICATION_FIELDS = [
    "seller_role",
    "capability_surface",
    "monetization_state",
    "access_control",
    "approval_and_limit_policy",
    "receipt_or_audit_trail",
    "revocation_and_next_threshold",
]

FORBIDDEN_PUBLIC_PATTERNS = [
    r"crypto trading LLM wiki",
    r"monthly operating-cost target",
    r"max loss or risk budget",
    r"desired proof report",
    r"approval_required\"\\s*:\\s*false",
    r"0x1E5E9C09A2946094737724B9B0EAea819581f5d3",
]

PUBLIC_SURFACES = [
    "README.md",
    "docs/index.md",
    "docs/direct-base-usdc.md",
    "docs/plugin-wrapper.md",
    "plugins/agent-fiscal-autonomy-plugin/README.md",
    "plugins/agent-fiscal-autonomy-plugin/references/payment_and_entitlement.md",
    "plugins/agent-fiscal-autonomy-plugin/skills/agent-fiscal-autonomy-onboarding/SKILL.md",
    ".github/ISSUE_TEMPLATE/audit_request.md",
    ".github/ISSUE_TEMPLATE/agent_use_case.md",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        require((ROOT / rel).exists(), f"missing required file: {rel}", failures)

    for rel in [*REQUIRED_FILES, "commerce/catalog.json", "commerce/receipt_schema.json"]:
        if rel.endswith(".json") and (ROOT / rel).exists():
            try:
                json.loads(read(rel))
            except json.JSONDecodeError as exc:
                failures.append(f"invalid JSON in {rel}: {exc}")

    audit_template = read(".github/ISSUE_TEMPLATE/audit_request.md")
    for field in QUALIFICATION_FIELDS:
        require(field.replace("_", " ") in audit_template.lower() or field in audit_template, f"audit template missing {field}", failures)

    quote = json.loads(read("commerce/quote_response_template.json"))
    invoice = json.loads(read("commerce/base_usdc_audit_invoice_template.json"))
    mandate = json.loads(read("commerce/payment_mandate_template.json"))

    require(quote.get("approval_required") is True, "quote approval_required must be true", failures)
    require(quote.get("scope_acceptance_required_before_payment_route") is True, "quote must require scope acceptance", failures)
    require(invoice.get("pay_to_address") == "ISSUED_ONLY_AFTER_SCOPE_ACCEPTANCE", "invoice must not expose public pay_to_address", failures)
    require(mandate.get("status") == "draft_not_payable", "payment mandate must be draft_not_payable", failures)

    for rel in PUBLIC_SURFACES:
        text = read(rel)
        for pattern in FORBIDDEN_PUBLIC_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"forbidden public pattern in {rel}: {pattern}")

    if failures:
        print("R1_CJM_ALIGNMENT_VALIDATION status=FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("R1_CJM_ALIGNMENT_VALIDATION status=PASS")
    print("positioning=agent_fiscal_autonomy_audit")
    print("qualification_gate=seller_side_seven_fields")
    print("payment_route=closed_until_scope_acceptance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
