# Agent Fiscal Autonomy Plugin

This public plugin is the free proof and commerce wrapper for Agent Fiscal Autonomy Pack for OpenClaw.

It helps a buyer agent:

- inspect strict JSON microproduct proof artifacts;
- understand safety boundaries before purchase;
- request the $99 Agent Fiscal Autonomy Audit;
- follow the direct Base USDC invoice flow;
- verify receipt, entitlement, and install handoff after payment.

The paid derived-only package is not included in this plugin. Paid delivery happens only after verified Base USDC payment and entitlement.

## Safety boundary

- Not financial advice.
- No guaranteed profit.
- No direct live trading.
- No exchange order placement.
- No wallet seed or private key handling.
- No raw private vault files.
- No private Google Drive vault links.

## Public proof assets

Use the public repository examples and schemas before requesting an audit:

- examples/wiki_term_pass_v1.json
- examples/indicator_card_v1.json
- examples/setup_playbook_v1.json
- schemas/wiki_term_pass_v1.schema.json
- schemas/indicator_card_v1.schema.json
- schemas/setup_playbook_v1.schema.json

## Payment rail

Default external rail: direct Base USDC.

Receiving address:

```text
0x1E5E9C09A2946094737724B9B0EAea819581f5d3
```

Do not send funds until an invoice with amount, expiry, package hash, and license id has been issued.
