# 상품 탐색에서 내 이용 정보까지

[전체 기능](../README.md) · [AI 상담](../architecture/chat-flow.md) · [매장 방문](stores-and-reservations.md)

고객은 상품을 비교한 뒤 가입하고, 자신이 이용 중인 서비스와 청구·사용량을 확인합니다. 상품 화면과 MY 화면, AI 상담이 같은 서버 자료를 활용합니다.

## 고객이 이용하는 흐름

| 고객 행동 | FE가 하는 일 | BE가 하는 일 | 고객이 확인하는 결과 |
|---|---|---|---|
| 상품 찾기 | 상품 종류·검색 조건에 맞는 목록과 상세 표시 | 판매 상품과 조건 조회 | 요금제·홈상품·부가서비스·로밍·결합상품 정보 |
| 채팅 상품 조건 선택 | 단계별로 선택 가능한 조건과 결과 표시 | 조건별 결과 유무와 상품을 직접 조회 | 선택 조건에 맞춘 상품 목록 |
| 신규 회선 번호 확인 | 입력한 번호의 사용 가능 여부 확인 | 로그인 확인 후 기존 번호와 중복 조회 | 가입 요청 전 확인할 번호 상태 |
| 가입·변경 요청 | 로그인·대상 회선·선택 상품을 확인해 요청 | 본인 회선과 가입 상태, 중복·변경 조건 검사 후 저장 | 확정한 가입·변경 상태 또는 거절 사유 |
| 내 이용 정보 보기 | 회선 선택 후 항목별로 자료 요청 | 본인 회선의 약정·가입 상품·사용량·청구 조회 | 선택 회선의 정보와 이력 |
| AI에게 이용 정보 질문 | 질문 전송 후 답변과 이용 정보 카드 표시 | 관련 FAQ와 인증된 사용자 자료를 조회해 답변 생성 | 서버에서 확인한 정보에 대한 설명 |

## 상품과 회선을 함께 관리합니다

상품 목록은 로그인 전에도 탐색할 수 있습니다. 가입·변경·해지에는 로그인과 본인 회선 확인이 필요합니다. 요금제 변경, 부가서비스 가입, 로밍 일정, 결합 구성원, 홈상품 가입은 각각의 업무 조건을 적용합니다.

신규 회선은 가입 전에 전화번호 중복을 확인할 수 있습니다. 사전 조회 결과만으로 가입이 확정되는 것은 아니며, 실제 가입 요청에서도 서버가 번호와 가입 조건을 검사합니다.

MY 화면은 항목별 조회 결과를 나눠 표시합니다. 한 항목을 불러오지 못했다고 다른 정보까지 버리지 않으며, 실패한 항목에서 오류를 확인할 수 있습니다. 서버가 요청을 거절하면 변경이 끝난 것처럼 표시하지 않습니다.

관리자는 상품의 내용과 판매 상태를 관리합니다. 비활성 상품이나 이미 끝난 회선에 대한 요청은 화면의 버튼 표시와 별개로 서버에서도 확인합니다.

## 채팅 상품 목록에서 조건을 좁힙니다

상품 목록 답변에 조건 선택지가 있으면 고객은 조건을 단계별로 고르고 결과를 다시 조회합니다. 서버가 각 선택지에 맞는 상품의 존재 여부를 알려 주어 결과가 없는 선택지는 고를 수 없게 합니다. 이전 조건으로 돌아가 바꾸거나 처음부터 다시 선택할 수 있습니다.

이 조회는 비회원도 사용할 수 있습니다. LLM이나 답변 작업을 새로 실행하지 않고 상품 자료를 직접 반환하며, 조건 선택으로 받은 결과는 대화 기록에 저장하지 않습니다.

## AI 안내와 실제 변경을 구분합니다

AI는 허용된 조회 도구로 본인 이용 정보나 상품 자료를 확인합니다. 회선이 여러 개거나 자료가 부족하면 선택·추가 확인이 필요합니다. 모델이 답변에서 가입이나 변경을 언급하는 것만으로 업무 상태가 바뀌지는 않습니다.

검색된 FAQ가 일반 안내여도 질문에 본인 지칭과 사용량·청구 등의 표현이 함께 있으면 본인 정보 자료 수집을 추가합니다. 이때도 로그인과 회선 소유권 검사를 거칩니다.

가입·해지는 인증한 업무 요청으로 확정합니다. UBot 내부의 가입·청구·사용량 자료를 다루며 실제 통신사의 개통·과금·결제 원장과 연결한 기능은 아닙니다. 휴대폰 소개 화면의 예시 데이터도 실제 상품 가입 API와 구분합니다.

## 상세 구현과 검증

- Backend: [상품·가입·조회 규칙과 테스트](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/features/products-and-subscriptions.md)
- 새 조회 흐름: [상품 조건 직접 조회](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/src/main/java/com/ubot/chat/controller/ChatProductSearchController.java) · [번호 중복 확인](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/src/main/java/com/ubot/subscription/controller/SubscriptionController.java) · [상품 조건 선택 화면](https://github.com/ureca-UBot/UBot-FE/blob/0083c488ed48f4a21d78139f20f03609cc024bdf/src/user/ai/components/ChatProductRefine.tsx)
- Frontend: [상품 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/pages/StorePage.tsx) · [가입·이용 정보 연동](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/subscription/api/subscriptionApi.ts) · [가입·변경 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/subscription/components/SubscriptionActions.tsx)
- 다음 행동: [매장 방문 예약](stores-and-reservations.md) · [상담사 연결](counselor-handoff.md)
