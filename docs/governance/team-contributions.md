# 참여 멤버와 구현 기여

이 문서는 프로젝트에 참여한 멤버가 자신이 직접 구현한 내용과 근거를 기록하는 공간입니다. 커밋 수나 활동량으로 기여를 자동 추정하지 않으며, 다른 사람의 기여를 대신 작성하지 않습니다.

[조직 메인](../../profile/README.md)의 접이식 팀원 표에는 담당 영역과 주요 구현·개선을 간단히 적고, 자세한 설명과 근거는 이 문서에 작성합니다.

## 작성 원칙

- 각 참여자는 자신의 항목만 작성하거나 수정합니다.
- 직접 구현한 기능, 설계, 테스트, 문서와 운영 자동화를 구체적으로 적습니다.
- 코드 리뷰, 승인, 단순 병합과 회의 참석만으로는 구현 기여에 포함하지 않습니다.
- 각 항목에는 확인할 수 있는 Pull Request, 커밋 또는 문서 링크를 붙입니다.
- 공동 작업은 자신이 맡은 범위와 함께 작업한 멤버를 구분해 적습니다.
- 커밋 수나 순위로 멤버의 기여를 비교하지 않습니다.

## 작성 양식

아래 양식을 복사해 자신의 항목을 추가합니다.

```md
## [@GitHub-ID](https://github.com/GitHub-ID)

- 담당 영역:
- 직접 구현한 내용:
  -
- 테스트·운영·문서화:
  -
- 근거:
  - PR 또는 커밋 URL:
```

<!-- 이 아래부터 참여자가 자신의 항목을 직접 추가합니다. -->

## [@Catverdose](https://github.com/Catverdose)

- 담당 영역: Backend·Frontend 연동, 상담·비동기 처리, AI 실행 환경, 인프라·운영 및 검증

### 직접 구현·개선한 내용

