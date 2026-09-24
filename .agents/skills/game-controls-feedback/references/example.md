# Example: a charge action seems broken

**Observed report:** Players tap the action button and say nothing happens. The design actually requires a hold.

**Trace:** Intention to launch -> press -> hidden charging state -> release -> projectile. The break occurs before players learn that holding changes the state.

**Proposal:** Begin a visible charge indicator on press, increase its fill during the hold, and show a ready cue at the threshold. Releasing early produces a small launch if that fits the rule, or a clearly explained cancellation. Give a distinct cue for interruption.

**Signal specification:** Charge fill conveys amount; shape change conveys readiness; an optional tone reinforces it. Neither color nor sound alone is necessary.

**Test:** Let fresh players use the action without a spoken explanation. Record whether they discover charging and correctly explain an interrupted attempt.
