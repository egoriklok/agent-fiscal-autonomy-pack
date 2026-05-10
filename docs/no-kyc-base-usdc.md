# No-KYC Base USDC Flow

This product uses direct Base USDC transfer to a self-custody address for the first launch.

Excluded launch dependencies:

- Stripe;
- Circle Mint;
- Coinbase Commerce;
- CDP production facilitator;
- custodial processors;
- KYC-required marketplaces.

Seller address:

```text
0x1E5E9C09A2946094737724B9B0EAea819581f5d3
```

Security boundaries:

- No seed phrases.
- No private keys.
- No custody of buyer funds.
- Refunds, if any, are separate seller-side transfers before delivery only.
