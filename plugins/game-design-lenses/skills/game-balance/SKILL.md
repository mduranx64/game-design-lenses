---
name: game-balance
description: "Analyze fairness, challenge, dominant strategies, risk and reward, randomness, duration, and complexity in game rules. Use for tuning or a balance review; distinguish numerical analysis from player evidence."
---

# Game Balance

Define what balance means for this particular experience. Equal statistics, identical win rates, and symmetric roles are not universal goals. Record player skill, matchup, map, game phase, and sample limitations before interpreting outcomes.

## Analyze and tune

1. Describe the reported problem and evidence. Separate a rule defect, a comprehension issue, a tuning issue, and a deliberate asymmetry.
2. Compare actual decision situations. List options, costs, risks, opportunity costs, and when each should be preferred. Check whether an option dominates under all relevant conditions or only under narrow assumptions.
3. For chance, calculate expected value as sum(probability * outcome value), including losses and costs consistently. Check that probabilities sum to one. Also examine variance, streaks, worst cases, perceived odds, and the player's ability to recover. Do not equate equal expected value with equal experience.
4. Select relevant balance dimensions: fairness; challenge/success; meaningful choice; skill/chance; mental/physical demands; competition/cooperation; duration; rewards; punishment; freedom/guidance; simplicity/complexity; detail/imagination. Use these as prompts, not a mandatory scorecard.
5. Prefer a small change whose predicted effect can be explained. Inspect feedback loops, first-mover advantage, role interactions, and whether an added exception costs more clarity than it gains. Preserve distinctive quirks when they support the experience.
6. Define the comparison, player groups, measurements, and reversal condition before testing. Treat adaptive difficulty as a design choice with trust and competitive-fairness tradeoffs, not an automatic fix.

## Deliver

Return the diagnosis, assumptions and calculations, proposed parameter/rule changes, expected tradeoffs, and a focused test. Numerical models may rule out a claim or identify a candidate; they cannot certify that the game feels balanced.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 10, Some Elements Are Game Mechanics: printed pp. 129-169; PDF pages 158-198.
- Chapter 11, Game Mechanics Must Be in Balance: printed pp. 171-205; PDF pages 200-234.
- Relevant lenses: 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44, 45, 47.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
