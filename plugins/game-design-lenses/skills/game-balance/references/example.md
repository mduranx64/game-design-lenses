# Example: equal means, different risk

**Given:** Safe route pays 4 tokens. Risky route pays 10 with probability 0.4 and 0 otherwise. Both take one turn; there are no extra costs.

Safe EV = 4. Risky EV = 0.4 * 10 + 0.6 * 0 = 4. Risky variance = 0.4 * (10 - 4)^2 + 0.6 * (0 - 4)^2 = 24. Safe variance is 0.

Equal EV does not make these choices interchangeable. A player who needs at least 6 this turn can only succeed via the risky route. A player who needs 4 and cannot recover from failure may prefer safety. If the game never creates either situation, the risk decision may be weak.

**Test:** Compare choices in states needing 4 versus 6 tokens, then ask players what they expected and why. Do not adjust the payout until the available information and consequences are understood.
