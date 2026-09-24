---
name: game-puzzles
description: "Create or repair game puzzles with clear goals, readable rules, progress, clues, and verified solutions. Use for puzzle chains, hint design, difficulty ramps, and player bottlenecks."
---

# Puzzle Design

Establish the intended insight and what players can observe and manipulate. Decide whether the puzzle is about deduction, exploration, spatial reasoning, a perceptual shift, or another specific skill. Integrate it with the game's existing actions and fiction.

## Construct and verify

1. Define the initial state, legal actions, visible information, and success condition. Make the first useful interaction discoverable without revealing the solution.
2. Work out at least one complete solution before presenting the puzzle. Trace state changes and confirm every required clue is reachable before it is needed. Check alternative valid solutions rather than rejecting them because they differ from the intended path.
3. Provide intermediate feedback that distinguishes progress from arbitrary activity. Give players credible evidence that the problem can be solved.
4. Teach concepts before combining them. A sequence can grow toward a final synthesis; parallel branches can let players make progress elsewhere when stuck. Ensure optional branches are truly optional.
5. Write a hint ladder: orient attention, expose a relevant relationship, suggest a next action, then offer a solution or bypass if the experience calls for one. State any cost or consequence of taking help.
6. Inspect failure states, irreversible actions, resets, hidden prerequisites, and brute-force shortcuts. Perceptual shifts can produce a satisfying insight but are poor tools for finely graded difficulty; give them appropriate support.
7. Observe where fresh players first misunderstand or stall. Distinguish not knowing the goal, not understanding an action, missing evidence, and failing to combine understood evidence.

## Deliver

Provide a playable puzzle specification, solution trace, dependency structure, staged hints, and a test plan. Explicitly state if solvability has only been checked manually. In this edition, lens 48 concerns getting started with a puzzle; modern disability access requires additional considerations.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 12, Game Mechanics Support Puzzles: printed pp. 207-219; PDF pages 236-248.
- Relevant lenses: 48, 49, 50, 51, 52.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
