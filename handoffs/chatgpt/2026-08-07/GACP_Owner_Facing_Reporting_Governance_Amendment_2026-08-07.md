# GACP owner-facing reporting governance amendment

## Control

- Project: Governed Artifact Continuity Protocol (GACP)
- Date: 2026-08-07
- Repository: `blainesmith33/governed_artifact_continuity_protocol`
- Working branch: `gacp/new-chat-handoff-automation-framework-20260803`
- Change class: owner-directed governance amendment
- Scope: owner-facing reporting around governed inter-agent work
- Merge authority: already granted for the accepted operational-kit publication, subject to a superseding handoff that explicitly includes this owner-directed amendment

## Owner direction

After asking to receive summaries of both what ChatGPT asks Codex to do and what Codex actually does, the owner clarified:

> this should be part of the governance of this system. you should always report what codex found, what it recommends, what you agree with, what needs to change, and I need summaries so that I can make informed decisions

This is a governance requirement, not a conversational preference.

## Required owner-facing behavior

For any governed job delegated to Codex or another cooperating agent:

1. Before execution, the owner-facing coordinating agent must give the owner a concise plain-English summary of what the delegated agent is being asked to accomplish. The substantive technical/governed handoff remains in Git.
2. After the delegated agent returns, the coordinating agent must retrieve the authoritative result and relevant evidence from Git rather than relying only on the conversational completion receipt.
3. The coordinating agent must then provide an owner-facing report that states, as applicable:
   - what the delegated agent found;
   - what it actually did;
   - what it recommends;
   - the coordinating agent's independent assessment;
   - what the coordinating agent agrees with and why;
   - what the coordinating agent disagrees with or believes needs correction;
   - validation results and current project state;
   - what happens next;
   - any genuine owner decision required, with enough context to support an informed decision.
4. A Codex or agent `PASS` label is evidence to review, not a substitute for the coordinating agent's independent assessment when a substantive acceptance or owner decision is involved.
5. The owner-facing summary must not become the durable transport for substantive inter-agent state. Git remains authoritative and carries the full governed artifacts.
6. The owner must not be required to paste or relay the full result between agents merely so the coordinating agent can review it.

## Purpose

This rule preserves meaningful human agency without turning the owner into an artifact courier. It ensures the owner can make informed governance decisions while the durable technical state, evidence, and inter-agent handoffs remain externalized in Git.

## Relationship to existing GACP rules

This amendment adds an owner-interpretation/reporting obligation to the existing Git-first communication model. It does not weaken:

- bounded pre-authorization of routine mechanical operations;
- existing stop conditions and genuine owner gates;
- repository validation and provenance requirements;
- the rule that conversation memory is not authoritative;
- the prohibition on using the owner as the normal transport between cooperating agents.

The root `AGENTS.md` must encode this behavior as a mandatory bootstrap rule so a fresh conforming agent can recover it without conversation memory.
