# Game Design Lenses

An engine-independent plugin with **20 practical game-design skills**, adapted from Jesse Schell's *The Art of Game Design: A Book of Lenses* (2008). Created by [Miguel Duran](https://github.com/mduranx64). The repository also offers a portable Agent Skills bundle for OpenCode, Gemini CLI, GitHub Copilot, and Cursor.

## Start here

Use natural requests such as:

- "Review my game concept and prioritize the next test."
- "Turn my idea into a playable core loop."
- "Check whether this reward economy creates a dominant strategy."
- "Design a puzzle with clues, a solution, and a hint ladder."
- "Plan a playtest for this prototype."

After installation, skills can also be selected explicitly. In Codex, use `$game-lens-review`, `$game-mechanics`, or `$game-playtest` (or the plugin-qualified name shown by the skill picker). In Claude Code, use `/game-design-lenses:game-lens-review`, `/game-design-lenses:game-mechanics`, or `/game-design-lenses:game-playtest`.

## Included workflows

| Skill | Purpose |
| --- | --- |
| [game-design-brief](skills/game-design-brief/SKILL.md) | Turn a game idea into a testable design brief |
| [game-player-experience](skills/game-player-experience/SKILL.md) | Match the experience to real player motivations |
| [game-mechanics](skills/game-mechanics/SKILL.md) | Specify rules, state changes, and meaningful actions |
| [game-balance](skills/game-balance/SKILL.md) | Diagnose unfairness and dominant strategies |
| [game-economy](skills/game-economy/SKILL.md) | Connect resources and rewards to player decisions |
| [game-puzzles](skills/game-puzzles/SKILL.md) | Build solvable puzzles with clear clues and progress |
| [game-controls-feedback](skills/game-controls-feedback/SKILL.md) | Make controls and game state understandable |
| [game-pacing](skills/game-pacing/SKILL.md) | Shape anticipation, contrast, and satisfying payoffs |
| [game-narrative](skills/game-narrative/SKILL.md) | Connect story consequences to player actions |
| [game-world-characters](skills/game-world-characters/SKILL.md) | Build playable worlds and purposeful characters |
| [game-level-design](skills/game-level-design/SKILL.md) | Shape routes, encounters, and readable spaces |
| [game-art-direction](skills/game-art-direction/SKILL.md) | Connect visual and audio choices to the experience |
| [game-social-design](skills/game-social-design/SKILL.md) | Design cooperation, competition, and healthy communities |
| [game-prototype](skills/game-prototype/SKILL.md) | Test the riskiest design assumption with a small prototype |
| [game-playtest](skills/game-playtest/SKILL.md) | Turn real play observations into design decisions |
| [game-design-document](skills/game-design-document/SKILL.md) | Write the design information a team actually needs |
| [game-technology-fit](skills/game-technology-fit/SKILL.md) | Match technology choices to the intended experience |
| [game-pitch](skills/game-pitch/SKILL.md) | Pitch the experience with credible scope and evidence |
| [game-design-impact](skills/game-design-impact/SKILL.md) | Connect design purpose to effects on players |
| [game-lens-review](skills/game-lens-review/SKILL.md) | Find the most consequential game design problems |

## How the plugin works

Each skill has a focused trigger, an actionable workflow, an original worked example, and chapter/lens references. Skills support normal automatic discovery. There are no required MCP servers, API keys, engine integrations, executable hooks, or network services. The core design workflows work from the supplied project context; tasks involving current external facts may still need current sources.

The [skill map](references/skill-map.md) explains routing. The [100-lens index](references/lens-index.md) and [chapter map](references/chapter-map.md) provide source locations. [Source notes](references/source-notes.md) distinguish the book's concepts from the plugin's adaptations.

The book itself is not bundled. Page references match the supplied 2008 PDF. The plugin supports digital games, tabletop games, and physical play; it does not force an engine or automatically turn a design request into implementation.

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks actually completed and their limits. The [evaluation scenarios](evals/scenarios.md) provide reusable prompts for future checks. Structural validation alone does not establish the quality of game-design advice, and no plugin evaluation should be represented as human playtesting.

## Installation

This folder contains Codex, Claude Code, and Cursor manifests alongside the canonical `skills/`. From the repository root, follow the [repository guide](../../README.md) for installation in each agent. Start a new task or session so the skills are discovered.
