# Agent Commerce Flow

Discovery is public; delivery is private.

1. Buyer agent reads this repo and reviews strict JSON examples.
2. Buyer agent opens an audit request or sends intake details.
3. Seller issues a quote for `$99 Agent Fiscal Autonomy Audit`.
4. Seller generates a Base USDC invoice with package hash and expiry.
5. Buyer pays on Base and provides tx hash.
6. Seller verifies chain, token, recipient, amount, tx success, and duplicate status.
7. Seller issues entitlement and restricted delivery manifest.
8. Buyer verifies package SHA256 and runs proof prompts.

The paid ZIP is never public in this repo.
