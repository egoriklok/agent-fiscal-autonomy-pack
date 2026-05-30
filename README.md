# Agent Fiscal Autonomy Audit

Public no-secret readiness snapshots for payable MCP/API services, agent tools, and other agent spend surfaces. The fixed paid offer is a `$99 Agent Fiscal Autonomy Audit` after explicit scope acceptance and seven-field qualification.

This repo is the public trust surface for the audit. It helps a seller, builder, or buyer agent check whether an agent-facing capability is scoped, approved, logged, revocable, and ready for safer monetization or spend expansion.

## What This Is

The audit is a bounded readiness review for teams exposing APIs, MCP tools, datasets, SaaS workflows, or wallet/credit flows to AI agents.

It focuses on:

- authority and approval boundaries;
- pricing, payment, or quota surface clarity;
- spend limits and escalation thresholds;
- receipt, settlement, and audit-trail evidence;
- revocation, key rotation, or access-reduction paths;
- the next safe threshold for limited production use.

## What This Is Not

- Not financial, legal, tax, investment, or compliance advice.
- No guaranteed revenue, security, compliance, or incident prevention.
- No custody of buyer or seller funds.
- No wallet signing, private key, seed phrase, cookie, session, OAuth token, or API key handling.
- No direct live trading, exchange order placement, or private dashboard access.
- No payment route before explicit scope acceptance and qualification.

## Free Snapshot

The free public snapshot is intentionally small:

- public evidence links only;
- readiness status: `Ready`, `Partial`, or `Blocked`;
- three no-secret blind spots;
- one concrete next scope question.

The snapshot is not an invoice, not a payment request, and not a delivery artifact.

## Paid Offer

The paid entry offer is a fixed-scope `$99 Agent Fiscal Autonomy Audit`.

Payment rail: Base USDC, receive-only, after the scope is accepted and the qualification gate passes. The buyer provides non-custodial transaction proof; delivery happens only after payment verification.

The paid delivery bundle includes:

- human-readable audit report;
- machine-readable JSON summary;
- authority map;
- pricing, receipt, audit, and revocation gap list;
- next safe threshold recommendation.

## Qualification Gate

Before any invoice or payment route, open the seven-field Audit Request:

```text
https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md
```

Required non-secret fields:

1. `seller_role`
2. `capability_surface`
3. `monetization_state`
4. `access_control`
5. `approval_and_limit_policy`
6. `receipt_or_audit_trail`
7. `revocation_and_next_threshold`

If any field is missing, ambiguous, secret-bearing, or outside scope, the payment route stays closed.

## Public Proof Assets

This repo exposes strict example artifacts and schemas under `examples/` and `schemas/`. They demonstrate source discipline and machine-readable output style; they are not the paid audit deliverable.

Additional repo artifacts:

- `commerce/product-card.json`
- `commerce/payment_mandate_template.json`
- `deliverables/agent_fiscal_autonomy_audit_template.md`
- `deliverables/agent_fiscal_autonomy_audit_summary.schema.json`
- `docs/one-page-offer.md`
- `docs/retention-trigger-map.md`

## Safety Boundary

All intake must be public, redacted, or buyer-approved. Never submit secrets, private wallet material, raw credentials, auth headers, session material, customer PII, or private logs. The audit reviews boundaries and evidence; it does not need control over funds, accounts, browsers, or production systems.
