# Example: an upgrade comes too late

**Assumptions:** Start with 10 coins. Each completed expedition awards 8 and costs 3 in mandatory repairs. An optional upgrade costs 30. No randomness or other spending.

**Trajectory after repair:** 10 -> 15 -> 20 -> 25 -> 30. The upgrade is affordable after four successful expeditions. Buying it leaves 0; verify that a player with 0 can still start and finish the next expedition.

If the target is two expeditions, an illustrative price is 20. That is a pacing proposal, not evidence the upgrade becomes satisfying. Check what other purchase is delayed and whether the upgrade removes all later challenge.

**Failure case:** If repairs must be prepaid and an expedition can return empty, the player could become unable to start. Specify a recoverable free action or a bounded loss rule, then test it.
