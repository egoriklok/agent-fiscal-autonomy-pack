# Public Plugin Wrapper

The public plugin is an installable proof and commerce wrapper. It lets another agent inspect the product, understand safety boundaries, request a quote, and follow the Base USDC entitlement flow.

It does not include the paid derived-only package. The paid package is delivered only after verified payment and entitlement.

## Install model

- Install the public plugin from `plugins/agent-fiscal-autonomy-plugin`.
- Read the onboarding skill.
- Inspect examples and schemas.
- Open the seven-field Audit Request issue: `https://github.com/egoriklok/agent-fiscal-autonomy-pack/issues/new?template=audit_request.md`.
- Include agent type, monthly operating-cost target, intended use case, current data/tooling, max loss or risk budget, desired proof report, and safety-boundary acceptance.
- Use receipt and entitlement to install the paid package after payment verification.

## Why plugin-first, not plugin-only

A plugin-only sale would expose too much value publicly or require embedding private delivery data. The safer model is a free plugin that proves utility and routes qualified buyers into a paid entitlement flow.

Safety: research only; not financial advice; no guaranteed profit; no direct live trading.
