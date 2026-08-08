# GACP Sandbox Remediation Authorization and Acceptance Rerun Handoff

- Date: 2026-08-07
- Owner decision: **APPROVED**
- Authorized branch: `gacp/codex-execution-automation-corrective-20260807`
- Governing diagnostic commit: `f38076467aa9055028b1c9e9beccbafa49fee838`
- Readiness entering operation: **false**
- Merge authorization: **NOT GRANTED**

## Authorization

The owner approves the least-privilege host remediation documented by the governing diagnostic commit above and the subsequent GACP sandbox verification and acceptance rerun.

Codex must retrieve that exact diagnostic result from Git and use its documented remediation; this handoff deliberately does not duplicate machine-specific diagnostic details.

Routine mechanical actions already inside this bounded authorization do not require additional governance approvals.

## Explicit exclusions

The owner does not authorize:

- disabling the global AppArmor user-namespace restriction;
- weakening the sandbox or using unrestricted execution;
- modifying unrelated projects;
- broadening the documented host remediation;
- force-pushing, deleting branches, rewriting history, or merging GACP;
- publishing credentials, secrets, raw sessions, or additional private machine-local details.

If the documented remediation no longer matches the host state or cannot be applied within these limits, stop fail-closed and return a governed blocker. Do not improvise a broader security change.

## Verification and acceptance

After the approved remediation:

1. Verify the security boundary the diagnostic required to remain enabled is still enabled.
2. Re-run the documented sandbox prerequisite probes.
3. Only if those probes pass, rerun the existing GACP fresh-session execution acceptance harness using disposable repositories.
4. The representative governed flow must reach real repository execution and cover the existing inspect/edit/validate/stage/commit/push/receipt scenario.
5. Required operational result: **0 manual human approval prompts for routine governed execution after setup**.
6. Report any one-time administrator authentication needed for this owner-authorized host remediation separately from the routine prompt count.
7. Unit or deterministic tests alone are insufficient for readiness.

`ready_for_real_migration` must remain `false` unless the complete acceptance scenario actually passes.

The returned human-readable and machine-readable results must clearly distinguish mechanical runner/publication success from substantive acceptance/readiness so a publication `PASS` cannot be mistaken for production readiness.

## Durable return

Publish the governed result and receipt only to the existing corrective branch within the established GACP result conventions. Report the remediation outcome, verification outcome, fresh-session acceptance result, routine prompt count, substantive readiness, recommendation, and next genuine owner gate.

Normal scoped publication to the corrective branch is authorized. Merge is not.

Return only a short conversational receipt so ChatGPT can retrieve and independently assess the authoritative Git result.
