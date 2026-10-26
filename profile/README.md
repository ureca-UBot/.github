# UBot

> 상품 탐색과 가입, 이용 정보 확인, 매장 방문, 고객 지원, AI 상담과 사람 상담을 하나의 서비스로 연결합니다.

UBot은 통신 서비스를 찾고 이용하는 고객, 상담을 이어받는 상담사, 상품과 지식을 관리하는 관리자를 위한 상담 서비스입니다. 고객은 한 화면에서 상품·사용량·청구·약정을 확인하고, 매장을 찾아 예약하며, 공지·문의·알림을 이용할 수 있습니다. 대화가 필요할 때는 공식 FAQ를 바탕으로 답을 받고 같은 맥락에서 사람 상담으로 이어갑니다.

[서비스](https://u-bot.cloud) · [백엔드](https://github.com/ureca-UBot/UBot-BE) · [프론트엔드](https://github.com/ureca-UBot/UBot-FE) · [전체 문서](../docs/README.md)

## 하나로 이어지는 서비스 흐름

1. 회원과 비회원이 통신 상품·이용 정보·매장에 관해 묻거나 필요한 메뉴를 직접 찾습니다.
2. 회원은 자신의 가입 상품, 사용량, 청구·약정 정보를 확인하고 상품 가입과 변경으로 이어갑니다.
3. 주변 매장을 찾고 길을 안내받으며 방문 시간을 예약합니다.
4. 공지와 배너를 확인하고 문의를 남기며 예약·납부·가입·사용량 알림을 받습니다.
5. 대화형 안내는 공식 FAQ와 서버가 확인한 자료를 바탕으로 답하고, 필요하면 같은 대화에서 상담사를 호출합니다.
6. 관리자는 FAQ·상품·매장·안전 정책을 관리하고 미응답과 반복 문의를 다음 개선으로 연결합니다.

<picture>
  <source media="(max-width: 767px)" srcset="../docs/images/system-overview-mobile.svg">
  <img src="../docs/images/system-overview.svg" alt="고객과 운영 채널, UBot Frontend와 Backend, 데이터 계층, AI 런타임, 연구 저장소의 관계" width="100%">
</picture>

[그림 크게 보기](../docs/images/system-overview.svg) · [모바일 그림](../docs/images/system-overview-mobile.svg) · [시스템 구성 자세히 보기](../docs/system-architecture.md)

## 핵심 기능

- **회원·비회원 대화** — 비회원도 질문할 수 있고, 로그인하면 기존 대화를 회원 계정에서 이어 봅니다.
- **상품과 이용 정보** — 요금제·부가서비스·로밍·결합상품을 탐색하고 가입 상품, 사용량, 청구와 약정을 확인합니다.
- **매장 방문 지원** — 지역·현재 위치·지도 범위로 매장을 찾고 도보·자동차·대중교통 길찾기와 방문 예약을 제공합니다.
- **공지·문의·알림** — 공지와 배너, 일대일 문의, 예약·납부·가입·사용량 알림을 한 서비스에서 제공합니다.
- **FAQ 기반 상담** — 공식 FAQ와 서버가 확인한 자료를 바탕으로 답하고 사용한 근거를 기록합니다.
- **사람 상담사 인계** — 서버에 저장된 문답과 FAQ 선택을 전달해 고객이 같은 설명을 반복하지 않게 합니다.
- **지식 개선** — 미응답을 유사 질문끼리 묶고, FAQ 전환·사용 순위·급상승·지역별 문의 흐름으로 관리합니다.
- **관리자 운영** — FAQ·상품·매장·금지어·상담 안전 정책을 관리하고 변경·검토 이력을 확인합니다.

이 기능들은 저장된 업무 상태, 경로별 안전 검사, 지표·로그·알림과 장애별 복구 절차로 뒷받침됩니다.

## Start Here

| 알고 싶은 내용 | 문서 |
|---|---|
| UBot이 누구의 어떤 문제를 해결하는가 | [Product Overview](../docs/product-overview.md) |
| FE·BE·AI·DB가 어떻게 연결되는가 | [System Architecture](../docs/system-architecture.md) |
| 어떤 Repository가 무엇을 책임지는가 | [Repository Map](../docs/repository-map.md) |
| 왜 모델·임베딩·Vector DB와 처리 구조를 선택했는가 | [Engineering Decisions](../docs/engineering-decisions.md) |
| 실험 수치가 무엇을 검증했고 어디까지 해석할 수 있는가 | [Evidence Register](../docs/evidence-register.md) |
| 공통 용어와 문서 작성 규칙 | [Glossary](../docs/glossary.md) · [Documentation Policy](../docs/documentation-policy.md) |

## Repositories

### Production

- [UBot-BE](https://github.com/ureca-UBot/UBot-BE) — 회원·상품·매장·FAQ·상담·관리자 업무와 서버 데이터
- [UBot-FE](https://github.com/ureca-UBot/UBot-FE) — 고객·상담사·관리자 웹 애플리케이션

### Research and Benchmark

- [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest) — LLM 품질·프롬프트·GPU 서빙 평가
- [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest) — 임베딩·검색 구조·리랭커 평가
- [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest) — Vector DB와 인덱스 비교

연구 결과는 기술 선택의 근거입니다. 서로 다른 데이터·모델·런타임의 수치를 합쳐 현재 제품 성능으로 표현하지 않습니다. 실험과 Production 구현의 연결은 [Engineering Decisions](../docs/engineering-decisions.md)에서 확인합니다.

## 현재 범위

- UBot은 통신사의 과금·개통 원장을 대체하지 않습니다.
- 모델이 사용자의 권한이나 가입·예약 상태를 임의로 확정하지 않습니다. 상태 변경과 소유권 판단은 Backend가 담당합니다.
- Research Repository의 최고 수치는 Production 보장값이 아닙니다.
- API, 환경변수, 임계값, 제한 시간, 재시도와 데이터베이스 제약은 해당 Repository 문서를 기준으로 확인합니다.
