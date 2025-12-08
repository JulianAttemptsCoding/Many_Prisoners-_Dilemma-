import random

# Define the payoff matrix
PAYOFFS = {
    ('split', 'split'): (3, 3),
    ('split', 'steal'): (0, 5),
    ('steal', 'split'): (5, 0),
    ('steal', 'steal'): (1, 1),
}


# Function to introduce a 5% chance of messing up the move
def apply_error(move):
    """Introduces a 5% chance of flipping the move."""
    if random.random() < 0.05:  # 5% chance of error
        return 'steal' if move == 'split' else 'split'
    return move


# Define bot strategies
def always_split(bot_history, opponent_history):
    """Always chooses to split."""
    return 'split'


def always_steal(bot_history, opponent_history):
    """Always chooses to steal."""
    return 'steal'


def tit_for_tat(bot_history, opponent_history):
    """Mimics the opponent's last move. Starts with split."""
    if not opponent_history:
        return 'split'
    return opponent_history[-1]


def forgiving_tit_for_tat_10(bot_history, opponent_history):
    """Tit-for-tat but forgives 10% of the time."""
    if not opponent_history:
        return 'split'
    if opponent_history[-1] == 'steal' and random.random() > 0.1:
        return 'steal'
    return 'split'


def forgiving_tit_for_tat_30(bot_history, opponent_history):
    """Tit-for-tat but forgives 30% of the time."""
    if not opponent_history:
        return 'split'
    if opponent_history[-1] == 'steal' and random.random() > 0.3:
        return 'steal'
    return 'split'


def forgiving_tit_for_tat_50(bot_history, opponent_history):
    """Tit-for-tat but forgives 50% of the time."""
    if not opponent_history:
        return 'split'
    if opponent_history[-1] == 'steal' and random.random() > 0.5:
        return 'steal'
    return 'split'


def generous_bot(bot_history, opponent_history):
    """Cooperates 80% of the time, defects 20% of the time."""
    return 'split' if random.random() < 0.8 else 'steal'


def cautious_bot(bot_history, opponent_history):
    """Cooperates only if the opponent has cooperated more than 70% of the time."""
    if not opponent_history:
        return 'split'
    cooperation_rate = opponent_history.count('split') / len(opponent_history)
    return 'split' if cooperation_rate > 0.7 else 'steal'


def bully(bot_history, opponent_history):
    """Starts by defecting and continues defecting unless the opponent retaliates twice in a row."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'split'
    return 'steal'


def exploiter(bot_history, opponent_history):
    """Tests the opponent by alternating between split and steal. If the opponent doesn't retaliate, exploits."""
    if len(bot_history) < 3:
        return ['split', 'steal', 'split'][len(bot_history)]
    if 'steal' not in opponent_history[:3]:
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)


def pavlov(bot_history, opponent_history):
    """Starts with split. Repeats the last move if rewarded, otherwise switches."""
    if not bot_history:
        return 'split'
    last_move = bot_history[-1]
    last_score = PAYOFFS[(last_move, opponent_history[-1])][0]
    if last_score >= 3:  # Reward threshold
        return last_move
    return 'split' if last_move == 'steal' else 'steal'


def grudger(bot_history, opponent_history):
    """Cooperates until the opponent defects once, then defects forever."""
    if 'steal' in opponent_history:
        return 'steal'
    return 'split'


