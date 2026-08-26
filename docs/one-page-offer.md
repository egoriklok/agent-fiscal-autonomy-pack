# Agent Fiscal Autonomy Audit — $99 Fixed Scope

## The Problem

A payable API can charge correctly and still expose an authority gap.

Our own public x402 offer proved this. Its atomic price was `0.001 USDC`, but
one catalog field reported `priceCents=0`. The payment rail was precise. The
public representation was ambiguous.

The Agent Fiscal Autonomy Audit finds gaps like this before you expand agent
access, spend, or monetization.

## What You Receive

Within 72 hours after verified payment, you receive:

1. an evidence-linked authority map;
2. a review of approval rules and spend limits;
3. a pricing and payment consistency review;
4. a receipt and audit-trail gap list;
5. a revocation and rollback review;
6. one recommended next safe threshold;
7. a Markdown report;
8. a machine-readable JSON summary;
9. one factual correction round within seven calendar days.

See the [public sample audit](public-sample-audit.md) and its
[JSON summary](https://github.com/egoriklok/agent-fiscal-autonomy-pack/blob/main/deliverables/public-sample-audit-summary.json).

## Fixed Scope

The fixed price covers:

- one payable API, MCP server, agent tool, dataset, SaaS workflow, or wallet rail;
- up to ten public or buyer-approved redacted evidence items;
- one asynchronous clarification round;
- no production access;
- no credential, signer, wallet, or private dashboard access.

A larger or different scope requires a new agreement. The buyer can decline
before payment.

## Price and Delivery

- Price: `99 USDC` on Base mainnet.
- Invoice: issued only after the seven-field qualification and exact scope acceptance.
- Delivery target: 72 hours after verified payment and receipt of all accepted evidence.
- Seller failure before delivery: full refund of the received `99 USDC`.
- After delivery: one factual correction round. Disagreement with a documented readiness judgment is not a refund condition.

## Free Qualification Snapshot

Before any invoice, the buyer can submit seven non-secret fields:

1. seller role;
2. capability surface;
3. monetization state;
4. access control;
5. approval and limit policy;
6. receipt or audit trail;
7. revocation path and next threshold.

The free response contains:

- `Ready`, `Partial`, or `Blocked`;
- three evidence-linked blind spots;
- one next scope question.

The buyer can stop after this response. No payment is due.

## Safety Boundary

Do not send seed phrases, private keys, cookies, sessions, OAuth tokens, API
keys, auth headers, customer PII, or confidential logs.

This is a readiness audit. It is not financial, legal, tax, investment,
security, or compliance advice. It guarantees no revenue, payment, security
result, or incident prevention.

## Request

Open the seven-field audit request with public or redacted information:

```text
https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md
```

The payment route stays closed until both sides accept the fixed scope.
