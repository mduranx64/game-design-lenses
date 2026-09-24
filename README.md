# Game Design Lenses for Codex

An independent, open source Codex plugin with 20 engine-independent skills for designing and reviewing digital, tabletop, and physical games. The workflows draw on game-design concepts discussed in Jesse Schell's *The Art of Game Design: A Book of Lenses* (2008), and add original procedures, examples, and evaluation scenarios.

## Install from GitHub

After this repository is public, add its marketplace and install the plugin:

```sh
codex plugin marketplace add mduranx64/game-design-lenses
codex plugin add game-design-lenses@mduranx64-game-design
```

Start a new Codex task after installation. In the Codex app, you can also add the GitHub marketplace and select the plugin from the plugin picker. The repository's marketplace catalog is [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json); the plugin is in [`plugins/game-design-lenses/`](plugins/game-design-lenses/).

## What is included

The plugin provides workflows for briefs, player experience, mechanics, balance, economies, puzzles, controls, pacing, narrative, worlds, levels, art direction, social design, prototypes, playtests, design documents, technology fit, pitches, impact, and overall design review. See the [plugin guide](plugins/game-design-lenses/README.md) for the full list and example prompts.

The [validation record](plugins/game-design-lenses/VALIDATION.md) describes structural checks and six independent assistant exercises. These checks are not human playtests or a guarantee of game-design quality.

## Source and rights

The plugin's original content is licensed under [MIT](LICENSE). The book, its PDF, and extracted text are **not** included or licensed here. Lens names and edition-specific source locations are supplied for reference; see [source and adaptation notes](plugins/game-design-lenses/references/source-notes.md). This is an independent adaptation and is not affiliated with or endorsed by Jesse Schell or the publisher.

## Contributing

Issues and pull requests are welcome. For a skill change, describe the design problem it addresses, include a concrete example, and keep source-derived ideas distinguishable from new guidance. Do not submit scans, extracted book text, copied figures, long quotations, credentials, or private project data. Validate the plugin and changed skills before submitting.
