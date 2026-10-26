# Product Compatibility Matrix

UBot은 아직 독립적인 제품 버전을 발행하지 않았습니다. 현재 문서는 개발 중인 `preview` 조합을 설명하며, 명시적으로 검증하지 않은 조합을 지원한다고 추정하지 않습니다.

## Release Semantics

- Current development: `unversioned-preview`
- Latest released: 없음
- Recommended: 없음
- Supported: 없음
- Knowledge state: 부분 검증

## Known Combinations

| Product snapshot | UBot-FE | UBot-BE | Model runtime | Support state | Knowledge state | Verification |
|---|---|---|---|---|---|---|
| `unversioned-preview` | `develop` 계열 | `develop` 계열 | BE 설정 기준 | Best Effort | Partially Verified | 구성요소별 테스트와 수동 통합 확인 |
| 그 밖의 조합 | 임의 | 임의 | 임의 | Unknown | Unknown | 검증 기록 없음 |

`Unknown`은 지원 또는 비지원이라는 뜻이 아닙니다. 제품 조합을 `Supported`로 올리려면 FE·BE의 정확한 revision, 모델 설정, 실행 환경과 제품 E2E 근거를 함께 남깁니다.

## Compatibility Surfaces

| Surface | Contract | Current proof |
|---|---|---|
| Wire | [Cross-repo Contracts](../architecture/contracts.md) | 구성요소별 API·통합 테스트 |
| Behavior | 사용자 흐름과 비동기 상태 전이 | [BE Testing](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/testing.md) |
| Persisted data | Flyway migration과 작업 상태 | [BE Database Reference](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reference/database.md) |
| Config | FE endpoint와 BE runtime/model 설정 | 각 저장소 설정 문서 |

지원 상태의 의미와 승격 조건은 [Product Support Policy](support-policy.md)를 따릅니다.
