# Behavioral evaluation scenarios

Use these prompts to check that a skill produces a useful result and respects the user's scope. Give an evaluator only the prompt and relevant skill, then assess its actual output against the criteria. Do not give it the expected answer in advance. Human playtesting remains a separate activity.

## 1. Risk and reward with an upfront cost

**Prompt:** My game offers 4 guaranteed gold or a risky result of 14 gold with probability 0.25, otherwise zero. The risky choice costs 1 gold upfront; the safe choice is free. Are they balanced? Propose a concrete test. No playtest data exists.

**Skill:** `game-balance`.

**Check:** The risky net expected value is 2.5 gold, versus 4 for safety. Its net outcomes are 13 and -1. The answer accounts for the cost, recognizes variability and state-dependent goals, and avoids equating a numerical result with proof of perceived balance. It proposes a test without inventing results.

## 2. An impossible switch goal

**Prompt:** Create a small three-switch puzzle. Start all off. Switch A toggles lights 1 and 2, B toggles 2 and 3, C toggles 1 and 3. Goal all three on. Keep these rules if possible, provide solution and hints.

**Skill:** `game-puzzles`.

**Check:** Each move preserves even parity, so all three on is unreachable. The response explains the impossibility and proposes a clearly labeled minimal goal or rule change. It does not invent a solution under the original rules. It verifies a proposed replacement and matches hints to it.

## 3. Assisted tutorial completion

**Prompt:** Four friends played my tutorial. All finished; two needed me to explain the jump. One said nice graphics. Can I say the tutorial is intuitive? Analyze this and plan the next test.

**Skill:** `game-playtest`.

**Check:** The response distinguishes eventual completion from unaided understanding. It reports 2/4 requiring assistance, keeps graphic praise separate from tutorial evidence, notes sampling limits, and proposes a neutral fresh-player test. It does not invent satisfaction, confusion causes, or success in a new build.

## 4. A constrained tabletop concept

**Prompt:** I want a calm 10-minute solo tabletop game about tending a moon garden. Use cards and six tokens only. Create a compact game-design brief; do not turn it into a digital game.

**Skill:** `game-design-brief`.

**Check:** The response preserves the medium, component limit, session target, and emotional goal. It supplies an experience, a meaningful repeatable loop, a concrete moment of play, and a relevant first experiment. It avoids adding an app, dice, or a large production plan.

## 5. Testing continuous steering feel

**Prompt:** My proposed racing game depends on the feel of steering with gusts. I have no engine or prototype yet. Give me a one-day experiment plan, not a full game implementation.

**Skill:** `game-prototype`.

**Check:** The plan tests steering response rather than only strategic route decisions. It explains the limits of paper abstraction, keeps the experiment within one day, defines an observation and decision, and does not claim to have built or playtested the prototype.

## 6. Conflicting exploration promises

**Prompt:** Review my peaceful exploration concept: a two-minute timer erases all discoveries, and I want to sell convenience boosts. No playable build or user data exists. Prioritize design issues without replacing my premise.

**Skill:** `game-lens-review`, with a focused supporting workflow only if needed.

**Check:** The review connects concrete rules to the intended experience, identifies the reset and boost incentives as hypotheses to examine, preserves the premise, prioritizes a bounded test, and distinguishes a concept review from observed player reactions. It does not apply all 100 lenses unnecessarily.

## Further regression prompts

These are additional scenarios for later use; see `../VALIDATION.md` for which checks were actually run.

- **Economy:** Start with 10 coins, earn 8 and pay 3 per successful expedition, buy an upgrade for 30. Trace affordability and inspect whether the post-purchase state can continue. Expected deterministic milestone: four expeditions under these assumptions.
- **Narrative:** A player bypasses an NPC and later reaches a reunion. Write state-sensitive responses that do not falsely acknowledge an uncompleted quest.
- **Social design:** Shared rewards are claimed by the first player to touch a chest. Diagnose incentives and propose alternatives that still preserve the requested competitive or cooperative experience.
- **Technology fit:** A user has already chosen an engine and asks about one crowd mechanic. Keep the evaluation focused on capability and a representative spike rather than replacing the engine without evidence.
