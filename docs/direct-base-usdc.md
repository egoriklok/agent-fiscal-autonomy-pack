# Direct Base USDC Flow

This product can use direct Base USDC transfer for the first launch, but only after the readiness audit scope is qualified and explicitly accepted.

Excluded launch dependencies:

- Stripe;
- Circle Mint;
- Coinbase Commerce;
- CDP production facilitator;
- custodial processors;
- custodial marketplace payment processors.

## Payment Route Gate

The seller receiving reference is issued only inside a qualified quote, invoice, or payment mandate. Do not send funds from this public document alone.

Required preconditions:

- seven-field qualification is complete;
- scope is fixed and accepted;
- quote id or payment mandate exists;
- amount, asset, chain, expiry, delivery SLA, refund rule, and verification path are visible;
- no secrets, custody, wallet signing, or private dashboard access are requested.

## Security Boundaries

- No seed phrases.
- No private keys.
- No cookies, sessions, auth headers, OAuth tokens, or API keys.
- No custody of buyer or seller funds.
- No payment verification through wallet access.
- Refunds, if any, are separate seller-side transfers before delivery only.
