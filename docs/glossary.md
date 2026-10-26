# Glossary

UBot 문서에서 Repository를 가로질러 사용하는 용어를 정리합니다. 코드의 enum·field 이름은 해당 Repository 문서를 따릅니다.

| 용어 | 의미 |
|---|---|
| UBot | 통신 정보 질문, 업무 탐색, 사람 상담과 지식 개선을 연결하는 서비스 전체 |
| Conversation | 고객의 AI 문답, FAQ 선택과 허용된 상담 기록이 이어지는 대화 단위 |
| FAQ | 공식 질문·답변과 분류·질문 표현을 포함한 지식 단위 |
| RAG | 검색한 근거와 서버 자료를 생성 모델에 제공해 답변을 만드는 흐름 |
| Retrieval | 질문과 관련된 FAQ 또는 자료 후보를 찾는 단계 |
| Embedding | 문장을 Vector로 바꿔 의미 유사도를 비교하는 표현 |
| Reranker | 첫 검색 후보의 순서를 별도 모델로 다시 평가하는 단계. 현재 Production FAQ 검색에는 사용하지 않음 |
| Vector DB | Embedding을 저장하고 근접 검색하는 계층. UBot Production은 PostgreSQL과 pgvector를 사용 |
| LLM | 답변 생성, 질문 정리 또는 의미 판정에 사용하는 언어 모델 |
| AI Worker | 접수된 질문을 비동기로 가져와 Retrieval·모델 호출·검사·결과 저장을 수행하는 Backend 실행 역할 |
| Job | 질문 접수와 실제 AI 실행을 연결하는 추적 가능한 작업 |
| Evidence | 기술 주장이나 결정의 근거가 되는 dataset·실험 조건·원시 결과·검증 기록 |
| Guard | 입력, 생성 답변 또는 상담 메시지가 정해진 정책을 지키는지 검사하는 계층 |
| Counselor Handoff | 서버에 저장된 대화 맥락을 사람 상담사에게 전달하고 같은 대화에서 상담을 이어가는 흐름 |
| Unanswered | 근거 부족 등으로 AI가 답하지 못해 지식 개선 후보로 남긴 질문 |
| Outbox | 업무 상태 변경과 후속 처리 요청을 같은 트랜잭션에 기록하고 나중에 안전하게 전달하는 방식 |
| At-least-once delivery | 작업이 빠지지 않도록 한 번 이상 전달할 수 있게 하고, 중복은 처리 쪽에서 통제하는 전달 방식 |
| Idempotency | 같은 요청이 다시 와도 동일한 작업으로 식별해 중복 효과를 막는 성질 |
| Fencing | 회수된 이전 실행이 늦게 도착해도 새 실행의 결과를 덮지 못하게 실행 소유권을 검사하는 방식 |
| Observability | 상태 확인·지표·로그·알림을 연결해 시스템 내부 상태와 장애 원인을 판단할 수 있게 하는 성질 |
| Runbook | 운영 장애를 진단·완화·복구하고 성공 여부를 확인하는 절차 |
| Telemap | 지역과 의미가 비슷한 문의의 급증을 탐지해 운영자가 확인하도록 연결하는 기능 |
| Production Repository | 실제 사용자 서비스의 실행 코드와 계약을 관리하는 저장소 |
| Research Repository | 모델·검색 방법을 비교하고 원본 실험 조건과 결과를 관리하는 저장소 |
| Benchmark Repository | 기술 후보를 공통 조건에서 비교해 결정 근거를 제공하는 저장소 |
| 기준 위치 | 특정 사실을 최종적으로 관리하는 곳. 구현 상세는 해당 Production Repository, 실험 원본은 해당 Research·Benchmark Repository가 담당 |
| Lifecycle | Repository의 현재 사용 상태. Active, Research, Maintenance, Reference, Archived 중 하나 |
| ADR | 중요한 기술 결정의 배경·대안·근거·결과를 남기는 Architecture Decision Record |
