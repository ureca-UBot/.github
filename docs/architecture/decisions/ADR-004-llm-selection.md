---
title: 'ADR-004: 답변 모델로 Qwen3-4B Instruct 계열 사용'
type: architecture-decision
status: active
owner: 'UBot maintainers'
applicability: development-preview
last_reviewed: '2026-10-26'
---

# ADR-004: 답변 모델로 Qwen3-4B Instruct 계열 사용

- Status: Accepted
- Date: 2026-10
- Related Repositories: UBot-LLMTest, UBot-BE

## Context

FAQ 근거를 지키면서 한국어 답변을 만들고, 제한된 GPU에서 필요한 처리량과 응답 시간을 맞출 모델 계열이 필요합니다.

## Decision

UBot의 답변 생성 모델 계열로 Qwen3-4B Instruct를 사용합니다. 실행 engine과 양자화별 모델 이름·자원 설정은 UBot-BE가 관리합니다.

## Evidence

[model_test_v5](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/all_summary.md)는 고정 Context와 Ollama 조건에서 Qwen3-4B Instruct 양자화 후보를 비교했습니다. [서빙 실험](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/servingtest/docs/CONCLUSIONS.md)은 별도 GPU와 AWQ runtime을 비교했습니다.

## Trade-offs

- 품질 실험은 검색을 포함하지 않았고 사람 판정 보정도 끝나지 않았습니다.
- Ollama/GGUF 품질과 vLLM/AWQ 처리량은 같은 구성에서 측정한 값이 아닙니다.
- Production의 다른 양자화 구성이 같은 품질을 낸다고 보장하지 않습니다.

## Production Implementation

[UBot-BE LLM Runtime](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/infra/llm/README.md) · [LLM Module](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/how-to/llm-module.md)

## Revisit Triggers

- Production과 같은 runtime·양자화의 품질 gate를 통과하지 못할 때
- 새 모델이 같은 비용 범위에서 품질과 지연을 함께 개선할 때
- 안전성·도구 호출·구조화 출력 계약을 지속해서 지키지 못할 때
