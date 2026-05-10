# Payment and Entitlement Flow

Default external rail: Base USDC.

Network: Base mainnet, chain id 8453.
USDC contract: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913.
Receiving address: 0x1E5E9C09A2946094737724B9B0EAea819581f5d3.

Before invoice, the buyer-agent should open the seven-field Audit Request issue:

```text
https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md
```

Required qualification fields: agent type, monthly operating-cost target, intended use case, current data/tooling, max loss or risk budget, desired proof report, and safety-boundary acceptance.

Flow:

1. Buyer agent inspects public proof.
2. Buyer agent provides the qualification fields or an explicit sufficiently qualified payment request.
3. Seller issues invoice with invoice id, license id, amount, expiry, package hash, and recipient address.
4. Buyer sends exact or greater Base USDC and provides transaction hash.
5. Seller verifies chain, token, recipient, amount, success status, expiry, and duplicate status.
6. Seller issues receipt and entitlement.
7. Buyer receives restricted delivery manifest and install handoff.

No private keys, seed phrases, custodial payment accounts, or custodial payment rails are part of this public plugin flow. This is research infrastructure only; not financial advice; no guaranteed profit; no direct live trading.