| 영역 | 구현·개선 내용 | 근거 |
|---|---|---|
| 개발 환경 | Docker Compose·Testcontainers 기반 개발·테스트 환경, PostgreSQL·pgvector·PostGIS 구성, CI와 FE 초기 환경 구축 | [BE #3](https://github.com/ureca-UBot/UBot-BE/pull/3) · [BE #10](https://github.com/ureca-UBot/UBot-BE/pull/10) · [FE #2](https://github.com/ureca-UBot/UBot-FE/pull/2) |
| 비회원 채팅·인증 연동 | 게스트 세션·대화 연결·질문 횟수 제한과 FE 비회원 채팅 지원, 로그인 상태·로그아웃·토큰 재발급 연동 | [BE #113](https://github.com/ureca-UBot/UBot-BE/pull/113) · [BE #131](https://github.com/ureca-UBot/UBot-BE/pull/131) · [FE #28](https://github.com/ureca-UBot/UBot-FE/pull/28) · [FE #15](https://github.com/ureca-UBot/UBot-FE/pull/15) |
| 상품·본인 통신정보 | 요금제·결합·부가서비스·로밍 상품 조회와 관리자 CRUD, 회선 소유권을 확인하는 사용량·청구·약정·가입 정보 조회 API와 MY 화면 연동 | [BE #157](https://github.com/ureca-UBot/UBot-BE/pull/157) · [BE #165](https://github.com/ureca-UBot/UBot-BE/pull/165) · [FE #36](https://github.com/ureca-UBot/UBot-FE/pull/36) · [FE #40](https://github.com/ureca-UBot/UBot-FE/pull/40) |
| 상담사 연결·메시지 보호 | 상담 요청·배정·종료와 상담사 상태 관리, 금지어·임베딩 의미 검사, 허용 메시지 전달과 통합 이력, 고객·상담사·관리자 화면 및 상담 호출 시 현재 대화 자동 인계 | [BE #244](https://github.com/ureca-UBot/UBot-BE/pull/244) · [FE #68](https://github.com/ureca-UBot/UBot-FE/pull/68) · [자동 인계 수정](https://github.com/ureca-UBot/UBot-FE/commit/35193ab) |
| 금지어 관리 | 금지어 CRUD와 채팅 입력 필터링, 관리자 금지어 관리 화면 | [BE #104](https://github.com/ureca-UBot/UBot-BE/pull/104) · [FE #23](https://github.com/ureca-UBot/UBot-FE/pull/23) |
| 비동기 답변·작업 복구 | 질문 접수와 답변 생성을 API·Worker로 분리하고 Redis Streams·DB 작업 상태·실행 소유권·커밋 이후 ACK 구현, FE 상태 조회 연동, 중단 작업 회수·모델 재시도와 Worker 실행·복구 책임 분리 | [BE #214](https://github.com/ureca-UBot/UBot-BE/pull/214) · [FE #52](https://github.com/ureca-UBot/UBot-FE/pull/52) · [BE #281](https://github.com/ureca-UBot/UBot-BE/pull/281) · [BE #289](https://github.com/ureca-UBot/UBot-BE/pull/289) |
| 모델 실행·FAQ 검색 | LLM·Embedding Provider 전환과 OpenAI 호환 Client, Ollama·vLLM 실행 환경 분리, FAQ 질문·답변 임베딩 추가, HNSW 검색 전환과 후보 보충, 리랭커 제거 | [BE #146](https://github.com/ureca-UBot/UBot-BE/pull/146) · [BE #150](https://github.com/ureca-UBot/UBot-BE/pull/150) · [BE #153](https://github.com/ureca-UBot/UBot-BE/pull/153) · [BE #182](https://github.com/ureca-UBot/UBot-BE/pull/182) · [BE #251](https://github.com/ureca-UBot/UBot-BE/pull/251) · [BE #289](https://github.com/ureca-UBot/UBot-BE/pull/289) |
| FE 구조·오류 처리 | 기존 UI를 유지하며 컴포넌트·상태·API 처리 분리, 지연 로딩과 회귀 검사 추가, FAQ 조회 경합·관리자 화면·모니터링 표시 오류 개선 | [FE #64](https://github.com/ureca-UBot/UBot-FE/pull/64) · [FE #76](https://github.com/ureca-UBot/UBot-FE/pull/76) · [FE #77](https://github.com/ureca-UBot/UBot-FE/pull/77) |
| AWS·배포·운영 | FE·BE CI/CD, Terraform 네트워크·EC2·NLB·Spot GPU ASG와 On-Demand GPU 모드 전환, Prometheus 지표·Discord/Slack 장애·복구 알림, 배포 중단 후 Worker를 복구하는 systemd 타이머 | [BE #261](https://github.com/ureca-UBot/UBot-BE/pull/261) · [FE #72](https://github.com/ureca-UBot/UBot-FE/pull/72) · [BE #306](https://github.com/ureca-UBot/UBot-BE/pull/306) · [BE #268](https://github.com/ureca-UBot/UBot-BE/pull/268) · [BE #274](https://github.com/ureca-UBot/UBot-BE/pull/274) · [BE #318](https://github.com/ureca-UBot/UBot-BE/pull/318) |

### 테스트·문서화

- **임베딩 서빙 비교:** Ollama·TEI·vLLM 비교와 Ollama·vLLM 부하 측정 결과를 추가하고, 실험 결과와 BE 적용 내용을 정리했습니다. [서빙 비교 기록](https://github.com/ureca-UBot/UBot-EmbeddingTest/tree/ca61493/serving-benchmark) · [결과·BE 반영 정리](https://github.com/ureca-UBot/UBot-EmbeddingTest/pull/2)
- **서비스 부하·장애 검증:** FE Nginx부터 BE·Worker·모델·DB까지 AWS 질문 3,000건씩 두 번 전송한 결과, Worker·Redis·PostgreSQL·vLLM 장애 복구 시험, Discord 알림과 통신지도·미응답 관리 화면 검증 도구·결과·캡처를 정리했습니다. [ServerTest 기록](https://github.com/ureca-UBot/UBot-ServerTest/tree/07217660fa2aafcd671600905c62e3a2a8f0226a)
- **구현·운영 문서:** BE 실행·배포·설정·장애 대응 문서와 조직의 제품·기능·아키텍처·검증 문서를 정리하고, 코드 변경에 맞춰 설명·그림·링크를 갱신했습니다. [BE 문서·Terraform 정리](https://github.com/ureca-UBot/UBot-BE/pull/306) · [조직 문서 갱신](https://github.com/ureca-UBot/.github/commit/d10c22c2f25a005f5eedecb8deca392593e6e09c)
