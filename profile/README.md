# UBot

통신 서비스 FAQ를 기반으로 AI 상담을 제공하고,
사용자의 위치에 따라 가까운 매장을 안내하는 통신 상담 서비스 프로젝트입니다.

## Service

- [UBot-BE](https://github.com/ureca-UBot/UBot-BE)
  - UBot Backend 서비스

- [UBot-FE](https://github.com/ureca-UBot/UBot-FE)
  - UBot Frontend 서비스

## Prototype

- [UBot-FE-Mock](https://github.com/ureca-UBot/UBot-FE-Mock)
  - 사용자 화면 및 주요 서비스 시나리오 Mock

## Research / Experiment

- [UBot-LLMTest](https://github.com/ureca-UBot/UBot-LLMTest)
  - 로컬 LLM 후보 비교 및 답변 품질 검증

- [UBot-EmbeddingTest](https://github.com/ureca-UBot/UBot-EmbeddingTest)
  - Embedding 모델, Reranker, Clustering 검증

- [UBot-VertorDBTest](https://github.com/ureca-UBot/UBot-VertorDBTest)
  - Vector DB 후보 비교 및 성능 검증

## 멘토링 질문
- 1. 유플러스 챗봇을 직접 사용해보니, 장소 관련 질문을 하면 챗봇에서 직접 해당 장소를 안내해주는게 아니라 매장 찾기 페이지로 연결을 해줍니다. 다른 회사의 챗봇 서비스들도 비슷하게 작동하는데, 혹시 이렇게 구현하는 이유가 있을까요?
- 2. 실제 AI 상담 서비스를 운영할 때, 사용자의 질문이 명확하지 않아 답변을 어떻게 해야하는지 모르는 경우가 많을 것 같습니다. 이런 경우 질문을 하냐 마냐 경계를 정하는 기준이 있을것 같은데, 현업에서는 LLM이 어떻게 기준을 정하게 하는지 궁금합니다.
- 4. 저희가 만든 임베딩 모델의 유사도 threshold를 실험으로 정하고 있는데, 실무에서는 threshold를 어떤 기준으로 정하고, 추후에 변경한다면, 어떤 이유에 근거해서 변경하는지 궁금합니다.
- 5. 임베딩 방법중에, Dense, Sparse, Multi-vector 세개가 있다고 알고 있습니다. 실무에서는 성능 개선을 위해 가벼운 파트에는 Dense만, 복잡한 파트에는 여러 방법을 섞은 hybrid방식을 사용할 것 같은데,  가벼운 파트와 무거운 파트를 어떤 기준으로 구분하는지 궁금합니다.
- 6. 저희는 미답변 로그를 클러스터링해서 신규 FAQ 후보를 발굴하려고 하는데, 실무에서 이런 '콘텐츠 갭 발견' 파이프라인을 실제로 운영해보신 경험이 있으신가요?
- 7. 임베딩 모델을 추가 데이터로 파인튜닝해본 경험이 있으신가요? 사전학습 모델 그대로 쓰는 것과 비교해서 실제로 유의미한 개선이 있었나요?
