---
name: game-level-design
description: "Design playable spaces, routes, landmarks, encounters, and environmental guidance. Use for level layouts, navigation problems, exploration, or spaces that conflict with a game mechanic."
---

# Level and Spatial Design

Establish what the player must be able to do in the space and what the space should make them feel. Model the functional structure before choosing dimensions, decoration, or an engine representation.

## Lay out and inspect

1. Define objectives, movement capabilities, interaction ranges, hazards, checkpoints, entry/exit states, and any constraints already supplied. Label missing dimensions and traversal values as assumptions.
2. Choose a useful abstraction: line, grid, network, regions in continuous space, or overlapping spaces. Represent connectivity and visibility separately; a visible destination need not be reachable yet.
3. Place meaningful decisions and consequences. Explain the purpose of optional routes, shortcuts, backtracking, safe spaces, and bottlenecks. Verify that locked gates do not hide their own required keys.
4. Sequence learning, practice, combination, and variation only as needed for the experience. Match encounters to available information and player ability, not only geometric space.
5. Guide attention through goals, constraints, landmarks, contrast, characters, sound, and framing. Explain how cues relate to world logic and how players recover when they miss them.
6. Inspect contradictions: a refuge that constantly harms the player, an exploration game that punishes every detour, or a traversal move that the geometry cannot support. Preserve deliberate tensions when they serve the stated experience.
7. Walk critical and alternate paths, including failure/retry and sequence-break cases. Test a rough blockout or physical mockup at the actual movement scale before polishing visuals.

## Deliver

Provide a route or adjacency diagram, encounter/space purpose table, cue plan, traversal assumptions, and walkthrough. State whether reachability was reasoned about, simulated, or tested in a playable build; do not treat a diagram as proof of movement feel.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 10, Some Elements Are Game Mechanics: printed pp. 129-169; PDF pages 158-198.
- Chapter 16, Story and Game Structures Can Be Artfully Merged with Indirect Control: printed pp. 283-298; PDF pages 312-327.
- Chapter 19, Worlds Contain Spaces: printed pp. 329-343; PDF pages 358-372.
- Relevant lenses: 21, 71, 72, 73, 82, 83.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
