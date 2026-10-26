# UBot Documentation Portal

조직 문서는 UBot의 전체 맥락과 Repository 사이의 연결을 설명합니다. 구현 상세, 실행 명령과 현재 기본값은 각 Repository 문서에서 확인합니다.

## Start Here

| 질문 | 문서 |
|---|---|
| UBot은 무엇을 만들고 누구에게 어떤 결과를 주는가? | [Product Overview](product-overview.md) |
| 질문이 FE에서 임베딩·검색·업무 자료·답변·상담으로 어떻게 이어지는가? | [Chat and RAG Flow](chat-flow.md) |
| 전체 시스템과 데이터·AI 흐름은 어떻게 연결되는가? | [System Architecture](system-architecture.md) |
| 어떤 Repository를 봐야 하는가? | [Repository Map](repository-map.md) |
| 주요 기술을 왜 선택했는가? | [Engineering Decisions](engineering-decisions.md) |
| 실험과 검증 결과를 어디까지 근거로 사용할 수 있는가? | [Evidence Register](evidence-register.md) |
| 조직 문서를 어떻게 작성하고 갱신하는가? | [Documentation Policy](documentation-policy.md) |
| 공통 용어는 무엇을 뜻하는가? | [Glossary](glossary.md) |

## Decision Records

[Decision Index](engineering-decisions.md)에서 선택한 기술과 Production 구현을, [Evidence Register](evidence-register.md)에서 실험 조건·관측 결과·해석 한계를 함께 찾을 수 있습니다.

- [ADR-001: PostgreSQL + pgvector](decisions/ADR-001-vector-database.md)
- [ADR-002: BGE-M3](decisions/ADR-002-embedding-model.md)
- [ADR-003: 현재 FAQ 검색에서 Reranker 제외](decisions/ADR-003-reranker-strategy.md)
- [ADR-004: Qwen3-4B Instruct 계열](decisions/ADR-004-llm-selection.md)
- [ADR-005: 질문 접수와 답변 처리 분리](decisions/ADR-005-async-chat-processing.md)

## Repository Documentation

- Backend 제품·API·운영: [UBot-BE README](https://github.com/ureca-UBot/UBot-BE/blob/develop/README.md) · [Technical Docs](https://github.com/ureca-UBot/UBot-BE/tree/develop/docs)
- Frontend 화면·브라우저 검증: [UBot-FE README](https://github.com/ureca-UBot/UBot-FE/blob/develop/README.md) · [Frontend Docs](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)
- LLM 실험: [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest)
- Embedding·Retrieval 실험: [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest)
- Vector DB Benchmark: [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest)

## Templates

- [ADR](../docs-templates/ADR_TEMPLATE.md)
- [Benchmark](../docs-templates/BENCHMARK_TEMPLATE.md)
- [Runbook](../docs-templates/RUNBOOK_TEMPLATE.md)
- [Troubleshooting](../docs-templates/TROUBLESHOOTING_TEMPLATE.md)
