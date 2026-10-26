---
title: "UBot Cross-repo Contracts"
type: contract-index
status: preview
owner: "UBot maintainers"
last_reviewed: 2026-10-26
---

# Cross-repo Contracts

이 문서는 구성요소 사이에서 함께 지켜야 하는 계약의 위치와 판정 기준을 정리합니다. 필드·상태·환경변수의 상세 정의는 코드를 생산하는 저장소가 기준입니다.

## Contract Matrix

| Producer | Consumer | Contract | Runtime authority | Source of truth | Joint owner |
|---|---|---|---|---|---|
| UBot-BE | UBot-FE | HTTP 요청·응답, 인증 오류, 비동기 작업 상태 | 실제 HTTP 응답과 작업 조회 결과 | [BE API Reference](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reference/api.md) | BE + FE |
| UBot-FE | UBot-BE | 로그인·비회원 세션, 대화 식별자와 사용자 동작 | Backend가 검증한 사용자·대화 소유권 | [Frontend Integration](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/frontend-integration.md) | FE + BE |
| UBot-BE API | UBot-BE Worker | 작업 식별자, 상태 전이, 전달·중복·재시도 의미 | PostgreSQL 작업·시도 상태 | [Reliability Model](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reliability/reliability-model.md) | BE |
| UBot-BE | Model runtime | 채팅·임베딩 요청, 구조화 출력과 실패 의미 | 모델 HTTP 응답과 Backend 검증 결과 | [LLM Module](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/how-to/llm-module.md) | BE |
| UBot-BE | PostgreSQL | 영속 상태, 마이그레이션과 데이터 제약 | 적용된 Flyway schema와 DB 상태 | [Database Reference](https://github.com/ureca-UBot/UBot-BE/blob/develop/docs/reference/database.md) | BE |

## Required Contract Properties

교차 저장소 계약을 변경할 때는 다음을 함께 확인합니다.

- producer와 consumer, 기준 스키마 또는 문서
- 알 수 없는 입력과 누락 필드의 처리
- timeout, retry, stop condition
- ordering, duplicate, idempotency 의미
- 배포 순서와 rollback 제약
- producer·consumer가 함께 실행하는 검증 또는 재현 절차

컴파일이나 한쪽 저장소 테스트 통과만으로 제품 호환성을 확정하지 않습니다. 제품 수준 상태는 [Compatibility Matrix](../compatibility/product-matrix.md)에 기록합니다.
