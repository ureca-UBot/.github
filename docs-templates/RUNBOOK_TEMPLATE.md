# Runbook: 장애 이름

## Purpose

이 Runbook이 다루는 장애와 사용자 영향을 설명합니다.

## Scope

- Affected components:
- Not covered:
- Required access:
- Risk level:

## Trigger and Symptoms

| 신호 | 확인 위치 | 판단 기준 |
|---|---|---|
|  |  |  |

지표가 없다는 사실을 정상 또는 0으로 해석하지 않습니다.

## First Response

1. 변경 전에 시각, 배포 버전, 지표, 로그와 의존성 상태를 보존합니다.
2. 사용자 영향과 데이터 손상 가능성을 구분합니다.
3. 중복 처리나 유실 위험이 있으면 새 작업 투입을 제한합니다.

## Diagnosis

각 단계에 명령, 예상 결과와 해석을 함께 적습니다.

### Step 1

```shell
# read-only command
```

Expected:

Interpretation:

## Mitigation

### Action

- Purpose:
- User impact:
- Data impact:
- Stop condition:
- Rollback:

```shell
# command
```

Expected:

파괴적 명령, 데이터 삭제와 강제 재처리는 별도 승인과 정확한 대상 확인 없이 넣지 않습니다.

## Recovery Validation

- [ ] 사용자가 호출하는 경로가 정상 응답
- [ ] 대기 작업이 줄어듦
- [ ] 중복 결과가 없음
- [ ] 유실 작업이 없음
- [ ] 의존성 지표와 애플리케이션 지표가 함께 정상
- [ ] 관찰 시간 동안 재발하지 않음

## Escalation

| 조건 | 전달 대상 | 함께 전달할 증거 |
|---|---|---|
|  |  |  |

## Follow-up

- Incident record:
- Root cause:
- Permanent fix:
- Test or alert added:
- Documentation updated:
