# System Architecture

조직 아키텍처는 Repository와 런타임 사이의 책임만 설명합니다. API 경로, 설정값, 제한 시간, 재시도와 데이터베이스 제약은 각 Repository 문서에서 확인합니다.

<picture>
  <source media="(max-width: 767px)" srcset="images/system-overview-mobile.svg">
  <img src="images/system-overview.svg" alt="UBot의 사용자 채널, Frontend, Backend, 데이터 계층, AI 런타임, 운영 관측과 연구 저장소 관계" width="100%">
</picture>

[그림 크게 보기](images/system-overview.svg) · [모바일 그림](images/system-overview-mobile.svg)

## Runtime Components

### UBot-FE

**Responsibility**

고객·상담사·관리자가 사용하는 웹 화면과 브라우저 상호작용을 제공합니다.

**Owns**

- 화면, 라우트, 컴포넌트와 클라이언트 상태
- API 계약을 사용하는 요청과 오류 UX
- 반응형 화면, 접근성, 브라우저 회귀 검사

**Does not own**

- 사용자 권한과 업무 상태의 최종 판정
- 데이터베이스 기록과 AI 작업 복구
- 모델·임베딩 품질 보장

**Detailed Documentation**

[UBot-FE](https://github.com/ureca-UBot/UBot-FE) · [Frontend Docs](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)

### UBot-BE API

**Responsibility**

인증과 권한을 확인하고 대화·상담·업무 API를 처리하며 AI 작업을 접수합니다.

**Owns**

- 인증·소유권·업무 규칙
- 대화, 상담 인계와 고객 행동의 서버 상태
- 질문 작업 접수와 결과 조회
- 관리자 기능과 운영 API

**Does not own**

- 장시간 모델 추론의 실행 용량
- 브라우저 화면 상태
- Research 실험의 평가 방법

**Detailed Documentation**

[UBot-BE Architecture](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/architecture/overview.md) · [API Reference](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reference/api.md)

### AI Worker

**Responsibility**

접수된 질문을 가져와 검색·자료 수집·모델 호출·가드 검사를 실행하고 결과를 확정합니다.

**Owns**

- 작업 선점과 실행 상태 갱신
- Retrieval과 업무 자료 조합
- LLM·Embedding 호출과 결과 검사
- 중단 작업의 회수와 완료 기록

**Does not own**

- 외부 사용자 요청을 직접 받는 웹 API
- 사용자 권한이나 가입·예약 상태의 임의 결정
- 모델 서버 자체의 확장 정책

**Detailed Documentation**

[RAG Pipeline](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/rag-pipeline.md) · [Reliability Model](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reliability/reliability-model.md)

### PostgreSQL / pgvector

**Responsibility**

업무·대화·작업·FAQ의 원본과 벡터 검색 데이터를 보관합니다.

**Owns**

- 제품 상태와 작업 완료 기록
- 스키마와 마이그레이션
- FAQ 벡터와 검색 인덱스

**Does not own**

- 작업 전달 신호
- LLM 추론
- 클라이언트 화면 상태

**Detailed Documentation**

[Database Reference](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reference/database.md) · [Embedding and Search](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/faq-embedding.md)

### Redis

**Responsibility**

AI 작업 전달과 선택적 캐시·랭킹·분산 잠금·인증 보조 상태를 제공합니다.

**Owns**

- Worker가 소비하는 작업 Stream
- 짧은 수명의 보조 상태

**Does not own**

- 완료 답변과 업무 데이터의 유일한 원본
- 장애 뒤 작업의 최종 성공 여부

**Detailed Documentation**

[Redis Runtime](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/redis/README.md) · [Worker Recovery](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/worker-reliability.md)

### LLM / Embedding Runtime

**Responsibility**

답변 생성과 벡터 계산을 위한 모델 추론 API를 제공합니다.

**Owns**

- 모델 로딩과 추론 자원
- 요청 단위의 생성·임베딩 결과

**Does not own**

- 사용자 권한과 업무 상태
- FAQ 선택과 제품 정책
- 최종 답변의 저장과 상담 인계

**Detailed Documentation**

[Model Runtime](https://github.com/ureca-UBot/UBot-BE/blob/develop/infra/llm/settings.md) · [LLM Module](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/llm-module.md)

### Observability and Operations

**Responsibility**

애플리케이션·데이터 저장소·모델 런타임의 상태를 분리해 수집하고 운영자가 장애 원인과 대응 절차를 찾게 합니다.

**Owns**

- 상태 확인, 지표 수집과 알림 전달 흐름
- API·Worker·대기열·DB·Redis·모델을 구분하는 운영 신호
- 장애 유형별 런북 연결

**Does not own**

- 업무 데이터와 작업 결과의 원본
- 알림만으로 실행되는 자동 복구
- 측정하지 않은 가용성·복구 시간 보장

**Detailed Documentation**

[Observability](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/operations/observability.md) · [Runbooks](https://github.com/ureca-UBot/UBot-BE/tree/develop/docs/runbooks)

## 주요 흐름

### AI 답변

```text
고객 → UBot-FE → UBot-BE API → 작업 상태 저장
                              → AI Worker → FAQ 검색 / 업무 자료
                                          → LLM / 안전 검사
                              ← 결과 저장
고객 ← UBot-FE ← 작업 결과 조회
```

### 상담사 인계

```text
고객이 상담사 호출
  → UBot-BE가 서버에 저장된 대화로 맥락 구성
  → 배정된 상담사에게 허용된 이력 전달
  → 검사를 통과한 상담 메시지를 같은 대화에 저장
```

### 지식 개선

```text
답하지 못한 질문 → 미응답 저장 → 유사 질문 묶기와 검토
                                → FAQ 보강
                                → 새 벡터 생성과 다음 검색에 반영
```

### 실험 근거를 제품에 반영

Research Repository는 Production 런타임의 직접 의존성이 아닙니다.

```text
실험 / 벤치마크 → 검증 근거 → 기술 결정 → UBot-BE 또는 UBot-FE 구현
```

결정과 원본 근거는 [Engineering Decisions](engineering-decisions.md), Repository별 소유 범위는 [Repository Map](repository-map.md)에서 확인합니다.

### 운영과 복구

```text
API / Worker / DB / Redis / 모델 신호
  → 지표와 상태 수집
  → 알림 묶기와 전달
  → 구성 요소별 런북
  → 저장된 상태로 복구 결과 확인
```

작업 완료 여부는 알림이나 캐시가 아니라 Backend가 저장한 상태를 기준으로 확인합니다. 짧은 장애는 정해진 범위에서 회수·재시도하고, 제한을 넘기면 명시적인 실패로 끝내 운영자가 원인을 추적할 수 있게 합니다.

## 배포와 용량 경계

- 웹 API와 AI Worker는 같은 코드베이스의 서로 다른 실행 역할입니다. 요청 접수 용량과 AI 처리 용량을 따로 조절할 수 있습니다.
- 모델 런타임은 Backend 배포 단위와 분리할 수 있습니다. GPU 자원을 필요할 때 준비하거나 줄이는 운영 선택이 API 교체와 직접 묶이지 않습니다.
- 이 구조는 비용 조절의 여지를 제공하지만 자동 확장, 무중단 전환 또는 비용 절감액 자체를 보장하지는 않습니다.
- 배포 자동화와 인프라 정의는 UBot-BE가 관리하며, 실제 클라우드 자원의 현재 상태는 저장소 파일만으로 단정하지 않습니다.

현재 배포 경로와 검증 범위는 [BE Deploy](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/deploy.md), 서버·모델·관측 구성은 [BE Infra](https://github.com/ureca-UBot/UBot-BE/tree/develop/infra), 선택 배경은 [ADR-005](decisions/ADR-005-async-chat-processing.md)에서 확인합니다.
