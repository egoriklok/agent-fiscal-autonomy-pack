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
    "commerce/payable_surface_remediation_reference.json",
    "examples/payable_surface_remediation_vectors_v1.json",
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
    r"\bUSDT\b",
]

PUBLIC_SURFACES = [
    "README.md",
    "docs/index.md",
    "docs/direct-base-usdc.md",
    "docs/plugin-wrapper.md",
    "docs/portfolio-r1-ru.md",
    "docs/portfolio-r1-ru.html",
    "plugins/agent-fiscal-autonomy-plugin/README.md",
    "plugins/agent-fiscal-autonomy-plugin/references/payment_and_entitlement.md",
    "plugins/agent-fiscal-autonomy-plugin/skills/agent-fiscal-autonomy-onboarding/SKILL.md",
    ".github/ISSUE_TEMPLATE/audit_request.md",
    ".github/ISSUE_TEMPLATE/agent_use_case.md",
]

OPERATOR_DISCLOSURE_SURFACES = [
    "README.md",
    "docs/index.md",
]

OPERATOR_DISCLOSURE = (
    "This offer and outreach are operated by Hermes Agent, an AI agent "
    "working for owner/operator @egoriklok."
)

REMEDIATION_REQUIRED_FIELDS = {
    "limit_policy.policy_id",
    "limit_policy.subject_id",
    "limit_policy.asset",
    "limit_policy.asset_decimals",
    "limit_policy.amount_limit_minor",
    "limit_policy.window_type",
    "limit_policy.window_seconds",
    "limit_policy.window_started_at",
    "limit_policy.window_ends_at",
    "limit_policy.usage_before_minor",
    "limit_policy.usage_after_minor",
    "idempotency.idempotency_key",
    "idempotency.key_scope",
    "idempotency.request_hash",
    "idempotency.retention_until",
    "receipt.receipt_id",
    "receipt.intent_id",
    "receipt.idempotency_key",
    "receipt.payment_reference",
    "receipt.tx_hash",
    "receipt.amount_minor",
    "receipt.asset",
    "receipt.created_at",
    "finality.chain_id",
    "finality.status",
    "finality.mode",
    "finality.confirmations_observed",
    "finality.confirmations_required",
    "finality.block_number",
    "finality.block_hash",
    "finality.checked_at",
    "reorg.status",
    "reorg.detected_at",
    "reorg.orphaned_block_hash",
    "reorg.replacement_tx_hash",
    "reorg.reconciliation_id",
    "reorg.retry_policy",
}

REMEDIATION_CHECK_IDS = {
    "CAP-001",
    "IDEM-001",
    "IDEM-002",
    "RECEIPT-001",
    "FINALITY-001",
    "REORG-001",
}

FINALITY_IDENTITY_EVIDENCE = {
    "receipt.receipt_id",
    "receipt.payment_reference",
    "receipt.tx_hash",
    "finality.chain_id",
    "finality.block_hash",
}

REORG_IDENTITY_EVIDENCE = {
    "receipt.receipt_id",
    "receipt.payment_reference",
    "receipt.tx_hash",
    "finality.chain_id",
    "finality.block_hash",
    "reorg.orphaned_block_hash",
    "reorg.reconciliation_id",
}

