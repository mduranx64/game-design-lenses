# Game Design Lenses for Codex and Claude Code

An independent, open source plugin for Codex and Claude Code with 20 engine-independent skills for designing and reviewing digital, tabletop, and physical games. The workflows draw on game-design concepts discussed in Jesse Schell's *The Art of Game Design: A Book of Lenses* (2008), and add original procedures, examples, and evaluation scenarios.

Created by [Miguel Duran](https://github.com/mduranx64).

## Install in Codex

After this repository is public, add its marketplace and install the plugin:

```sh
codex plugin marketplace add mduranx64/game-design-lenses
codex plugin add game-design-lenses@mduranx64-game-design
```

Start a new Codex task after installation. In the Codex app, you can also add the GitHub marketplace and select the plugin from the plugin picker. The Codex marketplace catalog is [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json).

## Install in Claude Code

After this repository is public, run:

```sh
claude plugin marketplace add mduranx64/game-design-lenses
claude plugin install game-design-lenses@mduranx64-game-design
```

To test the local plugin without installing it, run `claude --plugin-dir ./plugins/game-design-lenses` from this repository. Try `/game-design-lenses:game-design-brief` in Claude Code. The Claude Code marketplace catalog is [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). Both platforms use the same [`skills/` directory](plugins/game-design-lenses/skills/) inside the plugin.

## What is included

The plugin provides workflows for briefs, player experience, mechanics, balance, economies, puzzles, controls, pacing, narrative, worlds, levels, art direction, social design, prototypes, playtests, design documents, technology fit, pitches, impact, and overall design review. See the [plugin guide](plugins/game-design-lenses/README.md) for the full list and example prompts.

The [validation record](plugins/game-design-lenses/VALIDATION.md) describes structural checks and six independent assistant exercises. These checks are not human playtests or a guarantee of game-design quality.

## Source and rights

The plugin's original content is licensed under [MIT](LICENSE). The book, its PDF, and extracted text are **not** included or licensed here. Lens names and edition-specific source locations are supplied for reference; see [source and adaptation notes](plugins/game-design-lenses/references/source-notes.md). This is an independent adaptation and is not affiliated with or endorsed by Jesse Schell or the publisher.

## Contributing

Issues and pull requests are welcome. For a skill change, describe the design problem it addresses, include a concrete example, and keep source-derived ideas distinguishable from new guidance. Do not submit scans, extracted book text, copied figures, long quotations, credentials, or private project data. Validate the plugin and changed skills before submitting.
