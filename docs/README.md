# UBot 기능별 문서

[제품 소개](../profile/README.md) · [서비스 이용](https://u-bot.cloud) · [시나리오로 살펴보기](overview/product.md)

고객이 화면에서 시작한 행동이 서버 처리와 어떤 결과로 이어지는지 기능별로 설명합니다. 각 문서에서 관련 FE·BE 구현과 검증 기록까지 찾아갈 수 있습니다.

문서를 수정할 때는 이 목차가 연결하는 본문을 사용합니다. 본문 위치와 참고 양식의 사용 범위는 [문서 작성 원칙](governance/documentation-policy.md#문서-위치와-수정-범위)에서 확인합니다.

## 기능으로 찾아보기

| 기능 | 확인할 흐름 |
|---|---|
| [상품과 내 이용 정보](features/products-and-subscriptions.md) | 상품 탐색·채팅 조건 선택 → 번호 중복 확인·가입·변경 → 회선 선택 → 이용 정보 확인 |
| [매장 찾기와 방문 예약](features/stores-and-reservations.md) | 지도·지역 검색 → 길찾기 → 시간 선택 → 예약·취소·알림 |
| [근거 기반 AI 상담](architecture/chat-flow.md) | FAQ 준비 → 질문 입력 → 임베딩·검색 → 업무 자료·도구 조회 → 답변 검사·표시 |
| [상담사 연결](features/counselor-handoff.md) | 요청 → 저장 이력 인계 → 배정·고객 정보 확인 → 메시지 보호 → 종료·재상담 |
| [회원과 대화 기록](features/accounts-and-conversations.md) | 비회원 질문 → 로그인·대화 승계 → 저장 기록 다시 보기 |
| [FAQ·공지·문의·알림](features/customer-support.md) | 공개 FAQ 탐색 → 지역 안내 → 문의 접수·답변 → 이용 알림·읽음 처리 |
| [FAQ와 지식 개선](features/knowledge-improvement.md) | FAQ 관리·색인, 미응답 그룹화·전환·재검증, 인기·지역 문의 분석 |
| [질문·답변과 상담 보호](features/ai-safety.md) | 입력·출력·상담 검사 → 정책 후보 검증 → 관리자 승인 |
| [배포와 서비스 운영](features/service-operations.md) | CI/CD → 상태·지표 확인 → 장애 알림 → 복구·결과 확인, 비용 판단 |

## 시나리오를 따라 읽기

- **고객의 질문과 행동:** [회원과 대화](features/accounts-and-conversations.md) → [AI 상담](architecture/chat-flow.md) → [상품·이용 정보](features/products-and-subscriptions.md) 또는 [매장 방문](features/stores-and-reservations.md) → [상담사 연결](features/counselor-handoff.md)
- **관리자의 개선:** [미응답·FAQ·문의 분석](features/knowledge-improvement.md) → [안전 정책 검토](features/ai-safety.md) → [새 지식으로 답변](architecture/chat-flow.md)
- **배포 후 운영:** [배포·관측·장애 대응](features/service-operations.md) → [시스템 구성](architecture/overview.md) → [실험과 검증 근거](proof/evidence-register.md)

## 설계와 검증을 더 알아보기

| 찾는 내용 | 문서 |
|---|---|
| FE·BE·모델·데이터 저장소의 관계 | [시스템 구성](architecture/overview.md) |
| 기능별 데이터와 테이블 간 연결 | [전체 ERD와 색상별 설명](architecture/data-model.md) |
| 제품과 실험 저장소의 역할 | [저장소 지도](architecture/components.md) |
| FE·BE 연동에서 지켜야 할 약속 | [연동 계약](architecture/contracts.md) |
| 주요 기술 선택의 이유 | [기술 결정](architecture/decisions/README.md) |
| 모델·검색·서빙·부하·화면 검증 결과 | [실험과 검증 근거](proof/evidence-register.md) |
| 제품을 직접 실행하는 순서 | [실행 안내](getting-started/quickstart.md) |
| 제품에서 사용하는 용어 | [용어집](reference/glossary.md) |

## 구현 문서

- Backend: [기능별 상세 문서](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/README.md) · [실행 안내](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/quickstart.md)
- Frontend: [README](https://github.com/ureca-UBot/UBot-FE/blob/develop/README.md) · [화면·연동 문서](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)
- 실험 원본: [생성 모델](https://github.com/ureca-UBot/UBot-LLMTest) · [임베딩·검색](https://github.com/ureca-UBot/UBot-EmbeddingTest) · [벡터 저장소](https://github.com/ureca-UBot/UBot-VertorDBTest)
- 서비스 검증: [부하·장애 복구·Discord 알림·통신지도·미응답](https://github.com/ureca-UBot/UBot-ServerTest)

## 팀 기록

- [참여 멤버와 구현 기여](governance/team-contributions.md): 각자 맡은 내용과 구현 근거 작성
- [멘토링 질문과 답변](governance/mentoring.md): 1~3차 멘토링 기록
