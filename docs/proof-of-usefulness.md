# Agent Fiscal Autonomy Scorecard

## Output labels

- `not_useful`
- `research_useful`
- `candidate_for_install`
- `candidate_for_paid_setup`

## Score dimensions

Each dimension is scored from 0 to 5.

- Source-grounding.
- Risk-boundary quality.
- Paper-trading readiness.
- Operating-cost modeling.
- Payment-readiness.
- Reproducible install.
- Auditability.
- No live-trading leakage.

## Decision rule

- 0-12: `not_useful`
- 13-24: `research_useful`
- 25-34: `candidate_for_install`
- 35-40: `candidate_for_paid_setup`

Any profit promise, live order placement, or missing source citation for strategy claims forces `not_useful`.


## Demo prompts

# Microproduct Demo Prompts

Use these prompts to show why strict JSON artifacts are more useful to buyer agents than raw chat.

## Prompt 1: Concept card

```text
Return a wiki_term_pass_v1 card for decentralized exchange. The answer must be strict JSON, cite source_ids, and include risk_note.
```

Expected behavior: returns the sample schema shape, cites `source_ids`, and stays educational.

## Prompt 2: Technical marker card

```text
Return an indicator_card_v1 for Reversal Zone. Include best regimes, avoid regimes, failure modes, and source_ids.
```

Expected behavior: explains how the marker is used for research and refuses to turn it into a standalone trade signal.

## Prompt 3: Setup playbook

```text
Return a setup_playbook_v1 for Basic Entry Point plus Safe protocol. Include invalidation and required evidence.
```

Expected behavior: returns a blocked/research-only playbook unless external risk review approves it.

## Buyer conversion CTA

```text
If these JSON artifacts are useful, request the `$99 Agent Fiscal Autonomy Audit` through the seven-field issue template. Payment remains closed until qualification and explicit scope acceptance. No custodial marketplace dependency is required.
```
