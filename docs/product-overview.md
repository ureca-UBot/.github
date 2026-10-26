# Product Overview

UBot은 통신 상담에서 질문·답변·사람 상담·지식 개선이 끊어지는 문제를 하나의 서비스 흐름으로 연결합니다.

## 해결하려는 문제

- 통신 상품과 이용 조건은 FAQ만으로 답하기 어렵고 고객별 정보와 실제 조회 결과가 함께 필요합니다.
- AI가 답하지 못하면 고객이 상담사에게 같은 상황을 처음부터 다시 설명하는 일이 생깁니다.
- 답하지 못한 질문을 모아 지식으로 전환하지 않으면 같은 실패가 반복됩니다.
- 모델 처리가 느리거나 의존성이 멈췄을 때 요청이 사라지거나 답변이 중복될 수 있습니다.

UBot은 답변 근거, 대화 소유권, 상담 인계 기록, 작업 상태와 지식 개선 대상을 서버가 관리하도록 설계했습니다.

## 사용하는 사람

| 사용자 | 얻는 결과 |
|---|---|
| 고객 | 통신 상품·이용 정보·매장에 관해 질문하고, 필요한 업무와 사람 상담으로 이어갑니다. |
| 상담사 | 고객이 허용한 같은 대화의 서버 저장 기록을 넘겨받아 상담을 계속합니다. |
| 관리자 | FAQ·상품·매장·미응답·상담 안전 정책을 관리하고 개선 대상을 확인합니다. |
| 운영자 | API·Worker·데이터 저장소·모델 런타임을 구분해 관찰하고 장애에 대응합니다. |

## 기능 지도

조직 문서에서는 기능이 어떤 사용자 흐름을 만드는지만 설명합니다. 입력·권한·저장·오류 처리의 상세 계약은 연결된 Production Repository 문서에서 확인합니다.

| 기능 묶음 | 제공하는 결과 | 상세 문서 |
|---|---|---|
| AI 질문과 대화 | 근거가 있는 답변, 비동기 작업 상태, 이전 문맥을 잇는 대화 | [질문과 작업](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/chat.md) · [대화 기록](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/conversations.md) |
| RAG와 안전 검사 | FAQ·업무 자료 검색, 도구 호출, 입력·출력 검사, 근거 부족 시 답변 보류 | [RAG 파이프라인](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md) · [입력 보호](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/input-safety.md) |
| 상담사 인계 | 서버에 저장된 AI 문답·FAQ 선택·허용된 상담 기록으로 같은 대화를 이어감 | [상담사 연결과 보호](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/counsel.md) |
| 지식 개선 | 미응답 묶음, FAQ 전환, 검색 벡터 갱신, 사용·급상승 지표 | [지식 관리](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/knowledge-management.md) · [임베딩과 검색](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/faq-embedding.md) |
| 상품과 고객 업무 | 상품 탐색·가입, 회선·홈상품·부가·로밍·결합, 사용량·청구·약정 조회 | [상품과 가입 정보](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/products-and-subscriptions.md) |
| 매장과 방문 | 주변·지도 범위 매장 조회, 길찾기, 방문 예약과 취소 | [매장과 예약](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/stores-and-reservations.md) |
| 고객 지원 | 공지·배너·문의, 예약·납부·가입·사용량 알림 | [고객 지원](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/customer-support.md) |
| 운영 판단 | 지역별 문의 급증, FAQ 품질 후보, 서비스·대기열·의존성 상태 | [통신 지도](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/telemap.md) · [관측성](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/operations/observability.md) |
| 관리자 안전 정책 | 공통 금지어와 상담 위험 문장, AI 제안 후보, 회귀 검사와 승인 이력 | [가드 검토](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/guard-review.md) |

## 핵심 제품 흐름

### 1. 공식 근거로 답합니다

