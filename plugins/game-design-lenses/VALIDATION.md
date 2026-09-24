# Validation record

Validated on 2026-09-24.

## Structural and source checks

- The bundled Codex plugin validator accepts the manifest.
- Claude Code 2.1.278 accepts the plugin and marketplace manifests in strict mode. The same 20 skill folders are shared by Codex and Claude Code.
- The bundled skill validator accepts all 20 skill entrypoints.
- Each skill has UI metadata, an explicit invocation example, a worked example, and relevant source references.
- The lens index contains exactly 100 unique entries, numbered 1-100. Each lens number and printed page was checked against the extracted text at the specified PDF page of the supplied book.
- Every primary lens route points to an existing skill that names the corresponding lens.
- Local Markdown links resolve within the plugin. No source PDF, extracted book text, unfinished scaffold placeholder, or machine-specific absolute path is bundled.
- The tetrad and interest-curve figures were visually inspected in the source PDF to check the conceptual interpretation. The plugin contains no copied figures.

## Independent behavioral checks

Two independent assistant passes completed six real prompts using the generated skills and relevant references. The resulting answers were reviewed against the scenario criteria in [evals/scenarios.md](evals/scenarios.md).

| Scenario | Workflow | Observed result |
| --- | --- | --- |
| Risky reward with upfront cost | Game balance | Calculated net EV 2.5 versus safe EV 4; preserved uncertainty about player experience. |
| Impossible three-switch puzzle | Puzzles | Detected the parity constraint; supplied a disclosed minimal repair, verified solution, and matching hints. |
| Tutorial with assisted completions | Playtesting | Separated completion from unaided comprehension; proposed a fresh-player test without invented results. |
| Calm solo tabletop game | Design brief | Preserved cards, exactly six tokens, solo play, and the calm ten-minute target as an unverified hypothesis. |
| One-day gust-steering experiment | Prototyping | Chose a representation capable of testing continuous control and delivered a plan without claiming execution. |
| Peaceful exploration with resets and boosts | Lens review | Prioritized concrete design tensions while preserving the premise and distinguishing hypotheses from observations. |

The actual generated responses are retained in [evals/observed-responses.md](evals/observed-responses.md). These are examples of assistant behavior during evaluation, not human participant results or a completed game project. No blocking skill defect was reproduced in these six cases.

## Numerical checks

Independent arithmetic and state enumeration confirmed:

- The risky-choice scenario's net EV is 2.5.
- The original two-lights-per-switch puzzle reaches only four even-parity states and cannot reach all three on.
- The safe-versus-risky worked example has equal EV 4 and risky variance 24.
- The economy example reaches a 30-coin upgrade after four successful expeditions under the stated deterministic assumptions.
- The pitch example's break-even figures are 12,000 and 15,000 units under its two illustrative scenarios.
- The sluice-gate example has the unique target configuration A open, B closed, C open, while permitting different action orders.

## Limits

Six of the twenty workflows received independent behavioral exercises. All twenty received structural validation and editorial review, but these checks do not establish reliability across every request or model. Skill selection was tested through explicit reading of the map and instructions; automatic selection in a newly opened Codex task is a separate integration check. No real player test, engine integration, or game build was performed.

Source verification established edition-specific locations for all indexed lenses. The workflows are newly written adaptations and operational additions, not verbatim author procedures. Source notes document the absent printed page 68 and the boundary between source concepts and modern adaptations. The repository README gives installation instructions; validation alone does not prove a public installation works.

Claude Code validation checks manifest syntax and structure. Installing from a public GitHub repository and invoking a skill in a live Claude Code session remain separate integration checks.
