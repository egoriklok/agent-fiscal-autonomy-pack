# Payment and Entitlement Flow

Default external rail: Base USDC.

Network: Base mainnet, chain id 8453.
USDC contract: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913.
Receiving address: 0x1E5E9C09A2946094737724B9B0EAea819581f5d3.

Flow:

1. Buyer agent inspects public proof.
2. Buyer agent requests quote.
3. Seller issues invoice with invoice id, license id, amount, expiry, package hash, and recipient address.
4. Buyer sends exact or greater Base USDC and provides transaction hash.
5. Seller verifies chain, token, recipient, amount, success status, expiry, and duplicate status.
6. Seller issues receipt and entitlement.
7. Buyer receives restricted delivery manifest and install handoff.

No private keys, seed phrases, custodial payment accounts, or KYC-required rails are part of this public plugin flow.
