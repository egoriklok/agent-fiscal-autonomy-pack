# Public Sample: Agent Fiscal Autonomy Audit

Status: `public_sample_not_client_delivery`

Target: Base USDC Wallet Balance Snapshot API

Observation time: 2026-08-26 16:11–16:12 UTC

This sample uses public evidence from an owner-controlled service. It shows the paid audit format. No buyer commissioned this review, and no payment occurred.

## Scope

- Capability: a Base wallet-balance API sold through an x402 external offer.
- Public offer: `https://payanagent.com/api/v1/offers/kh70t4y5x7t5y9xt0aa8gckfn98d4xxn`
- Protected resource: `https://x402-http-demo.egorikas.workers.dev/protected-route`
- Evidence reviewed: the public offer, seller receipt summary, public service page, and unpaid x402 challenges.
- Excluded: credentials, private logs, a paid request, wallet access, and production dashboards.

## Executive Readiness Status

Readiness: `Partial`

The service has a precise receive-only payment boundary. Both GET and POST returned HTTP 402 with the same Base USDC terms.

The full paid lifecycle remains unproven. The public seller record shows zero paid attempts and zero receipts sold.

## Authority Map

| Control | Observed boundary |
|---|---|
| Capability owner | The public seller identity controls the Worker and Payan offer. |
| Approval source | The x402 middleware requires exact payment before the protected response. |
| Agent access | The request accepts one public Base address. It requests no credential or wallet access. |
| Price | `1,000` raw official Base USDC (`0.001 USDC`) per protected request. |
| Network | Base mainnet, CAIP-2 `eip155:8453`. |
| Payment timeout | 300 seconds. |
| Cumulative buyer cap | Not published. |
| Revocation path | Not published for the Payan seller credential or listing. |

## Evidence Reviewed

### Payment boundary

The protected GET and POST routes returned HTTP 402. Each response specified:

- x402 version 2.
- scheme `exact`.
- network `eip155:8453`.
- amount `1000`.
- official Base USDC contract `0x833589fCD6eDb6E08f4C7C32D4f71b54bdA02913`.
- receive-only destination `0x1E5E…f5d3`. The cited response contains the exact value.
- timeout 300 seconds.

This observation proves the unpaid payment challenge. It does not prove a sale, delivery, or settlement.

### Public offer

The offer is active and declares a strict address input schema. Its output schema binds USDC and ETH balances to one observed Base block.

The offer shows `paidAttempts=0`. The seller receipt summary shows `receiptsSold=0` and no receipts.

## Gap List

### 1. Pricing representation

**Finding:** The offer exposes `priceCents=0`, `priceUsd=0.001`, and `amountRaw=1000` at the same time.

**Risk:** A catalog or buyer agent that relies on whole cents can interpret the offer as free.

**Recommended fix:** Treat the atomic token amount as authoritative. Show a micro-USDC price field or an exact decimal string in every public projection.

### 2. Paid lifecycle evidence

**Finding:** No public record links a paid attempt, Payan receipt, Base transfer, and delivered response for this offer.

**Risk:** The correct HTTP 402 challenge can hide a settlement or relay fault.

**Recommended fix:** Preserve one attributable third-party purchase. Link the offer, platform receipt, successful Base USDC transfer, and response hash.

### 3. Buyer budget limit

**Finding:** The server states a per-request price but no cumulative client limit.

**Risk:** An autonomous buyer can repeat valid requests beyond its intended budget.

**Recommended fix:** Require a client-side total cap. Publish a recommended request cap and a stop rule for repeated calls.

### 4. Revocation and rotation

**Finding:** The public material does not document an exact seller-key rotation, revoke, or account-close route.

**Risk:** A compromised seller credential can remain usable until a platform operator intervenes.

**Recommended fix:** Obtain and publish the official rotation or revoke procedure. If no procedure exists, record the operator support path and expected response time.

### 5. Demand proof

**Finding:** The offer is technically ready but has no paid attempt or receipt.

**Risk:** More payment engineering can consume effort without testing buyer demand.

**Recommended fix:** Seek one qualified buyer request before additional infrastructure work. Do not use an owner-funded test as revenue evidence.

## Next Safe Threshold

Run one buyer-authorized purchase only after the buyer accepts the exact price and a strict total budget.

A successful threshold requires all of these records:

1. the buyer request or acceptance reference.
2. the Payan receipt.
3. the successful official Base USDC transfer.
4. the protected response hash.
5. the seller balance increase above its pre-action baseline.
6. all direct costs.

## Boundary Statement

This sample is a readiness review. It is not financial, legal, tax, investment, security, or compliance advice. It guarantees no revenue, payment, or incident prevention.

## Evidence Artifacts

- `evidence/fiscal-sample-public-probe-20260826T161112Z.json`
- `evidence/fiscal-sample-protected-route-20260826T161212Z.json`
- `evidence/payanagent-activation-live-20260825T112003+0300.json`
