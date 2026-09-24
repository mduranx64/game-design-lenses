# Example: a rescue flare feature note

**Purpose:** Let a separated teammate communicate a location without opening chat.

**Proposed behavior:** Activate a flare at the player's location; teammates see a temporary marker. The marker persists for 10 seconds, a provisional value to test. Enemies seeing it is an unresolved competitive-design decision.

**Inputs/outputs:** Activation requires a charge. It consumes one charge and creates a marker. If activation is invalid, retain the charge and show a reason.

**Dependencies:** Team visibility rules, marker priority in a crowded scene, and flare supply.

**Decision needed:** Shared versus individual supply. Compare whether either model lets one teammate consume every signal. Do not expand this one feature into an entire inventory specification unless that dependency requires it.
