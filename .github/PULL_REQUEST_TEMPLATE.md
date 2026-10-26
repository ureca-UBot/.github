## Reader Outcome

[독자가 이 변경을 읽고 무엇을 판단하거나 실행할 수 있는가]

## Document Type

- [ ] Product / Use Case / Quickstart
- [ ] Architecture / RFC / ADR
- [ ] API / Reference / Compatibility
- [ ] Migration / Runbook / Reliability
- [ ] Troubleshooting / Incident / Known Issue

## Source of Truth

- Authoritative repository and path: [link]
- Exact commit/artifact revision: [SHA/digest]
- Dynamic runtime authority if relevant: [endpoint/header/status]

## Product Claim

- [ ] No externally visible strong claim
- [ ] Claim updated in `docs/proof/claims.yaml`
- [ ] Applicable version/environment and evidence linked

## Generated Content

- [ ] No generated content change
- [ ] Source repository updated first
- [ ] `generated/MANIFEST.yaml` updated
- [ ] Generated views are current (`python scripts/docs_tool.py generate --check`)

## Reader Validation

- [ ] Links and metadata valid
- [ ] Steps include expected observable result
- [ ] Known limitations and applicability stated
- [ ] No private author instructions exposed

## Ownership and Review

- Product owner: [team]
- Producer/consumer reviewers: [teams]
- Release or SRE reviewer if needed: [team]

## Publication Gate

The final documentation publishing workflow must run:

```bash
python scripts/docs_tool.py validate --mode publish
```