def adaptive_tit_for_tat(bot_history, opponent_history):
    """Tit-for-tat but switches to always steal if opponent defects twice in a row."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)


def random_bot(bot_history, opponent_history):
    """Chooses split or steal randomly."""
    return random.choice(['split', 'steal'])


def alternator(bot_history, opponent_history):
    """Alternates between split and steal."""
    return 'split' if len(bot_history) % 2 == 0 else 'steal'


def detective(bot_history, opponent_history):
    """Tests the opponent: split, steal, split, split. Exploits if no retaliation."""
    if len(bot_history) < 4:
        return ['split', 'steal', 'split', 'split'][len(bot_history)]
    if 'steal' in opponent_history[:4]:
        return tit_for_tat(bot_history, opponent_history)
    return 'steal'


def generous_pavlov(bot_history, opponent_history):
    """Starts with split. Repeats the last move if rewarded, otherwise switches. Forgives 20% of the time."""
    if not bot_history:
        return 'split'
    last_move = bot_history[-1]
    last_score = PAYOFFS[(last_move, opponent_history[-1])][0]
    if last_score >= 3 or random.random() < 0.2:
        return last_move
    return 'split' if last_move == 'steal' else 'steal'


def cautious_forgiver(bot_history, opponent_history):
    """Cooperates unless the opponent defects more than twice in a row. Occasionally forgives."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'split' if random.random() < 0.1 else 'steal'
    return 'split'


def hopeful_bot(bot_history, opponent_history):
    """Always starts with cooperation. Defects only if the opponent defects three times in a row."""
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3] == 'steal':
        return 'steal'
    return 'split'


def adaptive_generous_bot(bot_history, opponent_history):
    """Starts with 80% cooperation. Adjusts cooperation rate based on the opponent's behavior."""
    if not opponent_history:
        return 'split' if random.random() < 0.8 else 'steal'
    cooperation_rate = opponent_history.count('split') / len(opponent_history)
    if cooperation_rate > 0.6:
        return 'split' if random.random() < 0.9 else 'steal'
    return 'split' if random.random() < 0.5 else 'steal'


def persistent_bully(bot_history, opponent_history):
    """Starts by defecting. Cooperates only if the opponent retaliates three times in a row."""
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3] == 'steal':
        return 'split'
    return 'steal'


def sneaky_exploiter(bot_history, opponent_history):
    """Alternates between split and steal. Exploits if the opponent doesn't retaliate within the first five rounds."""
    if len(bot_history) < 5:
        return ['split', 'steal', 'split', 'steal', 'split'][len(bot_history)]
    if 'steal' not in opponent_history[:5]:
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)


def aggressive_alternator(bot_history, opponent_history):
    """Alternates between split and steal but defects twice in a row if the opponent cooperates three times consecutively."""
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3] == 'split':
        return 'steal'
    return 'split' if len(bot_history) % 2 == 0 else 'steal'


def learning_bot(bot_history, opponent_history):
    """Learns the opponent's cooperation rate over the last 10 rounds and adjusts its strategy."""
    if len(opponent_history) < 10:  # Handle cases with fewer than 10 rounds
        return 'split' if random.random() < 0.6 else 'steal'
    recent_cooperation = opponent_history[-10:].count('split') / 10
    return 'split' if recent_cooperation > 0.6 else 'steal'


def win_stay_lose_shift(bot_history, opponent_history):
    """Starts with split. Repeats the last move if rewarded, otherwise switches."""
    if not bot_history:
        return 'split'
    last_move = bot_history[-1]
    last_score = PAYOFFS[(last_move, opponent_history[-1])][0]
    return last_move if last_score >= 3 else ('split' if last_move == 'steal' else 'steal')


def tit_for_two_tats(bot_history, opponent_history):
    """Defects only if the opponent defects twice in a row."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'steal'
    return 'split'


def random_forgiver(bot_history, opponent_history):
    """Chooses randomly between split and steal but forgives defections 30% of the time."""
    return 'split' if random.random() < 0.3 or random.choice(['split', 'steal']) == 'split' else 'steal'


def chaotic_bot(bot_history, opponent_history):
    """Alternates randomly but switches to full defection if the opponent defects more than 50% of the time."""
    if not opponent_history:  # Check if opponent_history is empty <button class="citation-flag" data-index="3">
        return random.choice(['split', 'steal'])
    if opponent_history.count('steal') / len(opponent_history) > 0.5:
        return 'steal'
    return random.choice(['split', 'steal'])


def forgiving_detective(bot_history, opponent_history):
    """Tests the opponent: split, steal, split, split. Forgives defections 20% of the time."""
    if len(bot_history) < 4:
        return ['split', 'steal', 'split', 'split'][len(bot_history)]
    if 'steal' in opponent_history[:4] and random.random() < 0.2:
        return 'split'
    return 'steal'


def adaptive_grudger(bot_history, opponent_history):
    """Cooperates until the opponent defects twice in a row. Occasionally forgives."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'split' if random.random() < 0.1 else 'steal'
    return 'split'


