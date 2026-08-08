# GACP Codex Execution Adapter

- Status: operational corrective control
- Scope: reusable Codex execution setup for GACP-governed cross-repository work
- Governance boundary: technical capability is not owner authorization

## Purpose

The adapter closes the gap between an authorized GACP handoff and a fresh Codex session that starts
in a different target repository. The prior Git runner controlled staging, commits, pushes, and
receipts after execution began, but it did not make GACP bootstrap discovery or ordinary execution
permissions reusable across repositories.

## Setup

Run these commands from a trusted GACP checkout:

```sh
./bin/gacp-codex-profile inspect
./bin/gacp-codex-profile render
./bin/gacp-codex-profile install
./bin/gacp-codex-profile verify
```

`inspect` is read-only and reports sanitized compatibility characteristics. `render` shows the
exact dedicated profile before installation. `install` writes only
`$CODEX_HOME/gacp.config.toml` with mode `0600`; it does not edit the base `config.toml` and
refuses to overwrite an unmanaged profile. Repeated installation is an idempotent no-op when bytes
already match. `verify` checks exact managed bytes and invokes a supported, non-session runtime help
command with strict configuration enabled.

Start a governed session in the target checkout:

```sh
codex --profile gacp
# or
codex exec --profile gacp "Retrieve and execute the named GACP governed handoff."
```

The profile's machine-local GACP path is private configuration. The active target workspace is
provided by the session, and the configured GACP checkout is the additional workspace root.

## Effective characteristics

- `approval_policy = "on-request"`
- `approvals_reviewer = "auto_review"`
- custom permissions extend the built-in `:workspace` profile
- current target and one configured GACP backend are writable workspace roots
- `.git`, `.agents`, and `.codex` remain protected metadata paths
- configured repository Git metadata remains authoritative; copied or alternate Git directories/work trees are forbidden
- authorized candidate edits and validation remain inside the fresh session; the trusted host controller invokes the GACP runner for Git mutations
- network access is allowlisted to GitHub, its API, and GitHub content hosts
- common environment-secret files are denied
- no `:danger-full-access`, danger-full-access sandbox, blanket network, or approval bypass
- no base-config mutation and no public machine-specific path

Auto-review can approve eligible technical escalations inside the declared boundary. It cannot expand
the governed handoff, approve content, accept an exception, authorize a different remote or branch,
merge a protected branch, or replace owner acceptance.

## Disable and recovery

```sh
./bin/gacp-codex-profile disable
./bin/gacp-codex-profile enable
```

`disable` reversibly renames only a managed profile and is idempotent. `enable` restores it. The
adapter stops on legacy sandbox configuration, permission-name collisions, managed drift, unsupported
Codex versions, or non-GACP files at either managed path.

For controller-managed governed execution, the fresh session produces and validates only the
manifest-authorized candidate files. After it returns, the trusted host controller independently
checks the candidate scope and invokes `bin/gacp run <manifest>` outside the sandbox for exact staging,
commit, normal push, and ref verification. The controller then starts the second fresh session to
verify the published state is idempotent. This split keeps `.git` read-only in every agent session;
raw session-local Git mutation and alternate metadata remain forbidden.

## Operation-specific controls

The reusable profile answers only “can Codex perform ordinary bounded work?” Each operation must still
retrieve an authoritative Git handoff, read `AGENTS.md`, validate repository identity and state, and
obey its exact paths, actions, validation, publication, stop conditions, and next owner gate.

Public manifests should set `destination.local_path` to `runtime-repository-root`. The runner binds
that token to the invocation repository while retaining all other identity checks. Readiness is an
explicit manifest field and defaults to false.

## Current-platform references

This design follows the current Codex profile overlay and configuration model:

- [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Advanced configuration and profiles](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [Permission profiles](https://learn.chatgpt.com/docs/permissions)
- [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review)
- [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)

Permission profiles are a current Codex capability and may evolve. The adapter therefore requires a
minimum supported CLI version, uses strict diagnostics, records its effective characteristics, and
must be retested after material Codex permission-model changes.
