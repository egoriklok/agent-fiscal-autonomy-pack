# Agent Loop Memory Model

This project uses a two-level memory model for agent-commerce execution.

## Tactical memory

Tactical memory helps the sales loop decide the next concrete action:

- buyer intent checks;
- proof URL responses;
- quote and invoice steps;
- Base USDC payment verification;
- entitlement and delivery readiness;
- current blockers.

Tactical memory is short-lived and expires unless it is used or promoted.

## Strategic memory

Strategic memory stores durable product and market decisions:

- agents buy machine-readable capabilities, not landing pages;
- the public plugin is proof, not the paid package;
- direct Base USDC remains the no-KYC launch rail;
- x402 and marketplace compatibility are future tracks;
- the product must not promise profit or live trading.

Strategic memory changes only when new market evidence or buyer behavior justifies an update.

## Public vs private memory

Public GitHub memory includes product thesis, proof flows, schemas, examples, and plugin wrapper docs.

Private memory stays outside this repo:

- buyer data;
- invoices and transaction hashes;
- entitlement records;
- private Drive delivery links;
- raw vault paths;
- paid package files.

## Automation policy

The Codex heartbeat runner multiplexes tactical sales, delivery readiness, market research, content drafting, memory maintenance, and strategy synthesis. Each wake should choose one bounded action and record the result before doing anything else.

No automation may handle wallet secrets, place exchange orders, promise profit, bypass KYC systems, or expose raw/private files.