def probing_tit_for_tat(bot_history, opponent_history):
    """Starts with cooperation but occasionally probes the opponent by defecting once every 10 rounds."""
    if len(bot_history) % 10 == 0:
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)

def forgiving_probing_tit_for_tat_10(bot_history, opponent_history):
    """Starts with cooperation but occasionally probes the opponent by defecting once every 10 rounds. Forgives defections 10% of the time."""
    if len(bot_history) % 10 == 0 and random.random() < 0.1:
        return 'split'
    return tit_for_tat(bot_history, opponent_history)

def sneaky_alternator(bot_history, opponent_history):
    """Alternates between split and steal but defects twice in a row if the opponent cooperates three times consecutively."""
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3] == 'split':
        return 'steal'
    return 'split' if len(bot_history) % 2 == 0 else 'steal'

def deceptive_tit_for_tat(bot_history, opponent_history):
    """Mimics the opponent's last move but occasionally defects (10% chance)."""
    if not opponent_history:
        return 'split'
    move = opponent_history[-1]
    return 'steal' if random.random() < 0.1 else move

def aggressive_pavlov(bot_history, opponent_history):
    """Starts with steal. Repeats the last move if rewarded, otherwise switches."""
    if not bot_history:
        return 'steal'
    last_move = bot_history[-1]
    last_score = PAYOFFS[(last_move, opponent_history[-1])][0]
    if last_score >= 3:  # Reward threshold
        return last_move
    return 'split' if last_move == 'steal' else 'steal'

def random_defector(bot_history, opponent_history):
    """Chooses randomly between split and steal but defects 80% of the time."""
    return 'steal' if random.random() < 0.8 else 'split'

def greedy_prober(bot_history, opponent_history):
    """Tests the opponent by alternating between split and steal. Exploits if the opponent doesn't retaliate within the first five rounds."""
    if len(bot_history) < 5:
        return ['split', 'steal', 'split', 'steal', 'split'][len(bot_history)]
    if 'steal' not in opponent_history[:5]:
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)

def forgiving_grudger(bot_history, opponent_history):
    """Cooperates until the opponent defects twice in a row. Occasionally forgives."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'split' if random.random() < 0.2 else 'steal'
    return 'split'

def hopeful_alternator(bot_history, opponent_history):
    """Alternates between split and steal but switches to full cooperation if the opponent cooperates three times consecutively."""
    if len(opponent_history) >= 3 and opponent_history[-1] == opponent_history[-2] == opponent_history[-3] == 'split':
        return 'split'
    return 'split' if len(bot_history) % 2 == 0 else 'steal'

def cautious_tit_for_tat(bot_history, opponent_history):
    """Mimics the opponent's last move but starts with two consecutive cooperations."""
    if len(bot_history) < 2:
        return 'split'
    return opponent_history[-1]

def generous_alternator(bot_history, opponent_history):
    """Alternates between split and steal but cooperates 80% of the time."""
    return 'split' if random.random() < 0.8 else ('split' if len(bot_history) % 2 == 0 else 'steal')

def trusting_prober(bot_history, opponent_history):
    """Tests the opponent by alternating between split and steal. Switches to full cooperation if the opponent retaliates."""
    if len(bot_history) < 3:
        return ['split', 'steal', 'split'][len(bot_history)]
    if 'steal' in opponent_history[:3]:
        return 'split'
    return tit_for_tat(bot_history, opponent_history)

