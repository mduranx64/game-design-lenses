# Example: a push-your-luck courier

**State:** Public position and stamina; private destination card; known bag composition. One turn begins with 3 stamina.

**Actions:** Move to an adjacent space for 1 stamina; deliver at the matching destination for 1 stamina; rest ends the turn and restores stamina next turn.

**Risk option:** Before moving through a flooded edge, draw a token from a bag with 3 safe and 1 delay token, returning it after the draw. Delay consumes 1 extra stamina. The player must have 2 stamina before attempting that edge, so a delay cannot create an undefined negative value.

**Worked turn:** Start with 3, cross a flooded edge and draw delay, leaving 1; deliver, leaving 0; end turn. If the draw were safe, one stamina would remain.

**Unresolved design question:** Does visible safety information create an interesting detour, or make one route obviously superior? That requires comparison and playtesting.
