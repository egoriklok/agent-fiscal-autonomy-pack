# Agent Fiscal Autonomy Plugin

This public plugin is the free proof and commerce wrapper for Agent Fiscal Autonomy Audit.

It helps a buyer or seller agent:

- inspect public no-secret readiness proof artifacts;
- understand safety boundaries before requesting a paid audit;
- open the seven-field Audit Request issue;
- keep payment closed until qualification and explicit scope acceptance;
- verify receipt, entitlement, and delivery handoff after payment.

Audit request path:

```text
https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md
```

Before the `$99 Agent Fiscal Autonomy Audit` invoice, provide:

- `seller_role`
- `capability_surface`
- `monetization_state`
- `access_control`
- `approval_and_limit_policy`
- `receipt_or_audit_trail`
- `revocation_and_next_threshold`

The paid report is not included in this plugin. Paid delivery happens only after explicit scope acceptance, verified Base USDC payment, and entitlement.

## Safety Boundary

- No financial, legal, tax, investment, or compliance advice.
- No guaranteed revenue, security, compliance, or incident prevention.
- No live trading or exchange order placement.
- No custody of buyer or seller funds.
- No wallet seed, private key, cookie, session, OAuth token, API key, auth header, or raw credential handling.
- No private delivery links before verified payment and entitlement.

## Public Proof Assets

Use the public repository examples and schemas before requesting an audit:

- examples/wiki_term_pass_v1.json
- examples/indicator_card_v1.json
- examples/setup_playbook_v1.json
- schemas/wiki_term_pass_v1.schema.json
- schemas/indicator_card_v1.schema.json
- schemas/setup_playbook_v1.schema.json

## Payment Rail

Default external rail: Base USDC after qualification.

Do not send funds until a quote or payment mandate with amount, expiry, scope, delivery SLA, verification path, and recipient reference has been issued after explicit scope acceptance.
