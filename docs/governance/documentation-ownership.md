# Documentation Ownership

제품 문서와 구성요소 문서는 같은 내용을 복제하지 않습니다. 제품 의미와 저장소 사이의 연결은 이 저장소가, 실행 가능한 구현 상세는 해당 저장소가 관리합니다.

| Document | Canonical location | Owner |
|---|---|---|
| Product overview and user outcomes | `ureca-UBot/.github` | UBot maintainers |
| System architecture and component map | `ureca-UBot/.github` | FE + BE maintainers |
| Cross-repo contracts | `ureca-UBot/.github` | Producer + consumer maintainers |
| Product compatibility and support state | `ureca-UBot/.github` | UBot maintainers |
| Product decisions and evidence index | `ureca-UBot/.github` | Decision proposer + implementation owner |
| Backend API, configuration, internals, operations | `ureca-UBot/UBot-BE` | Backend maintainers |
| Frontend routes, components, browser behavior | `ureca-UBot/UBot-FE` | Frontend maintainers |
| Experiment method, raw data, and result | Research/benchmark repository | Experiment owner |
| Individual implementation contributions | `docs/governance/team-contributions.md` | Each participant for their own entry |

중요 문서는 release 또는 revision 결합, 마지막 검토일, 생성 원본 또는 자동 계약 검증 중 하나 이상을 가져야 합니다. 개인 기여는 본인이 직접 작성하며 리뷰·승인·단순 병합은 구현 기여로 기록하지 않습니다.
