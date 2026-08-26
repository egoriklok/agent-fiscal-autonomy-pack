# Public Proof of Usefulness

The public sample audits an owner-controlled x402 API. It is not a fictional
example and not a client delivery.

## Concrete Finding

The protected API declared an exact price of `1,000` raw official Base USDC.
The public offer exposed these price fields at the same time:

- `amountRaw=1000`.
- `priceUsd=0.001`.
- `priceCents=0`.

A client that relies on whole cents can interpret the offer as free. The audit
separates the correct payment rail from the ambiguous catalog projection and
provides a specific fix.

## What The Sample Demonstrates

- evidence-linked findings instead of generic advice.
- separate authority, payment, receipt, limit, and revocation analysis.
- explicit facts, risks, and recommended fixes.
- a machine-readable summary that validates against the public schema.
- a no-secret and no-custody boundary.
- an honest `Partial` result for a paid lifecycle that lacks evidence.

## What The Sample Does Not Prove

- It does not prove that the offer made a sale.
- It does not prove that every private control is safe.
- It does not guarantee revenue, security, compliance, or incident prevention.
- It is not financial, legal, tax, investment, security, or compliance advice.

## Review The Artifacts

- [Human-readable audit](public-sample-audit.md)
- [Machine-readable summary](../deliverables/public-sample-audit-summary.json)
- [Summary schema](../deliverables/agent_fiscal_autonomy_audit_summary.schema.json)

If this format fits your capability, open the seven-field Audit Request. The
payment route remains closed until qualification and exact scope acceptance.
