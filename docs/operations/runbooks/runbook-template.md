---
title: 'Runbook: [TODO: Operation]'
type: runbook
status: draft
owner: '[TODO: OWNER]'
applicability: '[TODO: PRODUCT_PROFILE]'
last_reviewed: null
---

# [TODO: Operation]

## 실행 조건과 목표

- Trigger: [TODO]
- Desired end state: [TODO]
- Operator/owner: [TODO]
- User/data impact: [TODO]

## 안전 등급

- Mutability: [READ_ONLY / MUTATING / DESTRUCTIVE]
- Repeatability: [ONE_TIME / IDEMPOTENT / REPEATABLE / NON_IDEMPOTENT]
- Reversibility: [Two-way / Expensive / One-way]

## 변경 전 관찰 및 증거 확보

```bash
[TODO: read-only command]
```

Capture: [TODO: release/commit/config/metrics/logs/last-known-good]

## Rollback 경로 사전 준비

[TODO: independent rollback control plane, owner and commands]

## 실행 단계

### 1. [TODO: Action]

```bash
[TODO: exact command]
```

Expected:

```text
[TODO: exact result]
```

Produced value: [TODO: value for next step]

If not: [STOP / ESCALATE / next branch]

### 2. [TODO: Next action]

Consumes: [TODO: previous step result]

```bash
[TODO: exact command]
```

Expected:

```text
[TODO: exact result]
```

## 수렴/최종 검증

- Desired version: [TODO]
- Observed version: [TODO]
- Converged when: [TODO]
- Time limit: [TODO]
- On NOT_EVALUATED: [TODO]

## Rollback

- Trigger: [TODO]
- Steps: [TODO]
- Expected: [TODO]

## Escalation

[TODO: owner, trace and diagnostic bundle]