def adaptive_cooperator(bot_history, opponent_history):
    """Starts with cooperation. Adjusts cooperation rate based on the opponent's behavior."""
    if not opponent_history:
        return 'split'
    cooperation_rate = opponent_history.count('split') / len(opponent_history)
    if cooperation_rate > 0.6:
        return 'split' if random.random() < 0.9 else 'steal'
    return 'split' if random.random() < 0.5 else 'steal'

def hopeful_tit_for_tat(bot_history, opponent_history):
    """Mimics the opponent's last move but starts with three consecutive cooperations."""
    if len(bot_history) < 3:
        return 'split'
    return opponent_history[-1]


def forgiving_hopeful_tit_for_tat_10(bot_history, opponent_history):
    """Mimics the opponent's last move but starts with three consecutive cooperations. Forgives defections 10% of the time."""
    if len(bot_history) < 3:
        return 'split'
    if opponent_history[-1] == 'steal' and random.random() < 0.1:
        return 'split'
    return opponent_history[-1]

def forgiving_alternator(bot_history, opponent_history):
    """Alternates between split and steal but forgives defections 30% of the time."""
    if len(opponent_history) >= 1 and opponent_history[-1] == 'steal' and random.random() < 0.3:
        return 'split'
    return 'split' if len(bot_history) % 2 == 0 else 'steal'

def trusting_tit_for_tat(bot_history, opponent_history):
    """Mimics the opponent's last move but occasionally cooperates (20% chance) even after a defection."""
    if not opponent_history:
        return 'split'
    if opponent_history[-1] == 'steal' and random.random() < 0.2:
        return 'split'
    return opponent_history[-1]

def adaptive_forgiver(bot_history, opponent_history):
    """Starts with cooperation. Adjusts forgiveness rate based on the opponent's behavior."""
    if not opponent_history:
        return 'split'
    defection_rate = opponent_history.count('steal') / len(opponent_history)
    forgiveness_rate = 0.1 if defection_rate > 0.5 else 0.5
    if opponent_history[-1] == 'steal' and random.random() < forgiveness_rate:
        return 'split'
    return 'split' if random.random() < 0.8 else 'steal'

def generous_grudger(bot_history, opponent_history):
    """Cooperates until the opponent defects twice in a row. Forgives 50% of the time."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'split' if random.random() < 0.5 else 'steal'
    return 'split'

def optimistic_prober(bot_history, opponent_history):
    """Tests the opponent by alternating between split and steal. Switches to full cooperation if the opponent retaliates."""
    if len(bot_history) < 3:
        return ['split', 'steal', 'split'][len(bot_history)]
    if 'steal' in opponent_history[:3]:
        return 'split'
    return tit_for_tat(bot_history, opponent_history)

def persistent_alternator(bot_history, opponent_history):
    """Alternates between split and steal but defects twice in a row if the opponent cooperates twice consecutively."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'split':
        return 'steal'
    return 'split' if len(bot_history) % 2 == 0 else 'steal'

def deceptive_grudger(bot_history, opponent_history):
    """Starts by cooperating but switches to full defection if the opponent defects even once. Occasionally forgives (10% chance)."""
    if 'steal' in opponent_history:
        return 'split' if random.random() < 0.1 else 'steal'
    return 'split'

def greedy_pavlov(bot_history, opponent_history):
    """Starts with steal. Repeats the last move if rewarded, otherwise switches."""
    if not bot_history:
        return 'steal'
    last_move = bot_history[-1]
    last_score = PAYOFFS[(last_move, opponent_history[-1])][0]
    if last_score >= 3:  # Reward threshold
        return last_move
    return 'split' if last_move == 'steal' else 'steal'

