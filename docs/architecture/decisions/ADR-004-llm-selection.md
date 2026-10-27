# ADR-004: 답변 모델로 Qwen3-4B Instruct 계열 사용

- Status: Accepted
- Date: 2026-10
- Related Repositories: UBot-LLMTest, UBot-BE

## Context

FAQ 근거를 지키면서 한국어 답변을 만들고, 제한된 GPU에서 필요한 처리량과 응답 시간을 맞출 모델 계열이 필요합니다.

## Decision

UBot의 답변 생성 모델 계열로 Qwen3-4B Instruct를 사용합니다. 실행 engine과 양자화별 모델 이름·자원 설정은 UBot-BE가 관리합니다.

## Alternatives Considered

Tesla T4·Ollama·고정 Context 조건에서 모델마다 1,300문항을 평가한 결과입니다([양자화·모델 판단](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/summary/quantization_decision.md)).

| 후보 | 정답 | 정답·근거·상태 모두 충족 | 평균 / p95 | 채택하지 않은 이유 |
|---|---:|---:|---:|---|
| Qwen3-4B-Instruct Q8_0 | 78.8% | 71.9% | 3.49 / 5.98초 | Q4_K_M과 정답률 차이가 유의하지 않은데(p=0.22) 응답이 1.34배 느리고 가중치가 1.7배 큼 |
| Gemma3-4B QAT | 67.0% | 42.0% | 원본 보고서 참조 | 정답률이 크게 낮음 |
| **Qwen3-4B-Instruct Q4_K_M (선택 계열)** | 77.5% | 70.5% | 2.61 / 4.75초 | 품질과 실행 비용의 균형이 가장 좋음 |

## Evidence

[model_test_v5](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/model_test_v5/try1/results/all_summary.md)는 고정 Context와 Ollama 조건에서 Qwen3-4B Instruct 양자화 후보를 비교했습니다. [서빙 실험](https://github.com/ureca-UBot/UBot-LLMTest/blob/cd017ac0fd5a99a9c453d1575950abea176beda3/servingtest/docs/CONCLUSIONS.md)은 별도 GPU와 AWQ runtime을 비교했습니다.

## Trade-offs

- 품질 실험은 검색을 포함하지 않았고 사람 판정 보정도 끝나지 않았습니다.
- Ollama/GGUF 품질과 vLLM/AWQ 처리량은 같은 구성에서 측정한 값이 아닙니다.
- Production의 다른 양자화 구성이 같은 품질을 낸다고 보장하지 않습니다.

## Production Implementation

[UBot-BE LLM Runtime](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/infra/llm/README.md) · [LLM Module](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/docs/how-to/llm-module.md)

## Revisit Triggers

- Production과 같은 runtime·양자화의 품질 gate를 통과하지 못할 때
- 새 모델이 같은 비용 범위에서 품질과 지연을 함께 개선할 때
- 안전성·도구 호출·구조화 출력 계약을 지속해서 지키지 못할 때
