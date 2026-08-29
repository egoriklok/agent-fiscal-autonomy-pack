# Fiscal product agent contract

Read `PRD.md`, `README.md`, `commerce/product-card.json`, and `docs/safety.md`
before changing the offer or producing a delivery.

OpenClaw R1 and Hermes Agent economy are parallel workers on one product. Keep a
separate buyer ID, state, evidence set, artifact path, authority gate, and
settlement record for every buyer. Do not impose a global one-buyer WIP limit or
a fixed waiting period. Concurrency is bounded only by current channel rules,
source-exact authority, verified execution capacity, and quality gates.

Never let parallelism weaken these rules:

- one unresolved external mutation at a time per buyer until canonical readback;
- no duplicate target or repeated contact without a new source-authorized reason;
- no secret, credential, private-wallet, or production-control collection;
- no invoice before seven-field qualification and exact scope acceptance;
- no paid delivery before independently verified payment;
- no sale or revenue claim without attributable acceptance and settlement proof.

Honcho is selective derived memory. Store only confirmed decisions, terminal
results, and material lessons with source pointers. Do not store raw leads,
messages, payment details, credentials, or complete product files there, and do
not use memory as action authority.

For a handoff, provide a structured record containing buyer ID, current state,
known and missing qualification fields, product revision, exact delivery target,
next action, authority fingerprint, and source pointers. Reject stale or
cross-buyer state.