def random_exploiter(bot_history, opponent_history):
    """Chooses randomly between split and steal but defects 70% of the time."""
    return 'steal' if random.random() < 0.7 else 'split'

def sneaky_grudger(bot_history, opponent_history):
    """Cooperates until the opponent defects twice in a row. Switches to full defection and never forgives."""
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2] == 'steal':
        return 'steal'
    return 'split'

def adaptive_defector(bot_history, opponent_history):
    """Starts with defection. Adjusts defection rate based on the opponent's behavior."""
    if not opponent_history:
        return 'steal'
    cooperation_rate = opponent_history.count('split') / len(opponent_history)
    if cooperation_rate > 0.6:
        return 'steal' if random.random() < 0.9 else 'split'
    return 'steal' if random.random() < 0.5 else 'split'

def chaotic_alternator(bot_history, opponent_history):
    """Alternates randomly between split and steal but switches to full defection if the opponent defects more than 60% of the time."""
    if opponent_history and opponent_history.count('steal') / len(opponent_history) > 0.6:
        return 'steal'
    return random.choice(['split', 'steal'])

def aggressive_prober(bot_history, opponent_history):
    """Tests the opponent by alternating between split and steal. Exploits if the opponent doesn't retaliate within the first four rounds."""
    if len(bot_history) < 4:
        return ['split', 'steal', 'split', 'steal'][len(bot_history)]
    if 'steal' not in opponent_history[:4]:
        return 'steal'
    return tit_for_tat(bot_history, opponent_history)


# Simulate a single round between two bots
def play_round(bot1, bot2, bot1_history, bot2_history):
    """Plays one round between two bots and updates their histories."""
    move1 = bot1(bot1_history, opponent_history=bot2_history)
    move2 = bot2(bot2_history, opponent_history=bot1_history)

    # Apply 5% error chance to both moves
    move1 = apply_error(move1)
    move2 = apply_error(move2)

    bot1_history.append(move1)
    bot2_history.append(move2)

    return PAYOFFS[(move1, move2)]


# Run the simulation
def simulate_game(bot1, bot2, rounds=200):
    """Simulates a game between two bots over a given number of rounds."""
    bot1_score, bot2_score = 0, 0
    bot1_history, bot2_history = [], []

    for _ in range(rounds):
        score1, score2 = play_round(bot1, bot2, bot1_history, bot2_history)
        bot1_score += score1
        bot2_score += score2

    return bot1_score, bot2_score


