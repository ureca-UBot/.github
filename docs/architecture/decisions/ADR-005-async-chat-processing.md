# ADR-005: 질문 접수와 답변 처리 분리

- Status: Accepted
- Date: 2026-10
- Related Repositories: UBot-BE, UBot-FE

## Context

모델 응답 시간은 일반 API보다 길고 GPU 처리량에 따라 크게 달라집니다. API 확장과 AI 실행 용량을 한 프로세스 수에 묶으면 고객 요청 수명, 장애 격리와 비용 조절이 어려워집니다.

## Decision

질문 접수와 상태 조회는 API가 담당하고, 검색·모델 호출·결과 확정은 별도 실행 역할이 비동기로 처리합니다. 작업 전달은 반복될 수 있지만 작업 상태와 최종 결과의 기준은 Backend 데이터 저장소에 둡니다. 현재 실행 소유자만 결과를 확정합니다.

## Alternatives Considered

| 후보 | 채택하지 않은 이유 |
|---|---|
| 같은 API 요청 안에서 답변까지 생성(동기 처리) | 모델 응답을 기다리는 동안 요청 연결을 점유하고, API와 모델 실행 용량을 따로 조절할 수 없으며, 프로세스가 멈추면 진행 중인 답변을 되살릴 기준이 없음 |
| SSE로 생성 중인 답변을 바로 전송 | BE #82 리뷰에서 SSE 없이 완성된 답변을 상태 조회로 돌려주기로 함([코드 구조와 요청 흐름](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/architecture.md)). 답변은 출력 검사를 통과한 뒤에만 사용자에게 보여 주므로 생성 중인 문장을 그대로 흘려보내지 않음 |

## Evidence

- [로컬 장애 복구 400건](https://github.com/ureca-UBot/UBot-ServerTest/blob/07217660fa2aafcd671600905c62e3a2a8f0226a/fault-recovery/README.md): Worker·Redis·PostgreSQL·vLLM을 각각 100건 처리 중에 중단한 뒤 400건 모두 최종 답변을 저장했고, 유실·중복 저장은 0건이었습니다.
- [AWS 채팅 부하 6,000건](../../proof/evidence-register.md#aws-채팅-부하와-관리자-화면-검증): 6,000건을 모두 접수했고, 작업 ID를 DB와 대조한 누락·상태 불일치는 0건이었습니다.

## Rationale

- API와 답변 처리 용량을 독립적으로 조절할 수 있습니다.
- 느린 모델 호출이 고객의 접수 연결을 계속 점유하지 않습니다.
- 답변 처리가 중단돼도 저장된 작업 상태에서 미완료 작업을 찾을 수 있습니다.
- GPU 서버의 가변적 운영이 웹 API 배포 단위에 직접 묶이지 않습니다.
- 답변 처리와 모델 자원을 트래픽·비용 조건에 맞춰 API와 별도로 조절할 수 있습니다.

## Trade-offs

- Frontend는 작업 식별자로 상태를 조회하고 실패·취소 상태를 처리해야 합니다.
- 중복 전달 가능성을 고려해 실행 소유권과 멱등성 계약이 필요합니다.
- 전달 계층과 데이터베이스의 장애를 각각 관측하고 복구해야 합니다.

## Production Implementation

[UBot-BE Architecture](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/architecture.md) · [Reliability Model](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/reliability-model.md) · [UBot-FE](https://github.com/ureca-UBot/UBot-FE)

## Revisit Triggers

- 비동기 UX가 제품 요구를 충족하지 못할 때
- 전달·저장 계층의 운영 비용이 이점보다 커질 때
- 별도 실행 계층이 없어도 모델 응답 시간을 안정적으로 제한할 수 있을 때
