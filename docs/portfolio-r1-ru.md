# Agent Fiscal Autonomy Pack — R1 portfolio page

**Коротко для портфолио:** я строю `Agent Fiscal Autonomy Pack` — proof-layer для AI agency economy, где AI-агенты, MCP/API-сервисы и публичные bounty/project surfaces проходят безопасную воронку: public discovery -> no-secret snapshot -> scope acceptance -> receive-only payout proof -> verified delivery.

Эта страница сделана как русскоязычная витрина проекта для раздела `Verification` в портфолио. Она показывает не обещание дохода, а реальную продуктовую систему: публичный репозиторий, CJM, CRM-воронку, safety-gates, rail-aware scoring и честное разделение pipeline value от подтвержденной выручки.

## Что это за проект

`Agent Fiscal Autonomy Pack` — публичный набор артефактов для аудита готовности сервисов к агентской коммерции. Целевая поверхность: payable MCP/API-сервисы, x402-adjacent продукты, browser/action-инструменты, agent-payment rails и команды, которые хотят безопасно открыть платный доступ для AI buyer-agents.

Главная идея: прежде чем AI-агент сможет покупать, оплачивать или запускать агентный сервис, нужно проверить не “может ли он заплатить”, а “можно ли это сделать без потери контроля”. Проект формализует эти вопросы в воронку, чеклисты и machine-readable доказательства.

## Почему это важно для AI agency economy

AI agency economy требует не только агентов, которые пишут код или ищут лиды. Нужен слой доверия между агентом-покупателем, сервисом-продавцом и человеком-владельцем бюджета. Этот проект строит именно такой слой:

- проверка authority boundaries: кто может одобрить действие и где лимит;
- spend caps и escalation thresholds до оплаты;
- receipt, settlement и audit-trail evidence после действия;
- revocation path, key rotation и access reduction;
- доказуемая доставка через PR, тесты, отчет, JSON summary и ссылку на proof artifact;
- receive-only Base USDC / payout proof без wallet signing, custody, swap, bridge или transfer со стороны агента.

## Текущий продуктовый контур

Бесплатный вход — `public/no-payment readiness snapshot` на основе открытых доказательств. Он не является invoice, payment request или paid delivery.

Платный вход — fixed-scope readiness review за `99 USDC/USDT` только после explicit `scope_acceptance=true`. До принятого scope payment route закрыт.

Основные deliverables paid review:

- human-readable audit report;
- machine-readable JSON summary;
- authority map;
- pricing, receipt, audit-trail and revocation gap list;
- next safe threshold recommendation.

## Как работает воронка R1

1. `Public discovery`: анализируются публичные GitHub issues, bounty surfaces, MCP/API/x402/payment-related контексты.
2. `Free snapshot`: создается короткий no-secret readiness snapshot: Ready / Partial / Blocked, blind spots и один точный next scope question.
3. `Scope acceptance`: клиент или maintainer подтверждает конкретный paid scope. Без этого invoice/payment request запрещен.
4. `Payment proof`: используется receive-only Base USDC или другой публичный payout rail. Агент не получает доступ к seed/private key и не может подписывать или тратить средства.
5. `Delivery`: результат закрывается доказуемым пакетом: PR/result, tests/build proof, summary, proof artifacts, next improvement suggestion.
6. `Retention`: повторная продажа возможна только по событию: новый paid endpoint, новый rail, изменение policy, revocation/receipt gap, incident или новый accepted scope.

## Что уже собрано

По актуальной R1/CJM-таблице от `2026-05-31`:

- публичный repo `agent-fiscal-autonomy-pack` выровнен с R1 CJM через merged PR #1;
- CRM pipeline живой: `4 tracked bounty deals`, `4 review-ready`, но `0 verified received USDC`;
- public acquisition scan: `54 raw issues`, `30 evaluated`, `0 eligible safe comment targets`, `0 comments posted`;
- R1 source pack: `240 public repos scanned`, `50 selected`, `50 candidate rows`, `50 CRM rows`, `50 qualification rows`;
- R1 CRM queue: target `50` уже достигнут как readiness artifact;
- revenue automation lane проходит безопасный цикл: discovery -> queue proof -> CRM -> payout envelope -> wallet watch;
- wallet watch и payment envelope работают в read-only / receive-only режиме: `no signing`, `no spend`.

## Честный статус

Подтвержденная выручка сейчас: `0 USDC`.

Это принципиально важно для портфолио: проект показывает работу над реальной инфраструктурой AI agency economy, но не заявляет продажи, revenue или payout до факта. Expected pipeline value не равен received revenue. Revenue признается только после public tx/platform proof и delivered artifact.

## Что считается успехом следующего этапа

Ближайший gate: довести R1 queue и public targets до состояния, где есть validator-green candidates, безопасный public send, принятый scope, затем payment proof и delivery artifact.

Минимальный business success:

- `scope_acceptance_status = accepted` для одного qualified candidate;
- `payment_status = verified` по public tx/platform proof;
- `recognized_revenue_usdc = 99` только после delivery artifact.

## Safety boundary

Проект намеренно не делает следующие вещи:

- не продает KYC-bypass;
- не берет custody;
- не делает wallet signing;
- не выполняет paid calls до scope acceptance;
- не запрашивает private dashboards, API keys, cookies, sessions, OAuth tokens, private customer data или raw credentials;
- не обещает guaranteed revenue, guaranteed payout, legal/compliance outcome или финансовый результат.

## Почему это сильный portfolio signal

Этот проект демонстрирует работу не над абстрактным “AI wrapper”, а над коммерческой инфраструктурой для агентных систем:

- продуктовая воронка сформулирована как доказуемый процесс;
- агентная автоматизация ограничена safety-gates;
- GitHub repo используется как public trust surface;
- paid route закрыт до квалификации;
- revenue truth отделен от pipeline optimism;
- delivery описана через проверяемые artifacts, а не через обещания.

Для раздела портфолио это можно формулировать так:

> Работаю над Agent Fiscal Autonomy Pack — proof-layer для AI agency economy: безопасная CRM-воронка, no-secret readiness snapshots, receive-only Base USDC payout proof, rail-aware scoring и delivery artifacts для agent-facing MCP/API/x402 сервисов.

## Verification links

- Public repo: <https://github.com/egoriklok/agent-fiscal-autonomy-pack>
- GitHub Pages home: <https://egoriklok.github.io/agent-fiscal-autonomy-pack/>
- README: <https://github.com/egoriklok/agent-fiscal-autonomy-pack/blob/main/README.md>
- Roadmap: <https://github.com/egoriklok/agent-fiscal-autonomy-pack/blob/main/ROADMAP.md>
- One-page offer: <https://github.com/egoriklok/agent-fiscal-autonomy-pack/blob/main/docs/one-page-offer.md>
- Retention trigger map: <https://github.com/egoriklok/agent-fiscal-autonomy-pack/blob/main/docs/retention-trigger-map.md>
- Merged PR #1: <https://github.com/egoriklok/agent-fiscal-autonomy-pack/pull/1>

## Embed target

После merge в `main` эта страница будет доступна как GitHub Pages URL:

```text
https://egoriklok.github.io/agent-fiscal-autonomy-pack/portfolio-r1-ru.html
```

Рекомендуемый короткий anchor text для портфолио:

```text
Agent Fiscal Autonomy Pack — proof-layer для AI agency economy
```
