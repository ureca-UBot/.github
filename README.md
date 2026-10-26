# UBot Product Documentation

이 저장소는 UBot 제품 문서의 기준 위치입니다. 제품의 목적, 구성요소 간 책임, 교차 저장소 계약, 호환성, 제품 수준 기술 결정과 검증 근거를 관리합니다. 사용자가 보는 단위는 Product, 구현 책임은 Component, 코드 위치는 Repository, 배포 단위는 Artifact로 구분합니다.

| 찾는 내용 | 기준 문서 |
|---|---|
| 제품이 해결하는 문제와 사용자 흐름 | [Product Overview](docs/overview/product.md) |
| 전체 시스템과 채팅·RAG 흐름 | [System Architecture](docs/architecture/overview.md) · [Chat Flow](docs/architecture/chat-flow.md) |
| 저장소와 구성요소의 책임 | [Generated Component Registry](generated/components.md) · [Component Map](docs/architecture/components.md) |
| 저장소 사이의 계약 | [Cross-repo Contracts](docs/architecture/contracts.md) |
| 기술 선택과 근거 | [Engineering Decisions](docs/architecture/decisions/README.md) · [Evidence Register](docs/proof/evidence-register.md) |
| 지원·검증된 제품 조합 | [Compatibility Matrix](docs/compatibility/product-matrix.md) · [Support Policy](docs/compatibility/support-policy.md) |
| 문서 소유권과 작성 규칙 | [Documentation Ownership](docs/governance/documentation-ownership.md) · [Documentation Policy](docs/governance/documentation-policy.md) |
| 전체 문서 탐색 | [Documentation Portal](docs/README.md) |

## 검증 상태

- 구성요소·Repository·Artifact의 단일 원본은 [`data/product.yaml`](data/product.yaml)입니다.
- 검증된 제품 조합은 [`docs/releases/product-versions.yaml`](docs/releases/product-versions.yaml), claim과 적용 범위는 [`docs/proof/claims.yaml`](docs/proof/claims.yaml)을 기준으로 합니다.
- 현재 `development-preview`는 권장 배포 조합이 아니며 contract test, 제품 E2E, upgrade, 실제 환경 propagation이 모두 `NOT_EVALUATED`입니다.
- 연구 저장소의 수치는 제품 릴리스 보장값이 아닙니다. 검증 전 claim은 `DRAFT`로 유지합니다.

생성된 표는 직접 고치지 않습니다. 원본 YAML을 수정한 뒤 다음 명령으로 생성·검사합니다.

```bash
python -m pip install -r requirements-docs.txt
python scripts/docs_tool.py generate
python scripts/docs_tool.py validate --mode template
python -m unittest discover -s tests -v
```

`template` 검증 성공은 제품 품질이나 공개 준비 완료를 뜻하지 않습니다. 공개 gate는 실제 owner, 증거, 권장 release profile과 propagation 확인이 준비된 뒤에만 통과해야 합니다.

API 필드, 환경변수, 실행 명령, 클래스, 데이터베이스 제약과 운영 절차는 해당 구성요소 저장소가 관리합니다. Backend 문서는 [UBot-BE](https://github.com/ureca-UBot/UBot-BE), Frontend 문서는 [UBot-FE](https://github.com/ureca-UBot/UBot-FE)를 기준으로 확인합니다.
