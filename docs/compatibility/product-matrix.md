# 제품 호환성 표

UBot은 아직 독립적인 제품 버전을 발행하지 않았습니다. 현재 문서는 개발 중인 `preview` 조합을 설명하며, 명시적으로 검증하지 않은 조합을 지원한다고 추정하지 않습니다.

## 버전 상태

- 현재 개발: `unversioned-preview`
- 최신 릴리스: 없음
- 권장 조합: 없음
- 지원 조합: 없음
- 검증 정도: 부분 검증

## 확인한 조합

| 제품 스냅샷 | UBot-FE | UBot-BE | 모델 런타임 | 지원 상태 | 검증 정도 | 확인 방법 |
|---|---|---|---|---|---|---|
| `unversioned-preview` | `develop` 계열 | `develop` 계열 | BE 설정 기준 | Best Effort | 부분 검증 | 구성요소별 테스트와 수동 통합 확인 |
| 그 밖의 조합 | 임의 | 임의 | 임의 | Unknown | Unknown | 검증 기록 없음 |

`Unknown`은 지원 또는 비지원이라는 뜻이 아닙니다. 제품 조합을 `Supported`로 올리려면 FE·BE의 정확한 revision, 모델 설정, 실행 환경과 제품 E2E 근거를 함께 남깁니다.

## 호환성 확인 범위

| 범위 | 계약 | 현재 근거 |
|---|---|---|
| 통신 형식 | [저장소 간 연동 계약](../architecture/contracts.md) | 구성요소별 API·통합 테스트 |
| 동작 | 사용자 흐름과 비동기 상태 전이 | [BE 지원·검증 범위](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/support-policy.md) |
| 저장 데이터 | Flyway migration과 작업 상태 | [BE Flyway 마이그레이션](https://github.com/ureca-UBot/UBot-BE/tree/f782ec7c72cc2af0631570e3b3e0d0a260072a25/src/main/resources/db/migration) |
| 설정 | FE endpoint와 BE runtime/model 설정 | 각 저장소 설정 문서 |

지원 상태의 의미와 승격 조건은 [제품 지원 정책](support-policy.md)을 따릅니다.
