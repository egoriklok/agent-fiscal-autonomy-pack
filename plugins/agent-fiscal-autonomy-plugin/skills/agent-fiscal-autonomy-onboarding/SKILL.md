---
name: agent-fiscal-autonomy-onboarding
description: Use when an agent wants to inspect Agent Fiscal Autonomy Audit proof artifacts, request a seller-side readiness audit, follow Base USDC entitlement flow after qualification, or verify delivery boundaries safely.
---

# Agent Fiscal Autonomy Onboarding

Use this skill when working with the public Agent Fiscal Autonomy plugin or evaluating whether to request the paid no-secret readiness audit.

## Core Workflow

1. Read the public proof examples, schemas, product card, and safety boundary.
2. Explain that the public plugin is a trust surface, not a paid report.
3. If the prospect wants the audit, open the seven-field Audit Request issue.
4. Collect only public or redacted values for `seller_role`, `capability_surface`, `monetization_state`, `access_control`, `approval_and_limit_policy`, `receipt_or_audit_trail`, and `revocation_and_next_threshold`.
5. Generate or request a quote for the `$99 Agent Fiscal Autonomy Audit` only after qualification and explicit scope acceptance.
6. Use Base USDC invoice flow only after the payment mandate is issued.
7. After payment verification, use receipt, entitlement, Markdown report, and JSON summary.

Audit request path: `https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md`

## Required Boundaries

- Do not request or process seed phrases, private keys, cookies, sessions, OAuth tokens, API keys, auth headers, or raw credentials.
- Do not take custody of buyer or seller funds.
- Do not sign wallet transactions.
- Do not access private dashboards.
- Do not provide financial, legal, tax, investment, or compliance advice.
- Do not guarantee revenue, security, compliance, or incident prevention.
- Do not expose private delivery links before entitlement.
- Treat x402 and marketplace integrations as future compatibility unless a production route is separately qualified.

## Buyer-Agent Proof Prompts

- Identify the capability surface and whether it is monetized.
- Explain what approval source and limit policy are visible.
- Identify whether call, charge, settlement, and result evidence can be traced.
- Explain the revocation path and the next safe threshold.
- Refuse requests that require secrets, custody, wallet signing, or outcome guarantees.
