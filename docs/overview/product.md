---
title: 'Product Overview'
type: product-documentation
status: active
owner: 'UBot maintainers'
applicability: development-preview
last_reviewed: '2026-10-26'
---

# Product Overview

UBot은 상품 탐색과 가입, 이용 정보 확인, 매장 방문, 고객 지원, AI 안내와 사람 상담이 서로 끊기는 문제를 하나의 서비스 흐름으로 연결합니다.

## 해결하려는 문제

- 상품을 찾은 뒤 가입으로, 매장을 찾은 뒤 길찾기와 예약으로 자연스럽게 이어지기 어렵습니다.
- 가입 상품·사용량·청구·약정처럼 고객마다 다른 정보는 본인 확인과 실제 서버 조회가 필요합니다.
- 공지·문의·예약·납부·가입·사용량 알림이 흩어져 있으면 고객과 관리자가 진행 상태를 놓치기 쉽습니다.
- AI가 답하지 못하면 고객이 상담사에게 같은 상황을 처음부터 다시 설명하는 일이 생깁니다.
- 답하지 못한 질문을 모아 FAQ로 전환하지 않으면 같은 문의와 실패가 반복됩니다.

UBot은 회원과 비회원의 대화, 상품·매장·예약·문의 상태, 답변 근거, 상담 인계 기록과 지식 개선 대상을 서버가 일관되게 관리하도록 설계했습니다.

## 사용하는 사람

| 사용자 | 얻는 결과 |
|---|---|
| 고객 | 상품을 찾고 가입·이용 정보를 확인하며, 매장 방문·문의·알림과 사람 상담으로 이어갑니다. |
| 상담사 | 고객이 허용한 같은 대화의 서버 저장 기록을 넘겨받아 상담을 계속합니다. |
| 관리자 | FAQ·상품·매장·미응답·상담 안전 정책을 관리하고 개선 대상을 확인합니다. |
| 운영자 | 서비스·데이터 저장소·모델 런타임을 구분해 관찰하고 장애에 대응합니다. |

## 기능 지도

조직 문서에서는 기능이 어떤 사용자 흐름을 만드는지만 설명합니다. 입력·권한·저장·오류 처리의 상세 계약은 연결된 Production Repository 문서에서 확인합니다.

| 기능 묶음 | 제공하는 결과 | 상세 문서 |
|---|---|---|
| 회원·비회원과 대화 | 회원 인증과 프로필, 비회원 질문 한도, 로그인 뒤 대화 승계 | [회원과 인증](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/identity.md) · [대화 기록](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/conversations.md) |
| 상품과 고객 업무 | 상품 탐색·가입, 회선·홈상품·부가·로밍·결합, 사용량·청구·약정 조회 | [상품과 가입 정보](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/products-and-subscriptions.md) |
| 매장과 방문 | 주변·지도 범위 매장 조회, 길찾기, 방문 예약과 취소 | [매장과 예약](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/stores-and-reservations.md) |
| 고객 지원 | 공지·배너·문의, 예약·납부·가입·사용량 알림 | [고객 지원](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/customer-support.md) |
| FAQ와 지식 개선 | FAQ·카테고리·버전·사용 이력, 미응답 묶음과 FAQ 전환, 인기·급상승 순위 | [지식 관리](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/knowledge-management.md) |
| 지역별 문의 흐름 | 지역과 의미가 비슷한 질문의 급증 탐지, 관리자 알림과 처리 | [통신 지도](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/telemap.md) |
| FAQ 기반 안내 | FAQ·업무 자료 검색, 필요한 서버 기능 호출, 근거 부족 시 답변 보류 | [채팅과 RAG 전체 흐름](../architecture/chat-flow.md) · [BE RAG 파이프라인](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md) |
| 상담사 인계 | 서버에 저장된 AI 문답·FAQ 선택·허용된 상담 기록으로 같은 대화를 이어감 | [상담사 연결과 보호](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/counsel.md) |
| 관리자 안전 정책 | 공통 금지어와 상담 위험 문장, AI 제안 후보, 회귀 검사와 승인 이력 | [가드 검토](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/guard-review.md) |
| 서비스 운영 | 업무 상태와 처리 현황, 지표·로그·알림, 장애별 확인 절차 | [관측성](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/operations/observability.md) |

