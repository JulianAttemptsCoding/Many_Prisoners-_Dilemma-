# Many Prisoners' Dilemma

An iterated prisoner's dilemma tournament between **58 hand-written strategies**. Each round, both bots
choose *split* (cooperate) or *steal* (defect):

| | opponent splits | opponent steals |
|---|---|---|
| **you split** | 3 / 3 | 0 / 5 |
| **you steal** | 5 / 0 | 1 / 1 |

Every move has a **5% chance of being flipped** (`apply_error`). That noise is what makes the
tournament interesting: strategies that never forgive spiral into mutual defection after one accidental
steal, and exploiters get punished by strategies that retaliate.

Pure Python standard library. No installation needed.

## Verify in one minute

```bash
python main.py                 # round-robin, 58 bots, 200 rounds per match, seed 7  (~1 s)
python main.py --repeats 20    # 20 seeds: who wins, and how often
python main.py --classic       # the original tournament format (see below)
```

Expected output for the default run (seed 7):

```
Round-robin: 58 bots, 200 rounds per match, 5% move noise, seed 7
 1. Persistent Bully | Starts by defecting. Cooperates only if the opponent retaliates three times in a row. | Total Score: 28429
 2. Cautious Bot | Cooperates only if the opponent has cooperated more than 70% of the time. | Total Score: 27714
 3. Grudger | ... | Total Score: 27608
```

Across seeds 7–26, **Persistent Bully wins 14 of 20 and Cautious Bot wins 6**. Both withhold
cooperation until the opponent has earned it. Persistent Bully opens by defecting, and Cautious Bot cooperates
only with opponents that have cooperated more than 70% of the time. Which strategy wins depends on the field:
these results are for this particular mix of 58 bots.

## How it's built (`main.py`)

| Piece | What it does |
|---|---|
| `PAYOFFS` | the payoff matrix above |
| strategy functions | `fn(bot_history, opponent_history) -> 'split' \| 'steal'`. Each sees both full move histories. Some are stochastic (forgive 10/30/50%, defect 70/80%). |
| `apply_error` | flips any move with probability 0.05 |
| `play_round` / `simulate_game` | one round / one 200-round match |
| `get_bots()` | the 58 strategies with plain-English descriptions |
| `round_robin(bots, rounds, seed)` | every pair plays exactly once. Seeded, so results are reproducible. |
| `classic_tournament(bots)` | the original format, kept as written |

### Round-robin vs. classic
The first version (`--classic`) chose a random match length of 150–250 rounds. For each pair, it also had
a 50% chance of making the first bot **play itself** instead, and both sides of that self-match counted
toward the bot. That inflates scores at random, so rankings changed a lot between runs.

The default is now a clean round-robin: every pair plays exactly once, with a fixed number of rounds and a
seed. The classic mode is still there for comparison.

## Ideas to extend
- Evolutionary dynamics: replicate high scorers each generation, as in Axelrod's ecological tournament.
- Measure how the winner changes as the noise rate goes from 0% to 20%.
