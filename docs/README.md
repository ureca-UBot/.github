# UBot Documentation Portal

UBot의 제품 문서와 각 구성요소 저장소의 구현 문서를 연결하는 시작점입니다. 제품 의미와 저장소 사이의 관계는 여기서, 실행 가능한 상세 계약은 실제 코드를 소유한 저장소에서 관리합니다.

## 제품 이해

| 질문 | 문서 |
|---|---|
| UBot은 누구의 어떤 문제를 해결하는가? | [Product Overview](overview/product.md) |
| 질문이 답변·상담·지식 개선으로 어떻게 이어지는가? | [Chat and RAG Flow](architecture/chat-flow.md) |
| FE·BE·모델·데이터 저장소는 어떻게 연결되는가? | [System Architecture](architecture/overview.md) |
| 어떤 저장소가 무엇을 책임지는가? | [Component Map](architecture/components.md) · [Generated Registry](../generated/components.md) · [Canonical Data](../data/product.yaml) |
| 저장소 사이에서 무엇을 계약으로 보는가? | [Cross-repo Contracts](architecture/contracts.md) |

## 결정, 호환성, 근거

| 질문 | 문서 |
|---|---|
| 주요 기술을 왜 선택했는가? | [Engineering Decisions](architecture/decisions/README.md) |
| 실험 결과를 어디까지 인용할 수 있는가? | [Evidence Register](proof/evidence-register.md) · [Claims Registry](proof/claims.yaml) |
| 어떤 제품 조합을 지원한다고 말할 수 있는가? | [Compatibility Matrix](compatibility/product-matrix.md) · [Support Policy](compatibility/support-policy.md) |
| 현재 제품 릴리스 상태는 무엇인가? | [Generated Release Summary](../generated/release-summary.md) · [Product Version Manifest](releases/product-versions.yaml) |

## 운영과 관리

| 질문 | 문서 |
|---|---|
| 처음 어디서 실행해야 하는가? | [Product Quickstart](getting-started/quickstart.md) |
| 문서의 기준 위치와 담당은 어디인가? | [Documentation Ownership](governance/documentation-ownership.md) |
| 문서를 어떻게 작성하고 갱신하는가? | [Documentation Policy](governance/documentation-policy.md) |
| 공통 용어는 무엇을 뜻하는가? | [Glossary](reference/glossary.md) |
| 참여자가 자신의 구현 기여를 어디에 기록하는가? | [Team Contributions](governance/team-contributions.md) |

생성 문서(`generated/`)는 직접 수정하지 않습니다. 구성요소·릴리스·claim 원본을 바꾼 뒤 `python scripts/docs_tool.py generate`로 갱신하며, `validate --mode template`은 구조와 링크를, `validate --mode publish`는 공개 준비 조건을 검사합니다.

## 구성요소 문서

- Backend: [UBot-BE README](https://github.com/ureca-UBot/UBot-BE/blob/develop/README.md) · [Maintainer Guide](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/README.md)
- Frontend: [UBot-FE README](https://github.com/ureca-UBot/UBot-FE/blob/develop/README.md) · [Frontend Docs](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)
- LLM 실험: [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest)
- Embedding·Retrieval 실험: [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest)
- Vector DB 벤치마크: [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest)

## Architecture Decision Records

- [ADR-001: PostgreSQL + pgvector](architecture/decisions/ADR-001-vector-database.md)
- [ADR-002: BGE-M3](architecture/decisions/ADR-002-embedding-model.md)
- [ADR-003: 현재 FAQ 검색에서 Reranker 제외](architecture/decisions/ADR-003-reranker-strategy.md)
- [ADR-004: Qwen3-4B Instruct 계열](architecture/decisions/ADR-004-llm-selection.md)
- [ADR-005: 질문 접수와 답변 처리 분리](architecture/decisions/ADR-005-async-chat-processing.md)

## Templates

- [ADR](../docs-templates/ADR_TEMPLATE.md)
- [Benchmark](../docs-templates/BENCHMARK_TEMPLATE.md)
- [Runbook](../docs-templates/RUNBOOK_TEMPLATE.md)
- [Troubleshooting](../docs-templates/TROUBLESHOOTING_TEMPLATE.md)
