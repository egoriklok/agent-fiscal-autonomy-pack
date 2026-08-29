# Product Requirements — Agent Fiscal Autonomy Audit

## Mission

Turn a public or buyer-approved evidence set into a bounded, source-linked
readiness audit for one agent spend or monetization surface. The commercial
milestone is an independently verified external payment for accepted work;
repeatable positive-net sales are the continuing objective.

## Buyer and outcome

The buyer operates a payable API, MCP service, AI tool, dataset, SaaS workflow,
or wallet/credit rail. The audit answers five practical questions:

1. Who authorized the capability or spend?
2. What exact limits and escalation rules apply?
3. What was charged or settled?
4. Which evidence makes the action auditable?
5. How is access reduced or revoked?

## Fixed commercial scope

- Price: `99 USDC` on Base mainnet.
- Scope: one capability surface, up to ten public or buyer-approved redacted
  evidence items, and one asynchronous clarification round.
- Outputs: a Markdown report and machine-readable JSON summary, including an
  authority map, gaps, and one next safe threshold.
- Correction: one factual correction round within seven calendar days.
- Payment: only after seven-field qualification and exact scope acceptance;
  delivery begins only after independent payment verification.

## Digital delivery model

There is no universal 72-hour clock and no artificial one-buyer queue. The
quote states an exact evidence-derived delivery target before payment. A fully
automatable public or redacted scope may complete immediately after payment and
evidence gates pass. Larger or ambiguous scopes receive a later target or are
rejected before invoice.

Each buyer has an isolated state machine, evidence set, artifact namespace,
acceptance record, and settlement record. Multiple buyers may progress in
parallel while source limits, platform rules, verified compute capacity, and
quality gates hold. One buyer's wait state never blocks another buyer.

## Per-buyer state machine

`DISCOVERED -> CONTACT_AUTHORIZED -> CONTACTED -> QUALIFIED -> QUOTED -> PAYMENT_VERIFIED -> DELIVERY -> ACCEPTED -> SETTLED`

Every transition requires current source evidence. Missing or ambiguous
evidence leaves only that buyer in its current state.

## Agent roles

- OpenClaw R1 operates acquisition and buyer communication through its
  source-authorized channels.
- Hermes Agent economy operates parallel acquisition, offer economics,
  qualification, delivery orchestration, cost accounting, and settlement
  verification.
- This repository is the versioned product and delivery contract.
- Honcho stores only confirmed decisions, results, and material lessons with
  source pointers. It is never the product source, CRM, action queue, wallet
  authority, or payment proof.

## Hard boundaries

- No secrets, credentials, private wallet material, raw sessions, or production
  control are required or accepted.
- No invoice before qualification and accepted scope.
- No substantive paid delivery before verified payment.
- No external message, account mutation, signature, or wallet action without
  its current source-exact authority.
- Existing balances, self-transfers, promises, invoices, and wallet movement
  without attributable acceptance are not revenue.

## Success

The audit is done only when the ordered Markdown and JSON artifacts match the
accepted scope, the committed delivery target is met, the buyer's correction or
acceptance outcome is recorded, and the payment remains independently
attributable after costs.
