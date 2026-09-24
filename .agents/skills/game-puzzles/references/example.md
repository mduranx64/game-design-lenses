# Example: three sluice gates

**State:** Gates A, B, C are closed, represented as (0,0,0). A lever toggles its own gate only. An open gate contributes A=1, B=2, C=4 units of water. The target is exactly 5, shown on a gauge. Actions are reversible.

**Solution:** Open A: (1,0,0), flow 1. Open C: (1,0,1), flow 5. Opening C then A also works. All 8 possible gate states yield different totals from 0 to 7, so this is the unique target state, with multiple action orders.

**Clues:** Gate capacities are visibly marked. The gauge updates after each action.

**Hints:** Notice the capacity marks -> find two capacities totaling 5 -> try the smallest and largest -> open A and C only.

**Design limit:** This is a teaching puzzle, not a sustained challenge. A later puzzle could add a real interaction between gates after players understand the rule.
