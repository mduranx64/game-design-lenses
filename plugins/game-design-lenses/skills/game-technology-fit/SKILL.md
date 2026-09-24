---
name: game-technology-fit
description: "Evaluate how game technology or physical materials enable the intended experience and affect iteration. Use for technical feasibility risks and design tradeoffs, not as an automatic engine-selection or migration workflow."
---

# Technology Fit

Start with the experience and production constraints. Technology includes physical materials and rules enforcement as well as software. Respect an already chosen engine or medium unless the user asks to reconsider it or a demonstrated limitation blocks the design.

## Evaluate fit

1. Separate capabilities essential to the experience from optional enhancements. Explain what playable behavior would change if a capability were removed.
2. Describe the concrete workload and constraints: player count, state scale, input/output needs, device conditions, iteration turnaround, skills available, and production capacity as relevant.
3. Identify the technical assumption with the greatest design consequence. Propose a bounded spike that measures the actual workload and yields a keep/change decision.
4. Compare options on the stated constraints and cost of learning, iteration, integration, and fallback. Do not rank tools on fashionable features alone.
5. Label facts, measured results, and forecasts separately. For current products, versions, licenses, or support claims, consult current official documentation when available; the 2008 book cannot establish those facts.
6. If forecasting matters, use conditional scenarios and leading signals rather than confidently predicting one future. Prefer choices that keep a useful fallback when uncertainty is material.

## Deliver

Provide the capability-to-experience map, evidence/unknowns, relevant comparison, spike specification, and fallback. A benchmark proves only its measured setup. Do not present a concept description or synthetic test as proof the full game runs on target hardware.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 4, The Game Consists of Elements: printed pp. 39-46; PDF pages 69-76.
- Chapter 7, The Game Improves Through Iteration: printed pp. 75-95; PDF pages 104-124.
- Chapter 26, The Team Builds a Game with Technology: printed pp. 403-413; PDF pages 432-442.
- Relevant lenses: 7, 14, 92, 93.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
