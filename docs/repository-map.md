# Repository Map

> 마지막 확인: 2026-10-26

UBot은 운영 제품 저장소와 기술 검증 저장소를 분리합니다. 제품 동작의 기준은 UBot-BE와 UBot-FE이며, 모델·임베딩·Vector DB 실험은 각 연구 저장소가 결과와 한계를 관리합니다.

## 한눈에 보기

| Repository | Type | Lifecycle | Responsibility | Documentation |
|---|---|---|---|---|
| [UBot-BE](https://github.com/ureca-UBot/UBot-BE) | Production | Active | 백엔드, AI 오케스트레이션, 데이터와 운영 | [README](https://github.com/ureca-UBot/UBot-BE/blob/develop/README.md) · [Docs](https://github.com/ureca-UBot/UBot-BE/tree/develop/docs) |
| [UBot-FE](https://github.com/ureca-UBot/UBot-FE) | Production | Active | 웹 애플리케이션과 브라우저 경험 | [README](https://github.com/ureca-UBot/UBot-FE/blob/develop/README.md) · [Docs](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs) |
| [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest) | Research | Research | LLM 품질, 프롬프트와 서빙 평가 | [Repository](https://github.com/ureca-UBot/UBot-LLMTest) |
| [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest) | Research | Research | 임베딩, 검색과 리랭커 평가 | [Repository](https://github.com/ureca-UBot/UBot-EmbeddingTest) |
| [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest) | Benchmark | Reference | 벡터 데이터베이스와 인덱스 비교 | [Decision](https://github.com/ureca-UBot/UBot-VertorDBTest/blob/main/docs/07-results/decision.md) · [Docs](https://github.com/ureca-UBot/UBot-VertorDBTest/tree/main/docs) |
| [ureca-UBot/.github](https://github.com/ureca-UBot/.github) | Documentation | Active | 조직 진입점과 공통 문서 | [Documentation Portal](README.md) |
| `UBot-FE-Mock` | Prototype | Reference | 초기 UI와 서비스 시나리오 참고 | 2026-10-26 기준 접근 불가 |

Lifecycle은 `Active`, `Research`, `Maintenance`, `Reference`, `Archived`만 사용합니다. `Reference`는 현재 제품을 직접 배포하지 않지만 기술 판단이나 이력을 확인할 때 사용하는 저장소를 뜻합니다.

## UBot-BE

### Responsibility

인증된 API, 업무 규칙, AI 처리 흐름, 데이터 저장과 운영 복구를 담당합니다.

### Owns

- 인증·권한과 사용자 소유권 검사
- 대화·질문 작업·상담 인계의 서버 상태
- FAQ 검색, 업무 자료 조회, LLM·가드 호출의 오케스트레이션
- 업무 API와 관리자 API
- PostgreSQL 스키마와 마이그레이션
- 비동기 Worker, 재시도·복구·관측 계약

### Does not own

- 브라우저 화면과 클라이언트 상태
- 모델·임베딩 후보를 비교하는 실험 방법과 원본 결과
- 저장소 밖 AWS 리소스의 실제 상태

### Detailed Documentation

[UBot-BE README](https://github.com/ureca-UBot/UBot-BE/blob/develop/README.md) · [Technical Documentation](https://github.com/ureca-UBot/UBot-BE/tree/develop/docs)

## UBot-FE

### Responsibility

고객·상담사·관리자가 사용하는 웹 화면과 브라우저 상호작용을 담당합니다.

### Owns

- 화면·라우트·컴포넌트와 클라이언트 상태
- API 계약을 사용하는 클라이언트 코드
- 반응형 화면, 접근성, 브라우저 오류 처리
- 프론트엔드 빌드와 화면 회귀 검사

### Does not own

- 업무 상태의 최종 판정과 권한 결정
- 데이터베이스 스키마와 서버 저장 기록
- 모델·임베딩 정확도
- Backend와 AI 서버의 장애 복구 정책

### Detailed Documentation

[UBot-FE README](https://github.com/ureca-UBot/UBot-FE/blob/develop/README.md) · [Frontend Documentation](https://github.com/ureca-UBot/UBot-FE/tree/develop/docs)

## UBot-LLMTest

### Responsibility

FAQ 근거를 받은 생성 모델의 답변 품질, 프롬프트 변화와 GPU 서빙 특성을 평가합니다.

### Owns

- 모델 품질 평가 데이터와 평가 정의
- 생성 결과, 결정 검사와 LLM Judge 결과
- 프롬프트 비교 실험
- GPU·실행 환경별 서빙 탐색 결과
- 실험 조건, 결과와 알려진 한계

### Does not own

- FAQ와 임베딩 검색 품질
- 운영 Backend의 응답 계약
- 제품에 배포할 모델의 최종 설정
- 실험과 다른 양자화·실행 환경의 품질 보장

### Detailed Documentation

[UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest) · [검증한 snapshot](https://github.com/ureca-UBot/UBot-LLMTest/tree/cd017ac0fd5a99a9c453d1575950abea176beda3)

## UBot-EmbeddingTest

### Responsibility

임베딩 모델, 검색 후보 구성, 리랭커와 군집화 방법을 비교합니다.

### Owns

- 임베딩·검색 평가 데이터와 분모
- 모델·검색 구조·리랭커 비교 결과
- Hit@K·MRR·Fact Recall 등의 평가 정의
- 임베딩 HTTP 처리량 진단
- 실험별 원본 결과와 해석 한계

### Does not own

- 운영 Backend의 SQL과 검색 매개변수
- 제품의 현재 임계값
- 최종 답변 생성 품질
- 실험 결과가 채택된 뒤의 Production 구현

### Detailed Documentation

[UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest) · [검증한 snapshot](https://github.com/ureca-UBot/UBot-EmbeddingTest/tree/ca614933c052fd413968d5735a3a5d31ebe37d92) · [서빙 엔진 비교](https://github.com/ureca-UBot/UBot-EmbeddingTest/blob/ca614933c052fd413968d5735a3a5d31ebe37d92/serving-benchmark/README.md)

## UBot-VertorDBTest

### Responsibility

벡터 저장소와 인덱스 후보를 같은 데이터·자원 조건에서 비교하고 기술 선택 근거를 남깁니다.

### Owns

- Vector DB 벤치마크 설계
- DB별 어댑터와 실행 도구
- Recall·지연·처리량·자원 측정 결과
- 비교 조건과 재현성 한계
- pgvector 선택에 사용한 판단 근거

### Does not own

- UBot-BE의 실제 데이터베이스 스키마
- 운영 검색 매개변수와 임계값
- 실서비스 트래픽의 지연 보장
- FAQ 검색 이후의 LLM 답변 품질

### Detailed Documentation

[Vector DB Decision](https://github.com/ureca-UBot/UBot-VertorDBTest/blob/main/docs/07-results/decision.md) · [검증한 benchmark snapshot](https://github.com/ureca-UBot/UBot-VertorDBTest/tree/9fcbff349648067fc4c96d56d82857f1bcccfdfd)

## ureca-UBot/.github

### Responsibility

UBot 조직의 진입점과 제품·시스템·Repository·기술 결정 사이의 연결을 제공합니다.

### Owns

- 조직 첫 화면
- 제품과 시스템의 전체 맥락
- Repository 분류와 책임 경계
- 기술 결정 색인
- 조직 전체 실험·검증 근거 색인
- 공통 용어와 문서 작성 원칙
- ADR·Benchmark·Runbook·Troubleshooting 양식

### Does not own

- API 경로와 요청·응답 필드
- 환경변수, 임계값, 제한 시간과 재시도 횟수
- 클래스·테이블·데이터베이스 제약
- 원본 실험 데이터와 상세 결과
- 각 Repository의 실행·배포 절차

### Detailed Documentation

[Organization Documentation](README.md)

## UBot-FE-Mock

### Responsibility

조직의 이전 소개에는 사용자 화면과 주요 서비스 시나리오의 초기 프로토타입으로 기록돼 있습니다.

### Owns

현재 저장소 내용을 확인할 수 없어 소유 범위를 확정하지 않습니다.

### Does not own

- 현재 Production 웹 애플리케이션
- Backend 업무 계약
- 현재 기능의 완료 상태와 검증 결과

### Detailed Documentation

2026-10-26 기준 GitHub API와 raw URL이 모두 404를 반환했습니다. 삭제 또는 비공개 전환 여부를 확인한 뒤 링크와 Lifecycle을 갱신합니다.