## 핵심 제품 흐름

### 1. 고객의 통신 생활을 한곳에서 이어갑니다

회원은 상품을 비교하고 가입하며 자신의 회선·홈상품·부가서비스·로밍·결합상품, 사용량·청구·약정을 확인합니다. 비회원도 질문할 수 있고, 로그인하면 기존 대화를 회원 계정에서 이어 봅니다.

### 2. 매장 탐색을 실제 방문까지 연결합니다

고객은 지역·현재 위치·지도 범위와 서비스 유형으로 매장을 찾습니다. 선택한 매장까지 도보·자동차·대중교통 경로를 확인하고 가능한 시간에 방문을 예약하거나 취소할 수 있습니다.

### 3. 공지와 문의, 알림으로 진행 상태를 놓치지 않습니다

고객은 공지와 배너를 확인하고 일대일 문의를 남겨 답변을 받습니다. 예약·납부·가입·사용량 변화는 알림으로 이어지며, 읽음 상태도 같은 계정에서 관리합니다.

### 4. 공식 근거로 질문에 답합니다

질문과 관련된 FAQ를 찾고, 필요한 경우 상품·고객·매장 정보를 서버에서 확인해 답변 자료로 사용합니다. 답변은 받은 근거와 허용된 도구 결과 안에서 만들며, 근거가 부족하면 추측하지 않고 보류합니다.

### 5. AI 안내를 사람 상담으로 이어갑니다

로그인한 고객이 상담사를 호출하면 새 상담을 처음부터 시작하지 않습니다. Backend가 같은 대화의 AI 문답, 고객이 선택한 FAQ와 허용된 이전 상담 기록을 구성해 상담사에게 전달합니다. 검사에 실패한 상담 메시지는 상대방에게 전달하지 않습니다.

### 6. 미응답을 다음 개선으로 바꿉니다

근거가 부족해 답하지 못한 질문은 개선 대상으로 남습니다. 유사한 질문을 묶고 관리자가 검토해 FAQ를 보강할 수 있습니다. 자주 사용되거나 갑자기 늘어난 질문과 지역별 문의 급증도 운영 판단에 활용합니다.

### 7. 안전 정책은 관리자의 판단으로 확정합니다

일반 질문, 생성 답변과 상담 메시지는 각 경로에 맞는 검사를 거칩니다. AI가 제안한 차단 후보는 곧바로 정책이 되지 않으며 회귀 검사와 관리자 승인을 거칩니다. 상품·매장·FAQ 변경도 해당 관리 기능과 이력 안에서 처리합니다.

## 기능을 받치는 구조

질문 접수와 답변 처리를 분리하고, 완료 상태의 기준을 데이터베이스에 둡니다. 서비스와 모델 실행 역할을 나눠 용량을 조절하고 중단된 작업을 저장 상태에서 다시 찾습니다.

운영자는 애플리케이션·PostgreSQL·Redis·모델 서버를 같은 장애로 뭉뚱그리지 않습니다. 상태·대기·실행·의존성 신호를 나눠 보고 연결된 런북으로 진단과 복구를 이어갑니다. 이 구조는 각 사용자 흐름이 완료 상태를 잃지 않고 이어지도록 뒷받침합니다.

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

- 시스템 구성: [System Architecture](../architecture/overview.md)
- Frontend부터 임베딩·검색·답변·상담까지: [Chat and RAG Flow](../architecture/chat-flow.md)
- 저장소와 책임: [Component Map](../architecture/components.md)
- 기술 선택과 근거: [Engineering Decisions](../architecture/decisions/README.md)
- 실험과 검증 결과: [Evidence Register](../proof/evidence-register.md)
- 시나리오별 BE 동작: [UBot-BE Use Cases](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/overview/use-cases.md)
- Backend 상세 기능: [UBot-BE Product Engineering Guide](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/README.md)
- Frontend 화면과 검증: [UBot-FE Documentation](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)
