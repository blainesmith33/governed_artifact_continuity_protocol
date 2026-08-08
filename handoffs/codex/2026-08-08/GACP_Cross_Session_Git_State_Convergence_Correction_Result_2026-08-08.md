# GACP Cross-Session Git-State Convergence Correction Result

- Date: 2026-08-08
- Governing authorization commit: `6e26ae4d203aac7230d0901d00cff9c76cf25790`
- Branch: `gacp/codex-execution-automation-corrective-20260807`
- Deterministic validation: **21/21 PASS**
- Fresh-session acceptance: **PASS**
- Routine manual human approval prompts: **0**
- Ready for real migration: **Yes, pending owner substantive acceptance**
- Merge authorization: **Not granted**

## Outcome

The bounded convergence correction is complete. The original failure was reproduced, its cause was
established from session command evidence, the minimum safe execution boundary was corrected, and a
clean disposable two-session acceptance scenario passed every required property.

The fresh Codex session now performs only authorized candidate editing and validation inside the
sandbox. The trusted acceptance controller independently validates that candidate and invokes the
existing manifest-validated `bin/gacp` runner outside the sandbox for exact staging, commit, normal
push, and ref verification. A second fresh session validates the published result without editing.

## Established root cause

The failed 2026-08-07 acceptance was not a Git push failure. Fresh sessions could not write the real
protected `.git` directories, so they created temporary copied Git metadata and used
`--git-dir`/`--work-tree` commands. Commits and pushes from those temporary directories reached the
disposable remotes, and worktree file edits persisted, but the temporary local refs disappeared when
the sessions ended. The actual disposable repositories therefore remained at their base commits.

Additional reproduction proved that Auto-review cannot make a path declared read-only by the active
permission profile writable. Prohibiting alternate metadata correctly caused a fail-closed stop at
`.git/index.lock`; an exact command rule also did not deterministically force a normally launched
runner outside the sandbox. The failure was therefore an interaction between the protected metadata
boundary, fresh-session execution, and the original acceptance harness assumption that session-local
Git mutations would persist.

## Corrective changes

1. The Codex profile keeps `.git` read-only and explicitly forbids copied, relocated, or alternate
   Git metadata.
2. The profile protects the exact GACP runner file and defines the controller-managed split boundary:
   candidate edit/validation in the fresh session; governed Git mutation in the trusted controller.
3. The acceptance harness generates manifest-bound disposable target and GACP operations.
4. The harness rejects alternate Git metadata commands and any unexpected session-local Git mutation.
5. The controller validates the unstaged target candidate, runs `bin/gacp` for target publication,
   generates the exact governed result, and runs `bin/gacp` for backend publication.
6. Acceptance evidence now records controller outcomes, final local/remote identities, clean states,
   idempotence, alternate-metadata use, profile cleanup, and prompt count.
7. Adapter documentation and deterministic tests describe and enforce the corrected boundary.

No `.git` protection, sandbox, AppArmor restriction, network boundary, or approval policy was
weakened. No real project was used or modified.

## Validation

The deterministic GACP, Git-action, and profile suite passed **21/21**. `git diff --check` passed.

The clean full acceptance scenario then passed with:

- two fresh noninteractive Codex sessions;
- session stdin set to `DEVNULL`;
- zero routine manual human approval prompts;
- no alternate Git metadata in either session;
- no writable Git metadata in either session;
- two successful manifest-validated controller runner operations;
- target local and remote commit identity at
  `3e8547e1d07383c921a2b1f63462ea7adb4450fb`;
- GACP disposable local and remote commit identity at
  `2ee1a417d1a303770d1f7eaeced1d536526f7b88`;
- clean final target and GACP worktrees;
- valid governed `result.json` identity;
- a second fresh session that made no changes and proved idempotence.

Machine evidence is recorded at
`evidence/2026-08-08/git-state-convergence-correction.json`.

## Assessment and recommendation

All nine required acceptance properties in the governing authorization passed together. Codex
therefore recommends `ready_for_real_migration=true` for owner substantive acceptance. This is a
technical readiness recommendation, not an owner acceptance or authorization to begin a real
migration automatically.

The next genuine gate is owner review and substantive acceptance of this corrected result. Merge of
the corrective branch into `main`, and any real-project migration, remain separately unauthorized.

## Remaining limitations

- Permission profiles remain beta and require revalidation after material Codex permission-model
  changes.
- Complete Codex session archive coverage remains unverified under the deferred repository control.
- The corrected model requires a trusted controller to invoke the governed runner after candidate
  generation; a standalone fresh session intentionally cannot write protected Git metadata.
