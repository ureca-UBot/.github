# [TODO: METHOD PATH]

[TODO: 호출자가 수행할 수 있는 동작을 한 문장으로 설명합니다.]

## 적용 범위와 인증

- Since: [TODO: version]
- Lifecycle: [TODO: Stable/Preview/Deprecated]
- Supported profile: [TODO: profile]
- Authentication and permission: [TODO]

## Request

```http
[TODO: METHOD /path]
```

| Parameter | Type | Required | Default | Unit | Meaning |
|---|---|---|---|---|---|
| [TODO: field] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: 실제 의미] |

Absent/null/empty semantics: [TODO]

Unknown input policy: [REJECT / IGNORE / WARN / PASS_THROUGH]

Update policy: [REPLACE / MERGE / PATCH / PRESERVE_ABSENT / CLEAR_ABSENT]

## Response

```json
{"result": "[TODO: EXAMPLE]"}
```

## Error Surface

| HTTP/gRPC | App Code | Meaning | Retry | Caller action |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 호출 계약

- Timeout: [TODO: value and unit]
- Idempotency/duplicate call: [TODO]
- Retry backoff and stop: [TODO]
- Rate limit authority: [TODO: response header, runtime endpoint, policy]
- Side effects / resource cleanup: [TODO]

## 실행 예제와 결과

```bash
[TODO: request]
```

Expected:

```text
[TODO: observable output]
```

Verification: [TODO: contract test or functional query]

## 잘못된 사용의 예

[TODO: counterexample, why invalid, exact error]

## 변경 및 호환성

- Compatibility dimension: [TODO]
- Deprecated since: [TODO or N/A]
- Replacement/migration: [TODO or N/A]

[공통 오류 설명](../docs/reference/errors.md) · [Product Compatibility](../docs/compatibility/product-matrix.md)
