# 문서 작성 원칙

제품 소개와 기능 흐름은 조직 문서에서 설명하고, API·설정·실행·운영의 상세 내용은 해당 저장소 문서로 연결합니다.

- 첫 화면에서는 전체 기능을 짧게 소개하고, 기능별 문서에서 흐름을 끝까지 설명합니다.
- 코드 변경으로 설명이 달라지면 관련 문서와 링크도 함께 고칩니다.
- 기술 선택과 성능 수치에는 실험 조건·적용 범위·원본 근거를 연결합니다.
- 실행 명령에는 예상 결과나 확인 방법을 적습니다.
- 이미지의 흐름과 문서 링크가 실제 구현에 맞는지 확인합니다.

## 문서 위치와 수정 범위

- 기술 결정의 본문과 색인은 [docs/architecture/decisions/](../architecture/decisions/README.md) 한 곳에서 관리합니다.
- 다른 주제도 [기능별 목차](../README.md)가 연결하는 본문 한 곳을 수정합니다. 소개·색인에는 요약과 링크를 두고 같은 상세 설명을 복사하지 않습니다.
- AWS 구성은 BE의 [Terraform 스택 구분](https://github.com/ureca-UBot/UBot-BE/blob/f782ec7c72cc2af0631570e3b3e0d0a260072a25/infra/terraform/stacks.md)과 해당 스택의 코드·입력값을 기준으로 확인합니다. `gpu-test`의 범위를 `aws-poc` 전체에 적용하지 않습니다.
- 참고 양식은 필요한 문서를 작성할 때 사용합니다. 양식마다 별도 문서를 만들거나 기존 문서를 일괄 재작성할 필요는 없습니다.

## 실험 결과를 인용할 때

데이터셋과 평가 문항 수, 모델·프롬프트, 하드웨어·동시성·측정 시간을 함께 확인합니다. 서로 다른 실험의 최고 수치를 한 구성에서 동시에 달성한 결과처럼 합치지 않습니다.

기존 실험 결과는 당시 조건의 기록으로 보존하고, 현재 설정과 다른 부분은 설명을 덧붙입니다. 원본 결과는 [실험과 검증 근거](../proof/evidence-register.md)에서 찾아볼 수 있습니다.

## 참고 양식

[ADR](../../docs-templates/ADR_TEMPLATE.md) · [Benchmark](../../docs-templates/BENCHMARK_TEMPLATE.md) · [Runbook](../../docs-templates/RUNBOOK_TEMPLATE.md) · [Troubleshooting](../../docs-templates/TROUBLESHOOTING_TEMPLATE.md)
