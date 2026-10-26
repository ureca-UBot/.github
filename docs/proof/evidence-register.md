# Evidence Register

UBot의 기술 선택과 제품 주장을 뒷받침하는 실험·검증 기록을 한곳에서 찾기 위한 문서입니다. 원시 데이터와 실행 코드는 각 저장소가 관리하고, 이 문서는 **무엇을 검증했는지**, **어떤 결정에 쓰였는지**, **어디까지 해석할 수 있는지**를 연결합니다.

> 마지막 확인: 2026-10-26

## 근거를 읽는 기준

- **모델 품질**은 고정된 근거를 받은 생성 결과를 평가합니다. FAQ 검색을 포함한 전체 RAG 정확도와는 다릅니다.
- **검색 품질**은 정답 FAQ를 후보 안에서 찾는 능력을 평가합니다. 최종 답변의 사실성이나 문장 품질을 보장하지 않습니다.
- **저장소 성능**은 정해진 데이터와 질의로 벡터 저장소를 비교한 결과입니다. 실제 서비스 지연을 그대로 뜻하지 않습니다.
- **서빙 처리량**은 특정 GPU·모델 형식·동시성·측정 시간의 관측값입니다. 장시간 운영 성능이나 SLO가 아닙니다.
- **화면 회귀 검사**는 고정 응답과 브라우저 조건에서 UI 변화를 찾습니다. 실제 계정과 외부 연동까지 확인하는 종단간 검증과 구분합니다.

서로 다른 실험에서 얻은 최고 수치를 한 제품 구성에서 동시에 달성한 값처럼 합치지 않습니다.

## 근거 지도

