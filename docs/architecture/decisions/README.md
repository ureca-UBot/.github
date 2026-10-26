# Engineering Decisions

UBot의 주요 기술 결정과 실험 근거, 실제 구현 문서를 연결합니다. 이 문서는 상세 구현과 설정값을 설명하지 않습니다. 현재 동작과 기본값은 각 Repository 문서를 기준으로 확인합니다.

## 근거가 구현으로 이어지는 방식

```text
Experiment / Benchmark
        ↓
      Evidence
        ↓
 Engineering Decision
        ↓
Production Implementation
```

실험의 최고 수치를 그대로 채택하지 않습니다. 데이터 대표성, 품질, 지연, 비용, 운영 복잡도와 재현성 한계를 함께 보고 결정합니다.

## 결정 상태

- `Proposed` — 검토 중
- `Accepted` — 현재 채택
- `Superseded` — 다른 결정으로 대체
- `Deprecated` — 더 이상 사용하지 않음

## Decision Index

| ID | 결정 | 상태 | 선택 이유 | Evidence | Production Implementation |
|---|---|---|---|---|---|
| [ADR-001](ADR-001-vector-database.md) | PostgreSQL + pgvector 사용 | Accepted | FAQ 원문과 벡터를 한 저장소에서 관리해 동기화·재색인·운영 복잡도를 줄임 | [Vector DB decision](https://github.com/ureca-UBot/UBot-VertorDBTest/blob/9fcbff349648067fc4c96d56d82857f1bcccfdfd/docs/07-results/decision.md) | [UBot-BE 검색 문서](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/faq-embedding.md) |
| [ADR-002](ADR-002-embedding-model.md) | Embedding 모델로 BGE-M3 사용 | Accepted | 소규모 모델 비교의 Top-K·MRR과 후속 검색 실험의 적용 가능성을 함께 고려 | [Embedding benchmark](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/model_benchmarks/docs/임베딩모델_벤치마크_최종비교.md) | [UBot-BE 모델 설정](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/llm/settings.md) |
| [ADR-003](ADR-003-reranker-strategy.md) | 현재 FAQ 검색에서 Reranker 제외 | Accepted | 확대·정정 비교와 현재 경로의 비용·복잡도를 기준으로 dense 검색만 운영 | [Corrected comparison](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/reranker/docs/임베딩_vs_reranker_비교결과_1000.md) | [UBot-BE RAG pipeline](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md) |
| [ADR-004](ADR-004-llm-selection.md) | Qwen3-4B Instruct 계열 사용 | Accepted | 품질과 실행 비용을 함께 보고 4B Instruct 계열을 답변 모델로 선택 | [LLM v5](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/all_summary.md) · [Quantization decision](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/summary/quantization_decision.md) | [UBot-BE model runtime](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/llm/README.md) |
| [ADR-005](ADR-005-async-chat-processing.md) | 질문 접수와 답변 처리 분리 | Accepted | 빠른 접수와 오래 걸리는 모델 실행을 분리하고 중단 작업을 저장 상태에서 복구 | [Reliability model](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reliability/reliability-model.md) | [UBot-BE architecture](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/architecture/overview.md) |

## 해석할 때 주의할 점

- ADR-001은 pgvector가 가장 빨랐다는 결정이 아닙니다. 더 빠른 후보가 있었고 운영 단순성을 함께 고려했습니다.
- ADR-002의 모델 비교 결과는 당시 데이터셋의 결과이며 현재 서비스 전체 검색 정확도를 뜻하지 않습니다.
- ADR-003은 Reranker가 항상 성능을 낮춘다는 결론이 아닙니다. 데이터셋과 후보 구성에 따라 결과가 달라질 수 있습니다.
- ADR-004는 모델 계열에 관한 결정입니다. Ollama/GGUF 품질 결과를 현재 vLLM 양자화 구성의 품질로 그대로 옮기지 않습니다.
- ADR-005는 구조 선택입니다. 장애 복구 범위와 제한 시간은 UBot-BE가 관리합니다.

실험 조건과 수치, Production 검증과의 경계는 [Evidence Register](../../proof/evidence-register.md)에서 확인합니다. 원시 데이터와 실행 코드는 연결된 Research·Benchmark Repository가 관리합니다.
