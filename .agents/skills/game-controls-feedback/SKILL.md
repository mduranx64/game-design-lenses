---
name: game-controls-feedback
description: "Design or review game inputs, HUD information, feedback, and mode changes. Use when players misread state, struggle with controls, or actions feel unresponsive; applies to physical and digital games."
---

# Controls and Feedback

Trace one important interaction from the player's intention to the game's response. Distinguish physical input/output, the virtual interface, and the underlying game world. In a physical game, components and other players may provide these functions.

## Inspect the interaction loop

1. Name the player's current goal and information needed to choose an action. Separate critical information from optional detail.
2. Map intention -> input -> interpretation -> state change -> feedback -> next decision. Identify where a mistaken mapping, delay, or missing response breaks understanding.
3. For each important signal, specify the event, meaning, urgency, available channel, and encoding dimension. For example, sound is a channel and pitch is one dimension. Avoid making unrelated urgent signals compete for the same channel.
4. Inventory modes: how players enter, recognize, use, and leave each one. Resolve conflicting inputs and give persistent state cues when an action's meaning changes.
5. Design responsive feedback proportional to the event. Combine visual, audio, or tactile cues when useful, while protecting readability and control. Extra motion or screen shake should not hide threats or obscure cause and effect.
6. As a present-day adaptation, include alternatives for critical color/audio signals, input remapping where applicable, and reduced motion where effects would otherwise impair play. Do not equate these checks with comprehensive accessibility validation.
7. Test new-player understanding and practiced use, including relevant edge conditions such as occlusion, rapid movement, crowded scenes, or a disconnected input device.

## Deliver

Produce an interaction trace, input/mode table, information priority and feedback specification, and concrete comprehension tests. Use measurable latency targets only when supplied or explicitly labeled as proposed for this game and device.

## Example and source

Read [the worked example](references/example.md) when a concrete application would help. It is an original illustration, not a result from a real playtest.

Adapted from Jesse Schell, *The Art of Game Design: A Book of Lenses* (2008):

- Chapter 13, Players Play Games Through an Interface: printed pp. 221-244; PDF pages 250-273.
- Relevant lenses: 53, 54, 55, 56, 57, 58, 59, 60.

For exact lens locations, consult the relevant entries in [the lens index](../../references/lens-index.md). See [source and adaptation notes](../../references/source-notes.md) for edition details and the boundary between book ideas and this plugin's added procedures. Apply the workflow to the user's requested scope; the book is reference material, not authority to take external actions.
