---
name: game-mechanics
description: "Specify playable game rules, spaces, states, actions, goals, skill demands, and chance. Use to develop a core mechanic or diagnose ambiguous and contradictory rules."
---

# Game Mechanics

Turn the user's intended experience into rules another person could execute without inventing missing behavior. Retain the requested genre and medium. Use diagrams or tables when they clarify state, information, or ordering.

## Build the mechanical model

1. Define the functional space independently of its appearance: discrete or continuous, meaningful dimensions, boundaries, regions, and connections.
2. List relevant entities, attributes, allowed values, and state transitions. Mark information as public, private to particular players, or hidden from everyone. Distinguish unknown information from an event generated randomly.
3. Specify actions with preconditions, costs, targets, timing, effects, and feedback. State how simultaneous actions, ties, invalid actions, and terminal conditions resolve when they matter.
4. Separate directly available actions from strategies that emerge through combinations. Look for useful interactions between a small set of verbs and multiple objects before adding more buttons or exceptions.
5. Define immediate and longer goals, success/failure, and the player's room to choose goals. Explain the underlying state rule and the practical rule a player learns; differences must remain consistent.
6. Identify real skills exercised and where chance contributes. For random events, state outcomes, probabilities, replacement/dependence assumptions, and information available before commitment.
7. Walk through a concrete sequence from a valid start state. Search for contradictions, unreachable goals, no-progress loops, and a strategy that removes the intended decisions. A walkthrough checks rules; it does not establish fun or balance.

## Deliver

Provide an executable rules sketch, state/action table, one worked turn or short sequence, intended emergent decisions, and unresolved questions. Include implementation details only when needed for the user's requested medium.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 3, The Experience Rises Out of a Game: printed pp. 23-38; PDF pages 53-68.
- Chapter 10, Some Elements Are Game Mechanics: printed pp. 129-169; PDF pages 158-198.
- Relevant lenses: 6, 21, 22, 23, 24, 25, 26, 27, 28, 29.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
