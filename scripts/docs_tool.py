#!/usr/bin/env python3
"""Documentation scaffolding validator and canonical-view generator.

This script validates local contracts and provenance. It does NOT execute product
E2E, contact remote GitHub APIs, or prove that a stated benchmark is true.
Evidence references still require independent CI/test jobs.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("PyYAML is required: python -m pip install -r requirements-docs.txt", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
KEY = re.compile(r"^[a-z][a-z0-9_-]*$")
TODO = re.compile(r"\[TODO(?::[^\]]+)?\]|\bTEMPLATE_(?:[A-Z0-9_]+)\b|https://github\.com/ORG/|@ORG/", re.I)
MD_LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s\)]+)(?:\s+[^)]*)?\)")
VALID_MODELS = {"unified", "coordinated", "independent"}
VALID_EVAL = {"NOT_EVALUATED", "PASS", "FAIL", "ERROR", "NOT_APPLICABLE"}
VALID_LIFECYCLE = {"draft", "experimental", "preview", "stable", "maintenance", "deprecated", "eol"}
VALID_CLAIM = {"DRAFT", "VERIFIED", "RETIRED"}
VALID_PROPAGATION = {"NOT_EVALUATED", "PLANNED", "RELEASED", "PROPAGATING", "OBSERVED", "VERIFIED", "ERROR"}
VALID_ELIGIBILITY = {"NOT_EVALUATED", "SUPPORTED", "CONDITIONAL", "NOT_RECOMMENDED"}


def load_yaml(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            value = yaml.safe_load(f)
        if not isinstance(value, dict):
            raise ValueError("expected YAML mapping")
        return value
    except (OSError, yaml.YAMLError, ValueError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: {exc}") from exc


def fail_if_unexpected(mapping, wanted, label, errors):
    if not isinstance(mapping, dict):
        errors.append(f"{label}: expected mapping")
    else:
        for field in wanted:
            if field not in mapping:
                errors.append(f"{label}: missing required field '{field}'")


def is_real(value):
    return isinstance(value, str) and bool(value.strip()) and not bool(TODO.search(value))


def asdict(value):
    return value if isinstance(value, dict) else {}


def validate_model(product, releases, claims, manifest, mode="template"):
    errors = []
    fail_if_unexpected(product, ["schema_version", "product", "repositories", "components", "artifacts"], "data/product.yaml", errors)
    meta = asdict(product.get("product"))
    fail_if_unexpected(meta, ["id", "name", "owner", "audience", "release_model", "publication_status"], "product", errors)
    model = meta.get("release_model")
    if model not in VALID_MODELS:
        errors.append(f"product.release_model must be one of {sorted(VALID_MODELS)}")
    if meta.get("publication_status") not in {"template", "ready"}:
        errors.append("product.publication_status must be 'template' or 'ready'")
    if mode == "publish" and meta.get("publication_status") != "ready":
        errors.append("Publish blocked: publication_status must be 'ready'")
    repos = asdict(product.get("repositories"))
    comps = asdict(product.get("components"))
    arts = asdict(product.get("artifacts"))
    for label, coll in [("repository", repos), ("component", comps), ("artifact", arts)]:
        for key in coll:
            if not KEY.fullmatch(str(key)):
                errors.append(f"{label} id '{key}' must be lowercase kebab/snake case")
    for cid, entry in comps.items():
        entry = asdict(entry)
        if not entry.get("repositories") or not isinstance(entry.get("repositories"), list):
            errors.append(f"component '{cid}' must list one or more repositories")
        for repo in entry.get("repositories", []):
            if repo not in repos:
                errors.append(f"component '{cid}' references unknown repository '{repo}'")
        if mode == "publish":
            if not is_real(entry.get("responsibility")):
                errors.append(f"component '{cid}' missing concrete responsibility")
    for aid, entry in arts.items():
        entry = asdict(entry)
        comp = entry.get("component")
        repo = entry.get("repository")
        if comp not in comps:
            errors.append(f"artifact '{aid}' references unknown component '{comp}'")
        if repo not in repos:
            errors.append(f"artifact '{aid}' references unknown repository '{repo}'")
        elif comp in comps and repo not in asdict(comps[comp]).get("repositories", []):
            errors.append(f"artifact '{aid}' repository '{repo}' is not associated with component '{comp}'")
    for rid, entry in repos.items():
        entry = asdict(entry)
        if mode == "publish" and (not is_real(entry.get("url")) or not is_real(entry.get("owner"))):
            errors.append(f"repository '{rid}' has unresolved URL/owner")

    fail_if_unexpected(releases, ["schema_version", "recommended_profile", "profiles"], "releases", errors)
    profiles = asdict(releases.get("profiles"))
    if not profiles:
        errors.append("releases must define at least one profile")
    recommended = releases.get("recommended_profile")
    if recommended is not None and recommended not in profiles:
        errors.append(f"recommended_profile references unknown profile '{recommended}'")
    if mode == "publish" and model in {"unified", "coordinated"} and not recommended:
        errors.append("Publish blocked: recommended_profile required for unified/coordinated releases")

    for pid, entry in profiles.items():
        entry = asdict(entry)
        lifecycle = entry.get("lifecycle")
        eligible = entry.get("production_eligibility")
        if lifecycle not in VALID_LIFECYCLE:
            errors.append(f"profile '{pid}' invalid lifecycle '{lifecycle}'")
        if eligible not in VALID_ELIGIBILITY:
            errors.append(f"profile '{pid}' invalid production_eligibility '{eligible}'")
        versions = asdict(entry.get("artifact_versions"))
        if model in {"unified", "coordinated"}:
            missing = set(arts) - set(versions)
            if missing:
                errors.append(f"profile '{pid}' missing artifacts {sorted(missing)}")
        for aid, v in versions.items():
            if aid not in arts:
                errors.append(f"profile '{pid}' references unknown artifact '{aid}'")
            if not isinstance(v, dict) or not isinstance(v.get("version"), str):
                errors.append(f"profile '{pid}' artifact '{aid}' requires string version")
        verification = asdict(entry.get("verification"))
        for check in ["contract_tests", "product_e2e", "upgrade"]:
            record = asdict(verification.get(check))
            status = record.get("status")
            if status not in VALID_EVAL:
                errors.append(f"profile '{pid}' verification '{check}' has invalid status '{status}'")
            if status == "PASS" and not (is_real(record.get("evidence")) and is_real(record.get("verified_at"))):
                errors.append(f"profile '{pid}' verification '{check}': PASS requires evidence and verified_at")
        prop = asdict(entry.get("propagation"))
        state = prop.get("status")
        if state not in VALID_PROPAGATION:
            errors.append(f"profile '{pid}' propagation has invalid status '{state}'")
        if state == "VERIFIED":
            if not all(is_real(prop.get(k)) for k in ["desired_revision", "observed_revision", "evidence", "verified_at", "environment"]):
                errors.append(f"profile '{pid}' propagation VERIFIED requires desired/observed revision, environment and evidence/date")
            if prop.get("desired_revision") != prop.get("observed_revision"):
                errors.append(f"profile '{pid}' propagation cannot be VERIFIED with divergent desired/observed revisions")
        if eligible in {"SUPPORTED", "CONDITIONAL"}:
            if eligible == "CONDITIONAL" and not entry.get("support_conditions"):
                errors.append(f"profile '{pid}' CONDITIONAL eligibility requires support_conditions")
            for check in ["contract_tests", "product_e2e"]:
                if asdict(verification.get(check)).get("status") != "PASS":
                    errors.append(f"profile '{pid}' cannot be SUPPORTED without PASS {check}")
            if state != "VERIFIED":
                errors.append(f"profile '{pid}' cannot be SUPPORTED until propagation is VERIFIED")
        if mode == "publish" and pid == recommended:
            if eligible not in {"SUPPORTED", "CONDITIONAL"}:
                errors.append(f"recommended profile '{pid}' needs verified production eligibility")
            if model in {"unified", "coordinated"} and not is_real(entry.get("product_release")):
                errors.append(f"recommended profile '{pid}' missing product_release")
            for aid, v in versions.items():
                required_identity = ["version", "commit"]
                if asdict(arts.get(aid)).get("type") in {"service", "container", "image"}:
                    required_identity.append("digest")
                for field in required_identity:
                    if not is_real(asdict(v).get(field)):
                        errors.append(f"recommended profile '{pid}' artifact '{aid}' missing {field}")
                commit = asdict(v).get("commit")
                if is_real(commit) and not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
                    errors.append(f"recommended profile '{pid}' artifact '{aid}' commit needs 40-character SHA")
                digest = asdict(v).get("digest")
                if is_real(digest) and not re.fullmatch(r"sha256:[0-9a-f]{64}", str(digest)):
                    errors.append(f"recommended profile '{pid}' artifact '{aid}' digest needs sha256:<64 hex>")

    fail_if_unexpected(claims, ["schema_version", "claims"], "claims", errors)
    listed = claims.get("claims", [])
    if not isinstance(listed, list):
        errors.append("claims must be a list")
        listed = []
    seen_claims = set()
    for item in listed:
        item = asdict(item)
        cid = item.get("id")
        if not cid or cid in seen_claims:
            errors.append(f"duplicate/missing claim id '{cid}'")
        seen_claims.add(cid)
        status = item.get("status")
        if status not in VALID_CLAIM:
            errors.append(f"claim '{cid}' has invalid status '{status}'")
        evidence = asdict(item.get("evidence"))
        doc = evidence.get("document")
        if doc:
            target = ROOT / str(doc)
            if not target.is_file():
                errors.append(f"claim '{cid}' evidence document missing: {doc}")
        for source in item.get("appears_in", []) or []:
            if not (ROOT / str(source)).is_file():
                errors.append(f"claim '{cid}' appears_in missing: {source}")
        profile = asdict(item.get("applicability")).get("product_profile")
        if profile not in profiles:
            errors.append(f"claim '{cid}' references unknown product profile '{profile}'")
        if status == "VERIFIED":
            if not is_real(item.get("last_verified")):
                errors.append(f"claim '{cid}' VERIFIED but last_verified is absent")
            if not is_real(item.get("owner")):
                errors.append(f"claim '{cid}' VERIFIED but owner is absent")
            if not any(is_real(evidence.get(k)) for k in ["reproduction_command", "raw_artifact", "reference_oracle"]):
                errors.append(f"claim '{cid}' VERIFIED but no reproducible artifact/oracle")
        if mode == "publish" and status == "DRAFT":
            # Drafts may exist but must not be used to make public claims.
            if item.get("appears_in"):
                errors.append(f"Publish blocked: claim '{cid}' appears in public docs but remains DRAFT")

    fail_if_unexpected(manifest, ["schema_version", "artifacts"], "generated/MANIFEST.yaml", errors)
    for art in manifest.get("artifacts", []) or []:
        art = asdict(art)
        if art.get("status") != "GENERATED":
            errors.append("generated manifest must list only GENERATED artifacts")
            continue
        source = asdict(art.get("source"))
        generator = asdict(art.get("generator"))
        if source.get("repository_id") not in repos:
            errors.append("generated artifact references unknown source repository")
        if not re.fullmatch(r"[0-9a-f]{40}", str(source.get("commit", ""))):
            errors.append("generated artifact source.commit must be 40-character git SHA")
        for k in ["destination", "generated_at", "consumed_by_profile"]:
            if not is_real(art.get(k)):
                errors.append(f"generated artifact missing {k}")
        for k in ["path"]:
            if not is_real(source.get(k)):
                errors.append(f"generated artifact source missing {k}")
        for k in ["name", "version", "command"]:
            if not is_real(generator.get(k)):
                errors.append(f"generated artifact generator missing {k}")
        if art.get("consumed_by_profile") not in profiles:
            errors.append("generated artifact references unknown product profile")
        dest = art.get("destination")
        if isinstance(dest, str) and not (ROOT / dest).exists():
            errors.append(f"generated artifact destination missing: {dest}")
    return errors


def frontmatter(content, path, errors):
    if not content.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{path}: unterminated frontmatter")
        return {}, content
    try:
        data = yaml.safe_load(content[4:end])
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid frontmatter YAML: {exc}")
        return {}, content[end+5:]
    if not isinstance(data, dict):
        errors.append(f"{path}: frontmatter must be mapping")
        data = {}
    for field in ["title", "type", "status", "owner"]:
        if field not in data:
            errors.append(f"{path}: frontmatter missing {field}")
    return data, content[end+5:]


def markdown_link_errors(mode):
    errors = []
    candidates = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
    for path in candidates:
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        content = path.read_text(encoding="utf-8")
        if path.name != "README.md":
            metadata, _ = frontmatter(content, rel, errors)
            if mode == "publish" and metadata.get("status") not in {"published", "active", "stable"}:
                errors.append(f"{rel}: publication blocked until frontmatter status is published/active/stable")
        if mode == "publish" and TODO.search(content):
            errors.append(f"{rel}: publish blocked by unresolved placeholder or ORG owner")
        # Remove fenced code, comments, and frontmatter before parsing prose links.
        prose = re.sub(r"(?s)^---\n.*?\n---\n", "", content)
        prose = re.sub(r"(?ms)^```.*?^```\s*$", "", prose)
        prose = re.sub(r"(?s)<!--.*?-->", "", prose)
        for matched in MD_LINK.finditer(prose):
            url = matched.group(1)
            if re.match(r"(?i)^(https?://|mailto:|tel:|#)", url):
                continue
            local = unquote(url.partition("#")[0])
            if not local:
                continue
            target = (path.parent / local).resolve()
            if not target.is_relative_to(ROOT.resolve()):
                errors.append(f"{rel}: local link escapes product-docs: {url}")
            elif target.is_dir():
                if not any((target / index).is_file() for index in ["README.md", "index.md"]):
                    errors.append(f"{rel}: directory link has no index: {url}")
            elif not target.is_file():
                errors.append(f"{rel}: broken local link: {url}")
    return errors


def canonical_views(product, releases, claims):
    meta = asdict(product.get("product"))
    repos, components, artifacts = (asdict(product.get(n)) for n in ["repositories", "components", "artifacts"])
    t = ["<!-- GENERATED: scripts/docs_tool.py. DO NOT EDIT. -->", "", "# Product Components", "",
         "| Component ID | Responsibility | Repository sources | Owner(s) |", "|---|---|---|---|"]
    for cid, item in sorted(components.items()):
        item = asdict(item)
        linked = []
        owners = []
        for rid in item.get("repositories", []):
            info = asdict(repos.get(rid))
            linked.append(f"[{rid}]({info.get('url', '#')})")
            owners.append(str(info.get("owner", "Unknown")))
        t.append(f"| `{cid}` | {str(item.get('responsibility', 'TBD')).replace('|','/')} | {', '.join(linked)} | {', '.join(sorted(set(owners)))} |")
    t += ["", "## Artifacts", "", "| Artifact ID | Component | Origin repository | Type |", "|---|---|---|---|"]
    for aid, art in sorted(artifacts.items()):
        art = asdict(art)
        t.append(f"| `{aid}` | `{art.get('component','?')}` | `{art.get('repository','?')}` | {art.get('type','?')} |")
    t += ["", "Source: [`data/product.yaml`](../data/product.yaml).", ""]
    component_md = "\n".join(t)
    t = ["<!-- GENERATED: scripts/docs_tool.py. DO NOT EDIT. -->", "", "# Product Release Profiles", "",
         f"Release model: `{meta.get('release_model', '?')}`", "",
         f"Recommended profile: `{releases.get('recommended_profile') or 'not selected'}`", "",
         "| Profile | Product release | Lifecycle | Eligibility | Contract | E2E | Propagation |",
         "|---|---|---|---|---|---|---|"]
    for pid, prof in sorted(asdict(releases.get("profiles")).items()):
        prof = asdict(prof)
        checks = asdict(prof.get("verification"))
        def st(n):return asdict(checks.get(n)).get("status", "NOT_EVALUATED")
        t.append(f"| `{pid}` | `{prof.get('product_release') or 'none'}` | {prof.get('lifecycle','draft')} | {prof.get('production_eligibility','NOT_EVALUATED')} | {st('contract_tests')} | {st('product_e2e')} | {asdict(prof.get('propagation')).get('status','NOT_EVALUATED')} |")
    t += ["", "## Artifact versions by profile", "", "| Profile | Artifact | Version | Commit |", "|---|---|---|---|"]
    for pid, prof in sorted(asdict(releases.get("profiles")).items()):
        for aid, info in sorted(asdict(asdict(prof).get("artifact_versions")).items()):
            info = asdict(info)
            t.append(f"| `{pid}` | `{aid}` | `{info.get('version','?')}` | `{info.get('commit') or 'NOT_EVALUATED'}` |")
    t += ["", "Source: [`docs/releases/product-versions.yaml`](../docs/releases/product-versions.yaml).", ""]
    release_md = "\n".join(t)
    t = ["<!-- GENERATED: scripts/docs_tool.py. DO NOT EDIT. -->", "", "# Product Claims", "",
         "| ID | Claim | Status | Evidence document |", "|---|---|---|---|"]
    for claim in claims.get("claims", []):
        claim = asdict(claim)
        evidence = asdict(claim.get("evidence"))
        doc = evidence.get("document")
        display = f"[{doc}](../{doc})" if doc else "Not provided"
        t.append(f"| `{claim.get('id','?')}` | {str(claim.get('statement','?')).replace('|','/')} | {claim.get('status','?')} | {display} |")
    t += ["", "**DRAFT is not a verified product claim.**", "", "Source: [`docs/proof/claims.yaml`](../docs/proof/claims.yaml).", ""]
    return {
        ROOT / "generated/components.md": component_md,
        ROOT / "generated/release-summary.md": release_md,
        ROOT / "generated/claim-summary.md": "\n".join(t),
    }


def perform_generation(views, check):
    errors = []
    for file, output in views.items():
        expected = output.rstrip() + "\n"
        if check:
            if not file.exists() or file.read_text(encoding="utf-8") != expected:
                errors.append(f"{file.relative_to(ROOT)}: generated view is stale; run python scripts/docs_tool.py generate")
        else:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(expected, encoding="utf-8")
    return errors


def run(args):
    try:
        product = load_yaml(ROOT / "data/product.yaml")
        releases = load_yaml(ROOT / "docs/releases/product-versions.yaml")
        claims = load_yaml(ROOT / "docs/proof/claims.yaml")
        manifest = load_yaml(ROOT / "generated/MANIFEST.yaml")
    except ValueError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    errors = validate_model(product, releases, claims, manifest, mode=args.mode if args.command == "validate" else "template")
    if args.command == "validate":
        errors += markdown_link_errors(args.mode)
        errors += perform_generation(canonical_views(product, releases, claims), True)
        if args.mode == "publish":
            if TODO.search((ROOT / "data/product.yaml").read_text(encoding="utf-8")):
                errors.append("data/product.yaml: unresolved product placeholders")
            if TODO.search((ROOT / "docs/releases/product-versions.yaml").read_text(encoding="utf-8")):
                errors.append("docs/releases/product-versions.yaml: unresolved release placeholders")
            if TODO.search((ROOT / "docs/proof/claims.yaml").read_text(encoding="utf-8")):
                errors.append("docs/proof/claims.yaml: unresolved claim placeholders")
            if TODO.search((ROOT / "generated/MANIFEST.yaml").read_text(encoding="utf-8")):
                errors.append("generated/MANIFEST.yaml: unresolved provenance placeholders")
            codeowners = (ROOT / ".github/CODEOWNERS").read_text(encoding="utf-8")
            if not any(line.strip() and not line.lstrip().startswith("#") for line in codeowners.splitlines()):
                errors.append(".github/CODEOWNERS: publication requires at least one active ownership rule")
            if TODO.search(codeowners):
                errors.append(".github/CODEOWNERS: example owners must be replaced")
    else:
        if not errors:
            errors += perform_generation(canonical_views(product, releases, claims), args.check)
    if errors:
        for message in sorted(set(errors)):
            print("ERROR", message, file=sys.stderr)
        print(f"FAILED: {len(set(errors))} validation issue(s).", file=sys.stderr)
        return 1
    print(f"PASS: {args.command} (mode={getattr(args, 'mode', 'template')})")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    g = sub.add_parser("generate", help="Regenerate canonical tables/views")
    g.add_argument("--check", action="store_true", help="Fail when generated files are stale")
    v = sub.add_parser("validate", help="Validate references, contract metadata and publication gates")
    v.add_argument("--mode", choices=["template", "publish"], default="template")
    args = parser.parse_args()
    sys.exit(run(args))


if __name__ == "__main__":
    main()
