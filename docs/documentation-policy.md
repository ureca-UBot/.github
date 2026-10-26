# Documentation Policy

UBot 조직 문서는 전체 맥락과 연결을 담당하고, 상세 구현은 해당 Repository가 관리합니다.

## 필수 원칙

1. **상세 구현의 기준은 해당 Repository입니다.** API, 설정, 코드, DB, 실행·배포 절차는 그 구현을 가진 저장소에 둡니다.
2. **같은 사실을 여러 곳에 복제하지 않습니다.** 조직 문서는 결론과 맥락을 요약하고 상세 문서로 연결합니다.
3. **코드 변경으로 설명이 틀리면 같은 변경에서 문서를 고칩니다.** 조직 수준의 책임이나 결정이 달라질 때만 이 저장소도 갱신합니다.
4. **성능·정확도·기술 선택에는 원본 Evidence를 연결합니다.** 조건과 한계를 빼고 숫자만 옮기지 않습니다.
5. **실행 명령에는 Expected Result 또는 검증 방법을 함께 적습니다.** 명령만 나열해 성공 여부를 독자에게 맡기지 않습니다.

## 조직 문서에 두는 내용

- 제품의 목적, 사용자와 핵심 흐름
- FE·BE·AI·데이터 계층의 관계
- Repository의 분류와 책임 경계
- 주요 기술 결정과 Evidence·구현 문서의 연결
- 조직 전체 실험·검증 근거의 색인과 해석 범위
- 조직 공통 용어와 문서 양식

## Repository로 보내는 내용

- API 경로와 요청·응답 필드
- 환경변수, 임계값, 제한 시간과 재시도 횟수
- 클래스·서비스·테이블·열·제약
- 세부 배포 명령과 운영 서버 설정
- 원본 데이터셋, 실험 스크립트, 원시 결과와 상세 벤치마크 수치

## 링크 원칙

- Repository 진입 링크는 기본 브랜치를 사용해 최신 문서로 연결합니다.
- ADR의 근거는 커밋 SHA가 들어간 고정 링크를 사용합니다.
- 조직 차원의 실험 요약은 [Evidence Register](evidence-register.md)에 두고 원시 결과를 가진 저장소로 연결합니다.
- Production 구현 링크는 해당 Repository의 현재 문서로 연결합니다.
- 접근할 수 없거나 검증하지 못한 링크는 그 상태를 함께 적습니다.

## 실험 수치 사용

다음 항목을 함께 확인하지 못하면 제품 성능으로 인용하지 않습니다.

- 데이터셋과 평가 분모
- 모델 리비전·양자화·프롬프트
- 하드웨어·실행 환경·동시성·측정 시간
- 홀드아웃과 사람 검토 여부
- 소스 커밋과 수정 중인 작업 트리 여부
- 현재 Production 구성과 다른 점

서로 다른 품질·검색·서빙 실험의 최고 수치를 한 구성에서 동시에 측정한 값처럼 합치지 않습니다.

## 책임과 검토

| 문서 | 작성·갱신 | 필요한 검토 |
|---|---|---|
| 조직 첫 화면·제품·Repository 지도 | 프로젝트 전체 | 제품 흐름과 Repository 책임을 아는 팀원 |
| System Architecture | 관련 FE·BE·AI 담당 | 바뀐 책임을 가진 Repository 담당자 |
| 기술 결정·ADR | 결정을 제안한 담당 | 근거와 Production 구현 담당자 |
| Evidence Register | 실험·검증 담당 | 원본 결과와 Production 구현을 아는 담당자 |
| Repository 문서 | 해당 Repository 담당 | 변경한 코드·운영 계약의 검토자 |
| 표준 양식·용어집 | 조직 문서 관리 | 실제 사용 Repository의 의견 |

## 변경 확인

- [ ] 조직 문서에 구현 상세를 복제하지 않았는가?
- [ ] Responsibility, Owns, Does not own이 서로 충돌하지 않는가?
- [ ] 기술 선택에 커밋 고정 근거가 있는가?
- [ ] Research 결과를 Production 보장값처럼 쓰지 않았는가?
- [ ] 모든 상대 링크와 이미지 경로가 열리는가?
- [ ] 새 명령에 예상 결과 또는 검증 방법이 있는가?

표준 문서는 [ADR](../docs-templates/ADR_TEMPLATE.md), [Benchmark](../docs-templates/BENCHMARK_TEMPLATE.md), [Runbook](../docs-templates/RUNBOOK_TEMPLATE.md), [Troubleshooting](../docs-templates/TROUBLESHOOTING_TEMPLATE.md) 양식을 사용합니다.
