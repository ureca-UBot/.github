# UBot Product Documentation

이 저장소는 UBot 제품 문서의 기준 위치입니다. 제품의 목적, 구성요소 간 책임, 교차 저장소 계약, 호환성, 제품 수준 기술 결정과 검증 근거를 관리합니다.

| 찾는 내용 | 기준 문서 |
|---|---|
| 제품이 해결하는 문제와 사용자 흐름 | [Product Overview](docs/overview/product.md) |
| 전체 시스템과 채팅·RAG 흐름 | [System Architecture](docs/architecture/overview.md) · [Chat Flow](docs/architecture/chat-flow.md) |
| 저장소와 구성요소의 책임 | [Component Catalog](COMPONENT_CATALOG.yaml) · [Component Map](docs/architecture/components.md) |
| 저장소 사이의 계약 | [Cross-repo Contracts](docs/architecture/contracts.md) |
| 기술 선택과 근거 | [Engineering Decisions](docs/architecture/decisions/README.md) · [Evidence Register](docs/proof/evidence-register.md) |
| 지원·검증된 제품 조합 | [Compatibility Matrix](docs/compatibility/product-matrix.md) · [Support Policy](docs/compatibility/support-policy.md) |
| 문서 소유권과 작성 규칙 | [Documentation Ownership](docs/governance/documentation-ownership.md) · [Documentation Policy](docs/governance/documentation-policy.md) |
| 전체 문서 탐색 | [Documentation Portal](docs/README.md) |

API 필드, 환경변수, 실행 명령, 클래스, 데이터베이스 제약과 운영 절차는 해당 구성요소 저장소가 관리합니다. Backend 문서는 [UBot-BE](https://github.com/ureca-UBot/UBot-BE), Frontend 문서는 [UBot-FE](https://github.com/ureca-UBot/UBot-FE)를 기준으로 확인합니다.
