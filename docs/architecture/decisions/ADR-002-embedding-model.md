# ADR-002: Embedding 모델로 BGE-M3 사용

- Status: Accepted
- Date: 2026-09
- Related Repositories: UBot-EmbeddingTest, UBot-BE

## Context

한국어 통신 FAQ의 다양한 표현을 같은 지식으로 연결하려면 dense Embedding 모델을 선택하고, Production에서 같은 차원과 모델 식별자를 일관되게 관리해야 합니다.

## Decision

FAQ 검색과 관련 벡터 처리의 Embedding 모델로 BGE-M3를 사용합니다.

## Alternatives Considered

FAQ 100개·합성 질문 60개로 비교한 결과입니다([최종 비교표](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/model_benchmarks/docs/임베딩모델_벤치마크_최종비교.md)).

| 후보 | Top-1 | MRR | 초당 처리량 | 채택하지 않은 이유 |
|---|---:|---:|---:|---|
| Qwen3-Embedding-0.6B | 75.0% | 84.4% | 37건 | 검색 정확도가 가장 낮고 처리량도 낮음 |
| multilingual-e5-large | 81.7% | 87.7% | 100건 | 처리량은 비슷하지만 정확도가 낮음 |
| gte-multilingual-base | 76.7% | 83.2% | 155건 | 가장 빠르지만 정확도가 낮고 Ollama를 지원하지 않음 |
| EmbeddingGemma-300M | 83.3% | 89.4% | 36건 | 정확도가 두 번째였지만 처리량이 BGE-M3의 약 3분의 1 |
| **BGE-M3 (선택)** | 86.7% | 91.6% | 100건 | 정확도가 가장 높고 처리량도 상위권 |

## Evidence

[초기 모델 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/eaf81130d837a1dbebb0ad4272eebfe2a6d32d29/model_benchmarks/docs/임베딩모델_벤치마크_최종비교.md)는 제한된 FAQ와 합성 질문에서 다섯 모델의 Top-K와 MRR을 비교했습니다. BGE-M3가 가장 높아 후속 검색 실험의 기준 모델이 됐습니다.

## Trade-offs

- 초기 결과는 소규모 합성 질문에 한정되며 현재 서비스 전체 정확도를 보장하지 않습니다.
- 질문 표현, FAQ corpus와 평가 label이 바뀌면 다시 검증해야 합니다.
- 모델 revision이나 serving engine이 달라지면 vector profile을 분리해 관리해야 합니다.

## Production Implementation

[UBot-BE Model Runtime](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/infra/llm/README.md) · [Embedding Profile](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/features/faq-management.md)

## Revisit Triggers

- 독립 검토한 실제 질문 holdout에서 다른 모델이 일관되게 우수할 때
- 지연·메모리·운영 비용이 제품 목표를 충족하지 못할 때
- 모델 revision 변경으로 기존 vector와 호환되지 않을 때