| 판단 대상 | 원본 근거 | 조직의 해석 | 연결된 결정·구현 |
|---|---|---|---|
| 생성 모델 | [UBot-LLMTest `cd017ac0`](https://github.com/ureca-UBot/UBot-LLMTest/tree/cd017ac0fd5a99a9c453d1575950abea176beda3) | Qwen3-4B Instruct 계열을 품질과 실행 비용을 함께 볼 후속 후보로 선택 | [ADR-004](../architecture/decisions/ADR-004-llm-selection.md) · [BE 모델 런타임](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/llm/README.md) |
| 임베딩 모델 | [UBot-EmbeddingTest `eaf8113`](https://github.com/ureca-UBot/UBot-EmbeddingTest/tree/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29) | 소규모 비교에서 BGE-M3가 가장 높은 후보 검색 지표를 보여 후속 검색 실험에 사용 | [ADR-002](../architecture/decisions/ADR-002-embedding-model.md) · [BE 검색 문서](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/faq-embedding.md) |
| 리랭커 | [정정 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/reranker/docs/임베딩_vs_reranker_비교결과_1000.md) | 확대·정정 데이터에서는 BGE-M3 단독 Top-1이 비교한 리랭커 조합보다 높아 현재 FAQ 경로에서 제외 | [ADR-003](../architecture/decisions/ADR-003-reranker-strategy.md) · [BE RAG](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md) |
| 임베딩 서빙 엔진 | [분리된 서빙 결과 `ca61493`](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/ca614933c052fd413968d5735a3a5d31ebe37d92/serving-benchmark/README.md) | 짧은 구성 요소 진단에서 vLLM이 첫 서빙 후보였으나 운영 채택과 장시간 포화는 별도 검증 대상 | [BE 모델 설정](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/llm/settings.md) |
| 벡터 저장소 | [UBot-VertorDBTest `9fcbff3`](https://github.com/ureca-UBot/UBot-VertorDBTest/tree/9fcbff349648067fc4c96d56d82857f1bcccfdfd) | 가장 빠른 후보가 아니라 FAQ 원문과 벡터를 함께 관리하는 운영 단순성을 우선해 pgvector를 선택 | [ADR-001](../architecture/decisions/ADR-001-vector-database.md) · [선택 문서](https://github.com/ureca-UBot/UBot-VertorDBTest/blob/9fcbff349648067fc4c96d56d82857f1bcccfdfd/docs/07-results/decision.md) |
| 비동기 작업 복구 | [BE 신뢰성 모델](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reliability/reliability-model.md) | 질문 접수와 답변 처리를 분리하고 PostgreSQL의 상태를 기준으로 중단 작업을 회수 | [ADR-005](../architecture/decisions/ADR-005-async-chat-processing.md) · [BE 아키텍처](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/architecture/overview.md) |
| 화면 구조와 회귀 | [UBot-FE `32c542c`](https://github.com/ureca-UBot/UBot-FE/tree/32c542c152b1f6a95402e84ac092b036eaa78c5b) | 리팩터링 당시 빌드·논리 검사·화면 비교 기록이며 현재 전체 UI와 실서버 종단간 보장은 아님 | [FE 리팩터링 기록](https://github.com/ureca-UBot/UBot-FE/blob/32c542c152b1f6a95402e84ac092b036eaa78c5b/docs/FE_REFACTOR.md) |

## 주요 관측 결과

### 생성 모델

[model_test_v5](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/all_summary.md)는 Tesla T4, Ollama, temperature 0, 순차 요청, 검색 없이 고정 Context를 제공한 조건입니다. 모델마다 독립 문항 1,300건과 반복 문항 100건을 만들고 LLM Judge와 결정 규칙으로 평가했습니다. 사람 판정 보정은 끝나지 않았습니다.

| 모델 | 정답 | 정답·근거·상태 모두 충족 | Judge 환각 판정 | 평균 / p95 |
|---|---:|---:|---:|---:|
| Qwen3-4B-Instruct Q4_K_M | 77.5% | 70.5% | 26.2% | 2.61초 / 4.75초 |
| Qwen3-4B-Instruct Q8_0 | 78.8% | 71.9% | 26.5% | 3.49초 / 5.98초 |
| Gemma3-4B QAT | 67.0% | 42.0% | 31.7% | 원본 보고서 참조 |

Q8과 Q4의 정답률 차이는 통계적으로 유의하지 않았고 Q8은 순차 응답이 1.34배 느렸습니다. 이 결과는 Ollama/GGUF 조건의 모델 계열 판단 근거이며, 현재 vLLM 양자화 구성의 품질 수치가 아닙니다.

별도 GPU 서빙 탐색에서는 Qwen3-4B, 30초 폐루프 조건에서 L4 vLLM P64/U64가 9.97 RPS와 p95 9.15초를 기록했습니다. 각 지점은 짧은 단일 실행이므로 장기 처리량과 운영 SLO로 사용하지 않습니다.

### 임베딩·검색·리랭커

[5개 임베딩 모델 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/model_benchmarks/docs/임베딩모델_벤치마크_최종비교.md)는 FAQ 100개와 합성 질문 60개를 사용했습니다. BGE-M3는 Top-1 86.7%, Top-3 95.0%, Top-5 98.3%, MRR 0.916을 기록했습니다. 이 값은 후속 실험의 모델 선택 근거이며 현재 서비스 전체 검색 정확도가 아닙니다.

1,000 FAQ·235문항의 정정 비교에서는 BGE-M3 단독 Top-1이 94.5%, MRR이 0.963이었습니다. 비교한 BGE·Jina 리랭커 조합의 Top-1은 각각 91.9%, 92.8%였습니다. 후보 수와 최적화 목표가 달라지면 결론도 달라질 수 있습니다.

[임베딩 서빙 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/ca614933c052fd413968d5735a3a5d31ebe37d92/serving-benchmark/README.md)는 네 질문 묶음, 동시성 1·4·8·16·32, 구간별 64건으로 총 2,560건을 실행했고 실패는 없었습니다. 동시성 32에서 vLLM은 Ollama보다 질문 묶음별 2.98~3.73배 높은 요청 처리량을 보였습니다. 전체 RAG 지연, 장시간 포화와 운영 안정성은 측정하지 않았습니다.

### 벡터 저장소와 HNSW

[fairness-v2](https://github.com/ureca-UBot/UBot-VertorDBTest/blob/9fcbff349648067fc4c96d56d82857f1bcccfdfd/docs/07-results/fairness-v2-results-20260913.md)는 합성 한국어 벡터 10,000개, BGE-M3 1,024차원 cosine, Top-10, 동시성 10 조건으로 여러 저장소를 비교했습니다. 비슷한 Recall 구간에서 Qdrant가 pgvector보다 빠른 결과도 있었습니다. pgvector는 속도 1위가 아니라 기존 PostgreSQL 안에서 원문·벡터·재색인을 함께 운영할 수 있다는 이유로 선택했습니다.

현재 BE의 별도 HNSW 측정은 합성 1,024차원 벡터와 Top-3 조건에서 1만 벡터의 p50이 exact보다 4.64~6.19배 빨랐다고 기록합니다. 1천 벡터에서는 순차 검색보다 느렸고, 실제 FAQ 질문의 recall 재검증은 남아 있습니다. 자세한 조건은 [BE HNSW 보고서](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/FAQ_HNSW_검색_테스트_보고서.md)를 따릅니다.

### 프론트엔드 회귀 기록

[FE 리팩터링 기록](https://github.com/ureca-UBot/UBot-FE/blob/32c542c152b1f6a95402e84ac092b036eaa78c5b/docs/FE_REFACTOR.md)은 해당 시점에 포맷·린트·논리 테스트 11개·빌드 통과, 데스크톱과 모바일 49개 화면 비교를 남겼습니다. 48개 화면은 픽셀 차이가 없었고 한 화면의 관리자 날짜 영역에 89픽셀 차이가 있었습니다. 진입 JavaScript는 1,017.46kB에서 278.60kB로 분리됐습니다.

이 수치는 해당 커밋의 고정 응답 비교입니다. 이후 변경, 실제 계정, 실제 Backend와 외부 SDK를 포함한 종단간 검증을 뜻하지 않습니다.

## 제품 코드 검증과의 경계

연구 실험은 후보를 비교하고 방향을 정합니다. 현재 구현이 그 결정을 올바르게 반영했는지는 Production Repository가 검증합니다.

- Backend의 현재 기능·통합 테스트: [UBot-BE Testing](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/testing.md)
- 검색·가드·파이프라인의 시점별 보고서: [UBot-BE Docs](https://github.com/ureca-UBot/UBot-BE/tree/develop/docs)
- Frontend의 현재 빌드·브라우저 검사: [UBot-FE](https://github.com/ureca-UBot/UBot-FE)

부하·장애 주입 결과는 실행 시점의 코드 SHA, 모델, 하드웨어, 동시성, 장애 시각과 원시 결과가 함께 남아야 조직 근거로 등록합니다. 로컬 산출물만 있거나 실행 조건을 다시 확인할 수 없는 수치는 현재 제품 보장으로 올리지 않습니다.

## 인용할 때 지킬 표현

| 사용할 수 있는 표현 | 함께 밝혀야 할 조건 |
|---|---|
| BGE-M3를 후속 임베딩 모델로 선택했다 | FAQ 100개·합성 질문 60개의 소규모 비교 |
| PostgreSQL과 pgvector를 선택했다 | 더 빠른 전용 DB가 있었고 운영 단순성을 함께 고려함 |
| 1만 합성 벡터에서 BE HNSW 경로가 exact보다 빨랐다 | Testcontainers·Top-3·합성 벡터 조건, 실제 FAQ recall 미검증 |
| Qwen3-4B Instruct Q4가 v5 고정 Context 평가에서 77.5%였다 | Ollama/GGUF·T4·LLM Judge·검색 없음·사람 보정 미완료 |
| L4에서 vLLM 9.97 RPS를 관측했다 | AWQ·P64/U64·30초 단일 탐색·p95 9.15초 |
| 임베딩 단기 진단에서 vLLM이 Ollama보다 2.98~3.73배 높은 처리량을 보였다 | 2,560건의 구성 요소 측정이며 전체 RAG·장기 운영 미검증 |
| FE 리팩터링 당시 48개 화면이 픽셀 동일했다 | 해당 커밋의 고정 응답 비교이며 한 화면과 이후 변경의 재검증 미완료 |

“UBot 전체 정확도”, “운영에서 항상 몇 배 빠름”, “사람 검증과 운영 SLO 완료”처럼 실험 범위를 제품 전체로 넓히는 표현은 사용하지 않습니다.

## 새 근거를 등록하는 조건

1. 실행 저장소와 commit SHA, 작업 트리 변경 여부를 남깁니다.
2. 데이터셋 버전·분모·제외 규칙과 모델 리비전·양자화·프롬프트를 기록합니다.
3. 하드웨어·런타임·동시성·측정 시간·준비 실행·재시도 조건을 적습니다.
4. 집계표와 함께 원시 결과, 생성 명령, 성공·실패 판정 기준을 보존합니다.
5. 탐색·튜닝 데이터와 최종 평가 데이터를 구분합니다.
6. 현재 Production 구성과 실험 조건이 다르면 차이를 먼저 밝힙니다.

기술 결정의 현재 상태는 [Engineering Decisions](../architecture/decisions/README.md), 각 저장소의 역할은 [Component Map](../architecture/components.md)에서 확인합니다.
