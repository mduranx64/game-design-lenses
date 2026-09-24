---
name: game-economy
description: "Design or tune in-game resources, rewards, sinks, progression costs, and failure recovery. Use for currency inflation, grind, pacing of upgrades, or rewards that players ignore."
---

# Game Economy and Progression

Start with the decisions the economy should make possible. Identify what players want to accomplish and why a resource matters inside those goals. A resource is useful when it affects a valued decision; more currencies do not automatically add depth.

## Model the economy

1. Inventory resources and rewards: sources, sinks, starting balances, storage caps, conversion rules, transferability, and reset/persistence boundaries. Include time, information, access, and social rewards when they matter.
2. Track a representative session or turn: next balance = current balance + inflows - outflows. Give rates explicit units and conditions. Distinguish mandatory upkeep from optional purchases.
3. Identify competing uses for scarce resources and how the player learns the tradeoff. Consider a universal currency versus specialized ones based on the desired choices and cognitive cost.
4. Estimate time to meaningful milestones for novice, typical, and expert assumptions. Separate deterministic arithmetic from stochastic estimates. Look for dead-end states, positive feedback that widens advantage, hoarding without purpose, and currency that loses its role.
5. Tie rewards to understandable achievement and failure costs to an intended lesson or tension. Inspect recovery time and whether losing erases more progress than the experience can support.
6. Propose a small change and examine both early and late play. If randomness matters, include distributions and unlucky sequences rather than only the mean.

## Deliver

Provide a source/sink table, explicit assumptions, a worked resource trajectory, milestone estimates, and tests of meaningful choice and recovery. Treat monetization as a separate scope decision. Never quietly add purchases, daily obligations, or retention mechanics to a request about an in-game economy.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 3, The Experience Rises Out of a Game: printed pp. 23-38; PDF pages 53-68.
- Chapter 10, Some Elements Are Game Mechanics: printed pp. 129-169; PDF pages 158-198.
- Chapter 11, Game Mechanics Must Be in Balance: printed pp. 171-205; PDF pages 200-234.
- Relevant lenses: 5, 28, 33, 39, 40, 41, 46, 47.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
