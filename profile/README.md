# UBot

> 통신 상품을 찾는 순간부터 가입·이용 정보 확인, 매장 방문, AI 안내와 사람 상담까지 한곳에서 이어 주는 통신 생활 서비스입니다.

고객은 여러 메뉴를 돌아다니지 않고 상품과 자신의 이용 정보를 확인하고, 가까운 매장을 찾아 방문을 예약하며, 궁금한 점을 대화로 해결할 수 있습니다. UBot이 해결하지 못한 질문은 사람 상담과 FAQ 개선으로 이어집니다.

[UBot 사용하기](https://u-bot.cloud) · [제품과 기능 자세히 보기](../docs/product-overview.md) · [전체 문서](../docs/README.md)

## 질문 하나가 답변·상담·다음 지식으로 이어집니다

UBot의 핵심은 질문에 문장 하나를 돌려주는 데 있지 않습니다. 관리자가 준비한 공식 지식을 검색하고, 필요한 업무 자료를 확인해 답하며, 해결하지 못한 질문과 사람 상담까지 다시 지식 개선으로 연결합니다.

<p align="center">
  <picture>
    <source media="(max-width: 767px)" srcset="../docs/images/chat-flow-mobile.png">
    <img src="../docs/images/chat-flow.png" alt="FAQ 임베딩 준비에서 Frontend 질문, Backend 검색과 업무 자료 조회, 답변 검사, 화면 표시와 상담사 인계로 이어지는 UBot 핵심 흐름" width="80%">
  </picture>
</p>

[채팅과 RAG 전체 흐름 읽기](../docs/chat-flow.md) · [큰 그림](../docs/images/chat-flow.png) · [모바일 그림](../docs/images/chat-flow-mobile.png)

1. **지식을 준비합니다.** 관리자가 FAQ·공식 답변·질문 표현·처리 의도를 관리하면, 현재 FAQ 버전의 질문 표현을 임베딩해 HNSW 검색 인덱스를 준비합니다.
2. **Frontend가 질문을 이어 붙입니다.** 통합 채팅과 플로팅 채팅이 현재 대화에 질문을 추가하고, Backend가 돌려준 작업 상태를 따라 검색·자료 수집·답변 생성 과정을 보여 줍니다.
3. **Backend가 먼저 보호하고 기록합니다.** 회원·비회원 권한, 대화 소유권, 이용 한도, 금지어와 프롬프트 공격을 확인하고 질문·시도·작업을 저장한 뒤 답변 처리를 시작합니다.
4. **질문에 맞는 근거를 찾습니다.** 질문을 필요한 검색 단위로 정리하고 임베딩한 뒤 현재 FAQ 버전과 같은 프로필의 벡터를 검색합니다. FAQ 의도에 따라 회원·상품·매장 자료와 서버가 허용한 조회 도구를 연결합니다.
5. **근거 안에서 답하고 다시 검사합니다.** 공식 FAQ 직접 반환 경로가 활성화되어 있고 승인 조건을 만족하면 등록된 답변을 사용합니다. 그 밖의 질문은 선별한 근거와 조회 자료로 답을 만들고, 서버가 구조·근거·수치와 위험 표현을 확인한 뒤 결과를 저장합니다.
6. **Frontend가 다음 행동을 엽니다.** 답변과 함께 이용 정보·상품·매장·지도 카드를 보여 주고, 평가·의도별 재검색·사람 상담으로 이어 줍니다.
7. **해결되지 않은 질문도 버리지 않습니다.** 근거가 부족한 질문은 미응답으로 수집해 유사 질문끼리 묶습니다. 관리자가 이를 검토해 FAQ를 보강하면 새 지식이 다시 임베딩되어 다음 검색에 쓰입니다.
8. **사람 상담은 같은 대화에서 이어집니다.** 로그인한 고객이 요청하면 서버에 저장된 AI 문답·FAQ 선택·허용된 이전 상담 기록을 상담사에게 넘깁니다. 상담 메시지는 금지어 검사와 의미 검사를 통과한 경우에만 전달합니다.
9. **장애도 같은 흐름 안에서 추적합니다.** PostgreSQL을 작업 상태의 원본으로 두고 Redis는 전달과 조회 캐시에 사용합니다. API·답변 처리·모델 실행을 나눠 필요한 자원만 조절하며, 지표·로그·알림과 장애별 절차로 중단된 작업을 찾고 복구합니다.

## UBot이 바꾸는 고객 경험

| 고객의 상황 | UBot이 제공하는 경험 |
|---|---|
| 어떤 상품이 나에게 맞는지 찾고 싶다 | 요금제·부가서비스·로밍·결합·홈상품을 탐색하고 조건을 비교합니다. |
| 지금 이용 중인 서비스를 확인하고 싶다 | 본인 회선의 가입 상품, 사용량, 청구·납부와 약정 정보를 확인합니다. |
| 매장을 방문해야 한다 | 지역·현재 위치·지도 범위로 매장을 찾고 길찾기와 방문 예약으로 이어갑니다. |
| 공지나 처리 결과를 놓치고 싶지 않다 | 공지·배너·일대일 문의와 예약·납부·가입·사용량 알림을 한곳에서 확인합니다. |
| 메뉴를 찾기 어렵거나 질문이 있다 | 공식 FAQ와 서버가 확인한 자료를 바탕으로 답을 받고 상품·이용 정보·매장 카드로 다음 행동을 선택합니다. |
| AI만으로 해결되지 않는다 | 같은 대화의 문답과 FAQ 선택을 상담사에게 넘겨 설명을 반복하지 않고 상담을 이어갑니다. |

## 고객·상담사·관리자가 같은 흐름을 공유합니다

### 고객

- 회원과 비회원 모두 질문할 수 있으며, 로그인하면 비회원 때의 대화를 회원 계정에서 이어 봅니다.
- 상품 가입·변경·해지, 사용량·청구·약정 조회, 매장 길찾기와 예약을 이용합니다.
- 답변 본문뿐 아니라 실제 조회한 상품·이용 정보·매장과 지도 자료를 함께 확인합니다.
- 답변 뒤에는 의도를 선택해 다시 검색하거나 사람 상담사를 호출할 수 있습니다.

### 상담사

- 고객 화면이 임의로 만든 내용이 아니라 서버에 저장된 AI 문답과 FAQ 선택을 전달받습니다.
- 재배정·재연결 때도 현재 참여 권한을 확인하고 같은 대화에서 상담을 계속합니다.
- 안전 검사를 통과한 메시지만 상대방에게 전달하고 허용된 상담 기록을 대화에 남깁니다.

### 관리자와 운영자

- 상품·매장·FAQ·카테고리·금지어·상담 안전 문장을 관리합니다.
- 미응답을 유사 질문끼리 묶어 검토하고 새 FAQ로 전환합니다.
- 인기·급상승 FAQ와 지역별 문의 흐름을 보고 지식 개선의 우선순위를 정합니다.
- 서비스·데이터 저장소·모델 상태를 구분해 보고 알림과 장애별 절차로 대응합니다.

## 주요 기능

- **상품과 가입** — 요금제·홈상품·부가서비스·로밍·결합상품 카탈로그와 회원 가입 상태를 관리합니다.
- **이용 정보** — 회선별 사용량, 청구·납부와 약정·할부 정보를 본인 범위에서 조회합니다.
- **매장과 방문** — 매장 검색, 지도 범위 조회, 도보·자동차·대중교통 길찾기, 방문 예약과 취소를 제공합니다.
- **고객 지원** — 공지·배너·일대일 문의와 예약·납부·가입·사용량 알림을 연결합니다.
- **FAQ 기반 안내** — 질문 임베딩으로 관련 FAQ를 찾고 필요한 회원·상품·매장 자료를 더해 근거 있는 답변을 만듭니다.
- **사람 상담사 인계** — 저장된 대화 맥락으로 상담을 이어 가고 상담 종료 뒤에도 같은 대화에서 기록을 확인합니다.
- **지식 개선** — 미응답, FAQ 사용 기록, 인기·급상승과 지역별 문의 흐름을 관리자 검토와 FAQ 보강으로 연결합니다.
- **안전 정책 관리** — 입력·생성 답변·상담 메시지를 경로별로 검사하고 정책 후보는 관리자 승인 뒤 반영합니다.

## 신뢰할 수 있는 결과를 만드는 원칙

- **업무 상태는 서버가 결정합니다.** 모델 문장만으로 가입·예약·사용자 정보 변경을 확정하지 않습니다.
- **근거가 없으면 추측하지 않습니다.** 관련 FAQ와 확인된 자료가 부족하면 답변을 보류합니다.
- **상담 인계는 서버 기록을 사용합니다.** 고객이 같은 상황을 처음부터 다시 설명하지 않게 하면서 임의 조작을 막습니다.
- **정책 변경에는 관리자 판단이 들어갑니다.** AI가 제안한 차단 후보를 자동으로 운영 정책에 넣지 않습니다.
- **실패 상태를 남깁니다.** 처리 중단과 외부 의존성 문제를 숨기지 않고 상태·지표·로그로 확인합니다.

## 더 알아보기

| 알고 싶은 내용 | 문서 |
|---|---|
| 제품이 해결하는 문제와 전체 기능 | [Product Overview](../docs/product-overview.md) |
| Frontend부터 임베딩·검색·답변·상담까지 | [Chat and RAG Flow](../docs/chat-flow.md) |
| FE·BE·모델·데이터 저장소의 관계 | [System Architecture](../docs/system-architecture.md) |
| 어떤 Repository가 무엇을 책임지는가 | [Repository Map](../docs/repository-map.md) |
| 주요 기술을 선택한 이유 | [Engineering Decisions](../docs/engineering-decisions.md) |
| 실험 결과와 해석할 수 있는 범위 | [Evidence Register](../docs/evidence-register.md) |

## 참여 멤버

<table>
  <tr>
    <td align="center"><a href="https://github.com/Catverdose"><img src="https://github.com/Catverdose.png?size=96" width="72" alt="Catverdose"><br><sub><b>@Catverdose</b></sub></a></td>
    <td align="center"><a href="https://github.com/gart09"><img src="https://github.com/gart09.png?size=96" width="72" alt="gart09"><br><sub><b>@gart09</b></sub></a></td>
    <td align="center"><a href="https://github.com/H0ng"><img src="https://github.com/H0ng.png?size=96" width="72" alt="H0ng"><br><sub><b>@H0ng</b></sub></a></td>
    <td align="center"><a href="https://github.com/jeaminlim0000"><img src="https://github.com/jeaminlim0000.png?size=96" width="72" alt="jeaminlim0000"><br><sub><b>@jeaminlim0000</b></sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Jo-hyeon-bin"><img src="https://github.com/Jo-hyeon-bin.png?size=96" width="72" alt="Jo-hyeon-bin"><br><sub><b>@Jo-hyeon-bin</b></sub></a></td>
    <td align="center"><a href="https://github.com/kl35805"><img src="https://github.com/kl35805.png?size=96" width="72" alt="kl35805"><br><sub><b>@kl35805</b></sub></a></td>
    <td align="center"><a href="https://github.com/sunji22"><img src="https://github.com/sunji22.png?size=96" width="72" alt="sunji22"><br><sub><b>@sunji22</b></sub></a></td>
    <td align="center"><a href="https://github.com/YuMinha"><img src="https://github.com/YuMinha.png?size=96" width="72" alt="YuMinha"><br><sub><b>@YuMinha</b></sub></a></td>
  </tr>
</table>

## Repositories

### Production

- [UBot-BE](https://github.com/ureca-UBot/UBot-BE) — 회원·상품·매장·FAQ·상담·관리자 업무와 서버 데이터
- [UBot-FE](https://github.com/ureca-UBot/UBot-FE) — 고객·상담사·관리자 웹 애플리케이션

### Research and Benchmark

- [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest) — 생성 모델 품질·프롬프트·GPU 서빙 평가
- [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest) — 임베딩 검색과 서빙 평가
- [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest) — Vector DB와 인덱스 비교

연구 결과는 기술 선택의 근거로 사용하며 서로 다른 실험의 최고 수치를 현재 제품 성능처럼 합치지 않습니다.

## 현재 범위

- UBot은 통신사의 과금·개통 원장을 대체하지 않습니다.
- 실제 통신망 개통과 결제 승인을 수행하는 외부 원장까지 구현한 제품은 아닙니다.
- 모든 질문에 답하는 범용 챗봇이나 모델의 일반 지식을 제공하는 서비스가 아닙니다.
- 다중 리전 재해 복구와 자동 GPU 확장을 완성된 제품 계약으로 선언하지 않습니다.