DELIVERY_TARGET_PLACEHOLDER = "SET_FROM_ACCEPTED_SCOPE_BEFORE_PAYMENT"
PAYMENT_ROUTE_PLACEHOLDER = "ISSUED_ONLY_AFTER_SCOPE_ACCEPTANCE"
DELIVERY_TARGET_PRECONDITION = "exact_delivery_target_set_from_accepted_scope"


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

    require(quote.get("schema_version") == "quote-response-v3", "quote schema version must be v3", failures)
    require(invoice.get("schema_version") == "base-usdc-invoice-v3", "invoice schema version must be v3", failures)
    require(mandate.get("schema_version") == "payment-mandate-v2", "mandate schema version must be v2", failures)
    require(quote.get("approval_required") is True, "quote approval_required must be true", failures)
    require(quote.get("scope_acceptance_required_before_payment_route") is True, "quote must require scope acceptance", failures)
    require(invoice.get("pay_to_address") == "ISSUED_ONLY_AFTER_SCOPE_ACCEPTANCE", "invoice must not expose public pay_to_address", failures)
    require(mandate.get("status") == "draft_not_payable", "payment mandate must be draft_not_payable", failures)
    require(
        DELIVERY_TARGET_PRECONDITION in mandate.get("required_preconditions", []),
        "payment mandate must require the exact delivery target before opening the payment route",
        failures,
    )
    for label, artifact in (("quote", quote), ("invoice", invoice), ("mandate", mandate)):
        require(
            artifact.get("delivery_target_mode")
            == "evidence_derived_exact_target_before_payment",
            f"{label} must use an evidence-derived exact delivery target",
            failures,
        )
        require(
            artifact.get("delivery_target_required_before_payment") is True,
            f"{label} must require the exact delivery target before payment",
            failures,
        )
        require(
            artifact.get("fixed_delivery_wait_hours") is None,
            f"{label} must not impose a fixed delivery wait",
            failures,
        )
        require(
            "delivery_sla_hours_after_verified_payment" not in artifact,
            f"{label} still contains the retired fixed delivery SLA",
            failures,
        )
        payment_route = artifact.get("pay_to_address", artifact.get("payee"))
        if payment_route not in (None, "", PAYMENT_ROUTE_PLACEHOLDER):
            require(
                bool(artifact.get("delivery_target"))
                and artifact.get("delivery_target") != DELIVERY_TARGET_PLACEHOLDER,
                f"issued {label} must set an exact delivery target before exposing a payment route",
                failures,
            )

    for rel in PUBLIC_SURFACES:
        text = read(rel)
        for pattern in FORBIDDEN_PUBLIC_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"forbidden public pattern in {rel}: {pattern}")

    for rel in OPERATOR_DISCLOSURE_SURFACES:
        text = read(rel)
        require(
            OPERATOR_DISCLOSURE in text,
            f"operator disclosure missing in {rel}",
            failures,
        )

    remediation_path = ROOT / "commerce/payable_surface_remediation_reference.json"
    vectors_path = ROOT / "examples/payable_surface_remediation_vectors_v1.json"
    if remediation_path.exists() and vectors_path.exists():
        remediation = json.loads(remediation_path.read_text(encoding="utf-8"))
        vectors = json.loads(vectors_path.read_text(encoding="utf-8"))

        require(
            remediation.get("artifact_role") == "remediation_reference_only",
            "payable-surface contract must be remediation_reference_only",
            failures,
        )
        require(
            remediation.get("third_party_conformance") == "unverified",
            "payable-surface contract must not claim third-party conformance",
            failures,
        )
        require(
            "does not claim" in remediation.get("not_a_claim", "").lower(),
            "payable-surface contract needs an explicit third-party non-claim",
            failures,
        )
        require(
            set(remediation.get("required_provider_fields", []))
            == REMEDIATION_REQUIRED_FIELDS,
            "payable-surface contract required_provider_fields drifted",
            failures,
        )

        checks = remediation.get("acceptance_checks", [])
        check_ids = {check.get("check_id") for check in checks}
        require(
            check_ids == REMEDIATION_CHECK_IDS,
            "payable-surface acceptance check IDs drifted",
            failures,
        )
        for check in checks:
            require(
                bool(check.get("pass_condition"))
                and bool(check.get("required_evidence")),
                f"payable-surface check {check.get('check_id')} lacks exact pass evidence",
                failures,
            )
        checks_by_id = {check.get("check_id"): check for check in checks}
        require(
            FINALITY_IDENTITY_EVIDENCE.issubset(
                set(checks_by_id.get("FINALITY-001", {}).get("required_evidence", []))
            ),
            "FINALITY-001 must require receipt, transaction, chain and block identity",
            failures,
        )
        require(
            REORG_IDENTITY_EVIDENCE.issubset(
                set(checks_by_id.get("REORG-001", {}).get("required_evidence", []))
            ),
            "REORG-001 must require receipt, transaction, chain, block and reconciliation identity",
            failures,
        )

        require(
            vectors.get("reference_contract")
            == "commerce/payable_surface_remediation_reference.json",
            "payable-surface vectors reference the wrong contract",
            failures,
        )
        require(
            vectors.get("third_party_conformance") == "unverified",
            "payable-surface vectors must not claim third-party conformance",
            failures,
        )
        vector_ids = {
            vector.get("vector_id") for vector in vectors.get("vectors", [])
        }
        require(
            vector_ids == REMEDIATION_CHECK_IDS,
            "payable-surface test vector IDs drifted",
            failures,
        )
        for vector in vectors.get("vectors", []):
            require(
                bool(vector.get("given"))
                and bool(vector.get("when"))
                and bool(vector.get("expect")),
                f"payable-surface vector {vector.get('vector_id')} is incomplete",
                failures,
            )

        vectors_by_id = {
            vector.get("vector_id"): vector
            for vector in vectors.get("vectors", [])
        }
        cap_expect = vectors_by_id.get("CAP-001", {}).get("expect", {})
        require(
            cap_expect.get("statuses")
            == ["accepted", "accepted", "limit_exceeded"]
            and cap_expect.get("third_request_charged") is False
            and cap_expect.get("settlement_count") == 2,
            "CAP-001 must prove an uncharged over-limit rejection",
            failures,
        )
        replay_expect = vectors_by_id.get("IDEM-001", {}).get("expect", {})
        require(
            len(set(replay_expect.get("receipt_ids", []))) == 1
            and len(set(replay_expect.get("payment_references", []))) == 1
            and len(set(replay_expect.get("tx_hashes", []))) == 1
            and replay_expect.get("settlement_count") == 1,
            "IDEM-001 must prove stable evidence and one settlement",
            failures,
        )
        conflict_expect = vectors_by_id.get("IDEM-002", {}).get("expect", {})
        require(
            conflict_expect.get("second_http_status") == 409
            and conflict_expect.get("second_error_code") == "idempotency_conflict"
            and conflict_expect.get("second_request_charged") is False
            and conflict_expect.get("settlement_count") == 1,
            "IDEM-002 must prove conflict without another charge",
            failures,
        )
        receipt_expect = vectors_by_id.get("RECEIPT-001", {}).get("expect", {})
        require(
            receipt_expect.get("unique_receipt_id_count") == 1
            and len(set(receipt_expect.get("receipt_ids", []))) == 1,
            "RECEIPT-001 must prove one stable receipt ID",
            failures,
        )
        finality_expect = vectors_by_id.get("FINALITY-001", {}).get("expect", {})
        finality_given = vectors_by_id.get("FINALITY-001", {}).get("given", {})
        finality_when = vectors_by_id.get("FINALITY-001", {}).get("when", [])
        require(
            finality_expect.get("statuses") == ["pending", "finalized"]
            and finality_expect.get("fulfillment_allowed") == [False, True]
            and finality_expect.get("receipt_ids")
            == [finality_given.get("receipt_id")] * 2
            and finality_expect.get("payment_references")
            == [finality_given.get("payment_reference")] * 2
            and finality_expect.get("tx_hashes")
            == [finality_given.get("tx_hash")] * 2
            and finality_expect.get("chain_ids")
            == [finality_given.get("chain_id")] * 2
            and finality_expect.get("block_hashes")
            == [finality_given.get("block_hash")] * 2
            and finality_expect.get("canonical_transaction_inclusion")
            == [True, True]
            and len(finality_when) == 2
            and all(
                observation.get("canonical_block_hash_matches") is True
                and observation.get("canonical_transaction_inclusion_matches")
                is True
                for observation in finality_when
            ),
            "FINALITY-001 must bind declared finality to one receipt, transaction, chain and block",
            failures,
        )
        reorg_expect = vectors_by_id.get("REORG-001", {}).get("expect", {})
        reorg_given = vectors_by_id.get("REORG-001", {}).get("given", {})
        reorg_when = vectors_by_id.get("REORG-001", {}).get("when", [])
        require(
            reorg_expect.get("reorg_status") == "reorg_detected"
            and reorg_expect.get("fulfillment_allowed") is False
            and reorg_expect.get("revenue_recognition_allowed") is False
            and reorg_expect.get("automatic_second_charge") is False
            and reorg_expect.get("reconciliation_id_required") is True
            and bool(reorg_expect.get("reconciliation_id"))
            and reorg_expect.get("chain_id") == reorg_given.get("chain_id")
            and reorg_expect.get("receipt_id") == reorg_given.get("receipt_id")
            and reorg_expect.get("payment_reference")
            == reorg_given.get("payment_reference")
            and reorg_expect.get("tx_hash") == reorg_given.get("tx_hash")
            and reorg_expect.get("orphaned_block_hash")
            == reorg_given.get("observed_block_hash")
            and len(reorg_when) == 1
            and reorg_when[0].get("chain_id") == reorg_given.get("chain_id")
            and reorg_when[0].get("receipt_id") == reorg_given.get("receipt_id")
            and reorg_when[0].get("tx_hash") == reorg_given.get("tx_hash")
            and reorg_when[0].get("orphaned_block_hash")
            == reorg_given.get("observed_block_hash"),
            "REORG-001 must fail closed and bind reconciliation to the orphaned payment identity",
            failures,
        )

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
