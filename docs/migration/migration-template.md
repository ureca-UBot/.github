---
title: 'Migration: [TODO: From → To]'
type: migration
status: draft
owner: '[TODO: OWNER]'
applicability: '[TODO: PRODUCT_PROFILE]'
last_reviewed: null
---

# [TODO: Migration]

## 변경 이유와 영향 사용자

[TODO: 어떤 문제가 해결되는가, 누가 영향을 받는가]

## 사전 조건

- [TODO: clean baseline]
- [TODO: backup/permission]
- [TODO: compatible versions]

## 단계별 계획

```text
Old → Optional Compatibility Bridge → Verify → Cutover → Cleanup
```

### Dry-run

```bash
[TODO: --dry-run command]
```

Expected:

```text
[TODO: changed resources]
```

### Migration

Actor: [TODO]

Mutability: [READ_ONLY / MUTATING / DESTRUCTIVE]

Repeatability: [ONE_TIME / IDEMPOTENT / REPLACE_ON_REPEAT / NON_IDEMPOTENT]

```bash
[TODO: command]
```

Verify: [TODO: observable end-to-end outcome]

## Cutover Contract

- Source authority: [TODO]
- Target authority: [TODO]
- Watermark/checkpoint: [TODO]
- Catch-up criterion: [TODO]
- Cutover barrier: [TODO]
- In-flight request behavior: [TODO]
- Authority transfer point: [TODO]

## Rollback 및 비가역 지점

- Pre-armed rollback: [TODO]
- Rollback independence: [TODO]
- Irreversible point: [TODO]
- Cleanup safety: [TODO]

## 임시 Migration Helper 제거

- Removal condition: [TODO]
- Owner: [TODO]

[Product Compatibility](../compatibility/product-matrix.md)
