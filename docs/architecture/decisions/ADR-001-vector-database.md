# ADR-001: PostgreSQL + pgvector를 Vector DB로 사용

- Status: Accepted
- Date: 2026-09
- Related Repositories: UBot-VectorDBTest, UBot-BE

## Context

FAQ 원문과 검색 벡터를 운영하면서 검색 품질·지연뿐 아니라 데이터 동기화, 재색인, 백업과 장애 대응 비용까지 함께 관리해야 합니다.

## Decision

UBot의 Production FAQ 벡터 저장소로 PostgreSQL과 pgvector를 사용합니다. 검색 인덱스의 현재 방식과 세부 설정은 UBot-BE가 관리합니다.

## Alternatives Considered

합성 10k 벡터·Top-10·동시성 10, Recall 약 0.96 구간의 측정값입니다([선정 결론](https://github.com/ureca-UBot/UBot-VectorDBTest/blob/9fcbff349648067fc4c96d56d82857f1bcccfdfd/docs/07-results/decision.md)).

| 후보 | p50 / p95 | peak RAM | 채택하지 않은 이유 |
|---|---:|---:|---|
| Qdrant | 2.56 / 3.94 ms | 0.10 GiB | 가장 빨랐지만 별도 서버를 두고 FAQ 원문과 벡터의 동기화·재색인 경로를 따로 운영해야 함 |
| OpenSearch (Lucene HNSW) | 3.49 / 4.93 ms | 4.71 GiB | 속도 이점이 작고 JVM 힙을 포함한 메모리 부담이 큼 |
| Milvus | 4.85 / 17.72 ms | 0.66 GiB | pgvector보다 느리고 본체·etcd·MinIO 구성이 필요함 |
| Weaviate | 13.04 / 24.40 ms | 0.18 GiB | 비교 후보 중 가장 느림 |
| **pgvector (선택)** | 3.35 / 7.34 ms | 0.21 GiB | 기존 PostgreSQL 안에서 원문·벡터·재색인을 함께 관리 |

## Evidence

[Vector DB benchmark](https://github.com/ureca-UBot/UBot-VectorDBTest/blob/9fcbff349648067fc4c96d56d82857f1bcccfdfd/docs/07-results/decision.md)는 여러 저장소를 같은 합성 데이터와 자원 범위에서 비교했습니다. 비슷한 Recall에서 Qdrant와 일부 OpenSearch 구성이 더 빨랐으므로 pgvector를 속도 우승자로 선택한 것은 아닙니다.

## Rationale

- FAQ 관계형 데이터와 벡터를 한 트랜잭션 경계에서 관리할 수 있습니다.
- 별도 Vector DB와 PostgreSQL 사이의 동기화·재색인 경로를 추가하지 않습니다.
- 기존 백업·migration·운영 도구를 함께 사용할 수 있습니다.

## Trade-offs

- 특정 품질 구간에서 전용 Vector DB보다 검색 지연이 높을 수 있습니다.
- 데이터 규모와 filter 조건이 달라지면 현재 선택을 다시 측정해야 합니다.
- 벤치마크의 합성 Top-K 결과는 실제 FAQ의 운영 SLO가 아닙니다.

## Production Implementation

[UBot-BE Embedding and Search](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/features/faq-management.md)

## Revisit Triggers

- 실제 FAQ 규모에서 검색 목표를 반복적으로 충족하지 못할 때
- 별도 검색 저장소의 운영 비용보다 성능 이점이 커질 때
- 데이터 동기화와 재색인을 안전하게 운영할 수 있는 구조가 준비될 때
