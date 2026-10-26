# 배포에서 장애 대응과 비용 판단까지

[전체 기능](../README.md) · [시스템 구성](../architecture/overview.md) · [AI 상담](../architecture/chat-flow.md)

고객이 질문하고 예약·상품·상담 기능을 사용하는 동안 운영자는 서비스 상태를 확인합니다. 개발 단계의 검증, 배포, 지표와 알림, 장애 복구를 하나의 흐름으로 연결합니다.

## 변경을 서비스에 반영합니다

CI가 변경한 코드를 빌드·테스트합니다. AWS 배포를 활성화한 대상 브랜치에서 push 검증이 성공하면 해당 버전의 이미지를 발행하고 서버 배포를 실행합니다. 배포 뒤에는 API 상태와 공개 조회, 답변 처리와 관측 대상의 상태를 확인합니다.

PR 검사가 성공한 것만으로 운영에 배포하지 않습니다. FE와 BE는 각자의 빌드·배포 구성을 사용하며, BE 배포가 데이터 저장소나 GPU 용량까지 새로 구성하는 작업은 아닙니다.

## 평상시 상태에서 장애 대응으로 이어갑니다

| 운영자의 행동 | 화면·알림 | 서버에서 확인하는 근거 |
|---|---|---|
| 서비스 상태 확인 | 관리자 운영 화면과 지표 | 요청 결과·응답 시간·의존 서비스 상태 |
| 답변 지연 확인 | 대기·실행·모델 지연 지표 | 저장된 작업과 실행 단계 |
| 이상 신호 확인 | 구성한 채널의 장애 알림 | 알림 규칙과 관련 지표·로그 |
| 원인 진단과 조치 | 장애별 대응 절차 | API·DB·Redis·모델의 상태 구분 |
| 복구 결과 확인 | 기존 요청과 새 요청의 최종 상태 | DB에 저장한 완료·실패 결과 |

운영 화면의 서비스 지표와 FAQ 품질 지표는 목적이 다릅니다. 응답이 느린지 확인하는 일과 FAQ가 질문을 해결했는지 확인하는 일을 나눠 봅니다.

## 중단된 요청을 어떻게 다루나요?

접수한 작업과 최종 결과를 DB에 남깁니다. 전달 신호가 사라지거나 실행 중인 프로세스가 종료되면 저장된 상태를 기준으로 다시 처리합니다. 늦게 돌아온 이전 실행이 새 결과를 덮어쓰지 못하도록 확인합니다.

Redis 조회 실패와 DB 조회 실패도 구분합니다. 모델 연결이 잠시 끊어지면 정해진 기한 안에서 재시도하고, 끝내 복구하지 못하면 실패 상태를 확정합니다. 재처리 과정에서 모델 계산이 다시 실행될 수 있으므로 작업 유실과 중복 답변 저장을 함께 확인합니다.

[실제 LLM 장애 실험](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/evidence/fault-recovery-20261023.md)은 처리 중인 요청에 장애를 주고 복구·최종 결과를 확인한 기록입니다. 측정한 환경의 결과이며 운영 환경의 복구 시간 보장값은 아닙니다.

## 비용을 판단하는 세 가지 지점

- **생성 호출을 줄이는 경로:** 조건에 맞는 공식 FAQ는 등록 답변을 직접 반환합니다. 질문 임베딩과 검색은 계속 수행합니다.
- **계산 결과의 재사용:** 검색 중 만든 벡터를 같은 조건의 후속 처리에서 활용해 중복 임베딩을 줄입니다.
- **자원별 용량 조절:** API·답변 처리·모델 실행을 나눠 요청 접수량과 계산량에 따라 자원을 조절합니다. 실행 동시성만 높인다고 모델 처리량이 같은 비율로 늘지는 않습니다.

최종 판단에는 인스턴스 가격뿐 아니라 실행 시간·트래픽·응답 완료 시간·오류를 함께 봅니다. Terraform에 정의한 자원이 모두 상시 실행 중이라는 뜻은 아니며, 자동 확장 가동 여부와 실제 비용은 배포 환경에서 확인해야 합니다.

## 상세 구현과 검증

- Backend: [운영 기능과 검증](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/features/service-operations.md) · [배포](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/deploy.md) · [장애별 런북](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/runbooks/README.md) · [Terraform](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/infra/terraform/README.md)
- Frontend: [운영 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/admin/operation/pages/OperationDashboardPage.tsx) · [FE 배포](https://github.com/ureca-UBot/UBot-FE/blob/develop/docs/AWS_DEPLOY.md)
- 선택 근거: [작업 접수·처리 분리](../architecture/decisions/ADR-005-async-chat-processing.md) · [모델·서빙 실험](../proof/evidence-register.md)
