---
title: 'ADR-003: 현재 FAQ 검색에서 Reranker 제외'
type: architecture-decision
status: active
owner: 'UBot maintainers'
applicability: development-preview
last_reviewed: '2026-10-26'
---

# ADR-003: 현재 FAQ 검색에서 Reranker 제외

- Status: Accepted
- Date: 2026-10
- Related Repositories: UBot-EmbeddingTest, UBot-BE

## Context

Reranker는 dense 검색 후보의 순서를 바꿔 품질을 높일 수 있지만 모델 호출, 지연, GPU 자원과 장애 경로를 추가합니다. 후보 구성과 데이터셋에 따라 효과도 달랐습니다.

## Decision

현재 Production FAQ 검색은 dense 후보를 사용하고 별도 Reranker를 호출하지 않습니다.

## Evidence

[확대·정정 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/reranker/docs/임베딩_vs_reranker_비교결과_1000.md)에서는 BGE-M3 단독이 두 Reranker 조합보다 높은 Top-1을 기록했습니다. 이 결과는 해당 데이터셋과 후보 구성에 한정됩니다. 따라서 “Reranker는 항상 나쁘다”가 아니라 현재 Production 경로에 넣을 근거가 충분하지 않다는 결정입니다.

## Trade-offs

- 실행 경로와 GPU 의존성은 단순해집니다.
- 후보 집합은 좋지만 1위 순서가 틀린 질문을 개선할 기회를 놓칠 수 있습니다.
- 서로 다른 실험 결과를 직접 비교할 수 없어 Production과 가까운 holdout이 필요합니다.

## Production Implementation

[UBot-BE RAG Pipeline](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md)

## Revisit Triggers

- 독립 검토한 실제 FAQ holdout에서 일관된 순위 개선을 확인할 때
- 추가 지연과 자원 비용을 포함해도 제품 목표를 충족할 때
- 장애 시 fallback과 관측 지표를 함께 설계할 수 있을 때