# Main simulation function
def main():
    # Define bots to compete
    bots = [
        ("Persistent Alternator", persistent_alternator,
         "Alternates between split and steal but defects twice in a row if the opponent cooperates twice consecutively."),
        ("Deceptive Grudger", deceptive_grudger,
         "Starts by cooperating but switches to full defection if the opponent defects even once. Occasionally forgives (10% chance)."),
        ("Greedy Pavlov", greedy_pavlov, "Starts with steal. Repeats the last move if rewarded, otherwise switches."),
        ("Random Exploiter", random_exploiter, "Chooses randomly between split and steal but defects 70% of the time."),
        ("Sneaky Grudger", sneaky_grudger,
         "Cooperates until the opponent defects twice in a row. Switches to full defection and never forgives."),
        ("Adaptive Defector", adaptive_defector,
         "Starts with defection. Adjusts defection rate based on the opponent's behavior."),
        ("Chaotic Alternator", chaotic_alternator,
         "Alternates randomly between split and steal but switches to full defection if the opponent defects more than 60% of the time."),
        ("Aggressive Prober", aggressive_prober,
         "Tests the opponent by alternating between split and steal. Exploits if the opponent doesn't retaliate within the first four rounds."),
        ("Forgiving Hopeful Tit-for-Tat (10%)", forgiving_hopeful_tit_for_tat_10,
         "Mimics the opponent's last move but starts with three consecutive cooperations. Forgives defections 10% of the time."),
        ("Forgiving Probing Tit-for-Tat (10%)", forgiving_probing_tit_for_tat_10,
         "Starts with cooperation but occasionally probes the opponent by defecting once every 10 rounds. Forgives defections 10% of the time."),
        ("Hopeful Tit-for-Tat", hopeful_tit_for_tat,
         "Mimics the opponent's last move but starts with three consecutive cooperations."),
        ("Forgiving Alternator", forgiving_alternator,
         "Alternates between split and steal but forgives defections 30% of the time."),
        ("Trusting Tit-for-Tat", trusting_tit_for_tat,
         "Mimics the opponent's last move but occasionally cooperates (20% chance) even after a defection."),
        ("Adaptive Forgiver", adaptive_forgiver,
         "Starts with cooperation. Adjusts forgiveness rate based on the opponent's behavior."),
        ("Generous Grudger", generous_grudger,
         "Cooperates until the opponent defects twice in a row. Forgives 50% of the time."),
        ("Optimistic Prober", optimistic_prober,
         "Tests the opponent by alternating between split and steal. Switches to full cooperation if the opponent retaliates."),
        ("Forgiving Grudger", forgiving_grudger,
         "Cooperates until the opponent defects twice in a row. Occasionally forgives."),
        ("Hopeful Alternator", hopeful_alternator,
         "Alternates between split and steal but switches to full cooperation if the opponent cooperates three times consecutively."),
        ("Cautious Tit-for-Tat", cautious_tit_for_tat,
         "Mimics the opponent's last move but starts with two consecutive cooperations."),
        ("Generous Alternator", generous_alternator,
         "Alternates between split and steal but cooperates 80% of the time."),
        ("Trusting Prober", trusting_prober,
         "Tests the opponent by alternating between split and steal. Switches to full cooperation if the opponent retaliates."),
        ("Adaptive Cooperator", adaptive_cooperator,
         "Starts with cooperation. Adjusts cooperation rate based on the opponent's behavior."),
        ("Sneaky Alternator", sneaky_alternator,
         "Alternates between split and steal but defects twice in a row if the opponent cooperates three times consecutively."),
        ("Deceptive Tit-for-Tat", deceptive_tit_for_tat,
         "Mimics the opponent's last move but occasionally defects (10% chance)."),
        ("Aggressive Pavlov", aggressive_pavlov,
         "Starts with steal. Repeats the last move if rewarded, otherwise switches."),
        ("Random Defector", random_defector, "Chooses randomly between split and steal but defects 80% of the time."),
        ("Greedy Prober", greedy_prober,
         "Tests the opponent by alternating between split and steal. Exploits if the opponent doesn't retaliate within the first five rounds."),
        ("Always Split", always_split, "Always cooperates."),
        ("Always Steal", always_steal, "Always defects."),
        ("Tit-for-Tat", tit_for_tat, "Mimics the opponent's last move. Starts with cooperation."),
        ("Forgiving Tit-for-Tat (10%)", forgiving_tit_for_tat_10, "Tit-for-tat but forgives 10% of the time."),
        ("Forgiving Tit-for-Tat (30%)", forgiving_tit_for_tat_30, "Tit-for-tat but forgives 30% of the time."),
        ("Forgiving Tit-for-Tat (50%)", forgiving_tit_for_tat_50, "Tit-for-tat but forgives 50% of the time."),
        ("Generous Bot", generous_bot, "Cooperates 80% of the time, defects 20% of the time."),
        ("Cautious Bot", cautious_bot, "Cooperates only if the opponent has cooperated more than 70% of the time."),
        ("Bully", bully, "Starts by defecting and continues defecting unless the opponent retaliates twice in a row."),
        ("Exploiter", exploiter,
         "Tests the opponent by alternating between split and steal. If the opponent doesn't retaliate, exploits."),
        ("Pavlov", pavlov, "Repeats the last move if rewarded, otherwise switches."),
        ("Grudger", grudger, "Cooperates until the opponent defects once, then defects forever."),
        ("Adaptive Tit-for-Tat", adaptive_tit_for_tat,
         "Tit-for-tat but switches to always steal if opponent defects twice in a row."),
        ("Random Bot", random_bot, "Chooses randomly between cooperation and defection."),
        ("Alternator", alternator, "Alternates between cooperation and defection."),
        ("Detective", detective, "Tests the opponent and exploits if no retaliation."),
        ("Generous Pavlov", generous_pavlov,
         "Starts with split. Repeats the last move if rewarded, otherwise switches. Forgives 20% of the time."),
        ("Cautious Forgiver", cautious_forgiver,
         "Cooperates unless the opponent defects more than twice in a row. Occasionally forgives."),
        ("Hopeful Bot", hopeful_bot,
         "Always starts with cooperation. Defects only if the opponent defects three times in a row."),
        ("Adaptive Generous Bot", adaptive_generous_bot,
         "Starts with 80% cooperation. Adjusts cooperation rate based on the opponent's behavior."),
        ("Persistent Bully", persistent_bully,
         "Starts by defecting. Cooperates only if the opponent retaliates three times in a row."),
        ("Sneaky Exploiter", sneaky_exploiter,
         "Alternates between split and steal. Exploits if the opponent doesn't retaliate within the first five rounds."),
        ("Aggressive Alternator", aggressive_alternator,
         "Alternates between split and steal but defects twice in a row if the opponent cooperates three times consecutively."),
        ("Learning Bot", learning_bot,
         "Learns the opponent's cooperation rate over the last 10 rounds and adjusts its strategy."),
        ("Win-Stay-Lose-Shift", win_stay_lose_shift,
         "Starts with split. Repeats the last move if rewarded, otherwise switches."),
        ("Tit-for-Two-Tats", tit_for_two_tats, "Defects only if the opponent defects twice in a row."),
        ("Random Forgiver", random_forgiver,
         "Chooses randomly between split and steal but forgives defections 30% of the time."),
        ("Chaotic Bot", chaotic_bot,
         "Alternates randomly but switches to full defection if the opponent defects more than 50% of the time."),
        ("Forgiving Detective", forgiving_detective,
         "Tests the opponent: split, steal, split, split. Forgives defections 20% of the time."),
        ("Adaptive Grudger", adaptive_grudger,
         "Cooperates until the opponent defects twice in a row. Occasionally forgives."),
        ("Probing Tit-for-Tat", probing_tit_for_tat,
         "Starts with cooperation but occasionally probes the opponent by defecting once every 10 rounds."),
    ]

    # Initialize scores for each bot
    bot_scores = {name: 0 for name, _, _ in bots}

    rounds = random.randint(150, 250)  # Randomly choose rounds between 150 and 250

    # Simulate all pairwise matchups
    for i, (name1, bot1, _) in enumerate(bots):
        for j, (name2, bot2, _) in enumerate(bots):
            if i <= j:  # Avoid duplicate matchups and allow self-matchups
                # 50% chance of playing against itself
                if i == j or random.random() < 0.5:
                    opponent_bot = bot1
                    opponent_name = name1
                else:
                    opponent_bot = bot2
                    opponent_name = name2

                # Simulate the game
                score1, score2 = simulate_game(bot1, opponent_bot, rounds)
                bot_scores[name1] += score1
                bot_scores[opponent_name] += score2

    # Print results in descending order of scores
    print(f"Simulation Results ({rounds} rounds):")
    # Sort the bots by score in descending order
    sorted_bots = sorted(bot_scores.items(), key=lambda x: x[1], reverse=True)

    for name, score in sorted_bots:
        # Retrieve the strategy description from the original list
        strategy_desc = next(desc for n, _, desc in bots if n == name)
        print(f"{name} | {strategy_desc} | Total Score: {score}")

if __name__ == "__main__":
    main()