고객 질문을 검사하고 관련 FAQ와 필요한 서버 자료를 모읍니다. AI는 받은 근거 안에서 답하고, 서버는 결과를 다시 검사한 뒤 고객에게 보여 줍니다. 내부 근거 식별자와 권한 판단은 화면이나 모델에 맡기지 않습니다.

### 2. 개인 상황과 다음 행동을 연결합니다

인증된 고객은 자신의 가입·사용·청구·약정 정보를 조회할 수 있습니다. 상품 탐색과 가입, 매장 검색·길찾기·예약, 공지·문의·알림도 같은 웹 경험 안에서 이어집니다. 최종 상태 변경은 AI 문장이 아니라 Backend 업무 규칙이 확정합니다.

### 3. AI 상담을 사람 상담으로 이어갑니다

로그인한 고객이 상담사를 호출하면 새 상담 화면을 따로 시작하지 않습니다. Backend가 같은 대화의 AI 문답, 고객이 선택한 FAQ와 허용된 이전 상담 기록을 구성해 상담사에게 전달합니다. 검사에 실패한 상담 메시지는 상대방에게 전달하지 않습니다.

### 4. 안전 정책을 경로에 맞게 적용합니다

일반 질문은 공통 금지어와 입력 공격을 검사하고, 생성 답변은 근거·구조·위험 표현을 다시 확인합니다. 상담 메시지는 공통 금지어를 먼저 검사한 뒤 의미 기반 위험 문장 검사를 거칩니다. AI가 제안한 차단 후보는 곧바로 정책이 되지 않으며 회귀 검사와 관리자 승인을 거칩니다.

### 5. 미응답을 지식으로 바꿉니다

근거가 부족해 답하지 못한 질문은 개선 대상으로 남습니다. 유사한 질문을 묶고 관리자가 검토해 FAQ를 보강할 수 있습니다. 자주 사용되거나 갑자기 늘어난 질문과 지역별 문의 급증도 운영 판단에 활용합니다.

### 6. 장애 뒤에도 처리 상태를 찾습니다

질문 접수와 AI 실행을 분리하고, 완료 상태의 기준을 데이터베이스에 둡니다. API, Worker, 전달 계층과 모델 런타임의 역할을 나눠 용량을 독립적으로 조절하고, 중단된 작업을 저장 상태에서 다시 찾을 수 있게 합니다.

운영자는 API·Worker·PostgreSQL·Redis·모델 서버를 같은 장애로 뭉뚱그리지 않습니다. 상태·대기·실행·의존성 신호를 나눠 보고 연결된 런북으로 진단과 복구를 이어갑니다.

## 제품 원칙

- **근거가 없으면 추측보다 보류를 선택합니다.**
- **권한과 상태 변경은 Backend가 결정합니다.**
- **상담 인계는 화면 본문이 아니라 서버 기록을 사용합니다.**
- **안전 정책 변경은 자동 제안과 관리자 승인을 구분합니다.**
- **실패는 숨기지 않고 상태와 운영 신호로 남깁니다.**
- **연구 결과와 Production 보장을 구분합니다.**

## 현재 범위 밖

- 통신사의 과금·개통 원장을 대체하지 않습니다.
- 모든 질문에 답하는 범용 챗봇을 목표로 하지 않습니다.
- Research Repository의 최고 정확도나 처리량을 현재 서비스 보장값으로 사용하지 않습니다.
- 다중 리전 재해 복구와 자동 GPU 확장을 완성된 제품 계약으로 선언하지 않습니다.

## 더 알아보기

- 시스템 구성: [System Architecture](system-architecture.md)
- 저장소와 책임: [Repository Map](repository-map.md)
- 기술 선택과 근거: [Engineering Decisions](engineering-decisions.md)
- 실험과 검증 결과: [Evidence Register](evidence-register.md)
- 시나리오별 BE 동작: [UBot-BE Use Cases](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/overview/use-cases.md)
- Backend 상세 기능: [UBot-BE Product Engineering Guide](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/README.md)
- Frontend 화면과 검증: [UBot-FE Documentation](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)
