# Payment and Entitlement Flow

Default external rail after qualification: Base USDC.

Network: Base mainnet, chain id 8453. USDC contract: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

The receiving address is issued only inside a qualified quote, invoice, or payment mandate after explicit scope acceptance. Do not send funds to any address merely because it appears in public discussion or historical examples.

Before invoice, open the seven-field Audit Request issue:

```text
https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md
```

Required qualification fields:

- `seller_role`
- `capability_surface`
- `monetization_state`
- `access_control`
- `approval_and_limit_policy`
- `receipt_or_audit_trail`
- `revocation_and_next_threshold`

Flow:

1. Agent inspects public proof and safety boundaries.
2. Prospect provides the seven non-secret qualification fields.
3. Seller accepts a fixed scope.
4. Seller issues quote/payment mandate with quote id, amount, expiry, scope, delivery SLA, verification path, and recipient reference.
5. Buyer sends exact Base USDC and provides transaction hash.
6. Seller verifies chain, token, recipient, amount, success status, expiry, quote id, and duplicate status.
7. Seller issues receipt and entitlement.
8. Buyer receives the Markdown report and JSON summary.

No private keys, seed phrases, custodial payment accounts, raw credentials, browser sessions, or wallet signing are part of this public plugin flow.
