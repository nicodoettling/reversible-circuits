# Self-Improvement Protocol

Agents may improve this skill when work in this project reveals durable, reusable knowledge.

## Update Triggers

Update `SKILL.md`, `references/`, or `scripts/` when:

- the same setup or diagnostic code is written more than once,
- a sampler bug recurs or is easy to prevent with instructions,
- an experiment establishes a stable workflow or falsifies a tempting approach,
- a new exact reference method becomes part of the standard validation path,
- the user explicitly asks to consolidate knowledge.

## Update Rules

- Keep `SKILL.md` concise and procedural.
- Put mathematical detail and experiment conventions in `references/`.
- Put repeatable deterministic actions in `scripts/`.
- Avoid adding broad research notes that belong in `HANDOFF.md`.
- Validate the skill after edits with the skill-creator validator.
- Test any new or changed script with a representative command.

## Autonomy Loop

For long agentic runs:

1. Create an experiment folder.
2. Write the objective and target distribution before coding.
3. Implement the smallest testable change.
4. Run exact small-case validation.
5. Record results and interpretation.
6. Update the sampler or diagnostics.
7. Promote only durable lessons into this skill.

If a run changes the project-level research assessment, update `HANDOFF.md`. If it changes how agents should work, update this skill.
