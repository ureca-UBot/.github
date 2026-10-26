---
title: 'Product Quickstart'
type: product-documentation
status: active
owner: 'UBot maintainers'
applicability: development-preview
last_reviewed: '2026-10-26'
---

# Product Quickstart

UBot은 Frontend와 Backend가 함께 동작하는 제품입니다. 아직 고정된 제품 릴리스 묶음은 없으므로 임의의 두 revision을 섞어 `Supported` 조합으로 간주하지 않습니다.

## 1. 구성요소 선택

- Backend API·데이터 저장소·모델 연결: [UBot-BE Quickstart](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/quickstart.md)
- Frontend 화면과 브라우저 실행: [UBot-FE](https://github.com/ureca-UBot/UBot-FE)

각 저장소의 요구 버전과 환경변수는 해당 저장소 문서를 따릅니다. 제품 수준의 알려진 조합은 [Compatibility Matrix](../compatibility/product-matrix.md)에서 확인합니다.

## 2. 성공 확인

구성요소가 켜졌다는 사실뿐 아니라 다음 사용자 결과를 확인합니다.

1. Frontend가 Backend health와 인증 API에 접근한다.
2. 회원 또는 비회원 질문이 접수되고 작업 식별자가 반환된다.
3. 같은 작업을 조회해 최종 답변 또는 명시적인 실패 상태를 확인한다.
4. 로그인·로그아웃 뒤 대화 소유권과 화면 기록이 계약대로 유지된다.

정확한 API와 문제 해결 순서는 [BE Maintainer Guide](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/README.md)를 따릅니다. 검증한 revision과 결과가 없다면 제품 전체 E2E를 완료했다고 기록하지 않습니다.
