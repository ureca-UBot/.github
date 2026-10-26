---
title: 'Contract: [TODO: Producer → Consumer]'
type: cross-repo-contract
status: draft
owner: '[TODO: OWNER]'
applicability: '[TODO: PRODUCT_PROFILE]'
last_reviewed: null
---

# [TODO: Producer → Consumer Contract]

## 범위

- Producer component: [TODO]
- Consumer component: [TODO]
- Source repository/schema: [TODO: commit-aware path]
- Runtime authority: [TODO: response header/status/control-plane field]
- Contract version: [TODO]
- Joint owners: [TODO: producer & consumer]

## 요청 또는 메시지의 의미

[TODO: 필드, 상태, 단위, 기본값과 적용 시점]

| Input | Meaning | Missing/null/empty | Unknown input |
|---|---|---|---|
| [TODO: field] | [TODO] | [TODO] | [REJECT / IGNORE / WARN / PRESERVE] |

## 호출과 전달 계약

- Timeout: [TODO: value+unit]
- Retryable errors: [TODO]
- Backoff/stop: [TODO]
- Ordering: [TODO]
- Duplicate/idempotency: [TODO]
- Resource lifetime/cleanup: [TODO, if applicable]

## 실패 시 동작

| Failure | Producer behavior | Consumer behavior | Safety policy |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [FAIL_OPEN / FAIL_CLOSED / FALLBACK] |

## 버전 호환성

| Surface | Rule | Proof |
|---|---|---|
| Source | [TODO] | [TODO] |
| Wire | [TODO] | [TODO] |
| Semantic | [TODO] | [TODO] |
| Persisted data | [TODO] | [TODO] |

## 배포와 되돌리기

- Compatible rollout order: [TODO]
- Rollback constraint: [TODO]
- Default evolution/persisted data risk: [TODO]

## 검증

```bash
[TODO: executable contract test command]
```

Expected:

```text
[TODO: asserted result]
```

Evidence applicability: [TODO: producer/consumer commits, config, environment, sample]

Generated artifact revision: [TODO: schema source commit + generator version]
