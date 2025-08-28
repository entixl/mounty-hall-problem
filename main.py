import random

def monty_hall_sim(trials=10000, switch=True):
    wins = 0
    for _ in range(trials):
        doors = [0, 0, 1]  # 0 = goat, 1 = car
        random.shuffle(doors)

        choice = random.randint(0, 2)  # initial choice
        # Host opens a goat door
        available_doors = [i for i in range(3) if i != choice and doors[i] == 0]
        host_opens = random.choice(available_doors)

        if switch:
            # Switch to the remaining unopened door
            choice = next(i for i in range(3) if i != choice and i != host_opens)

        if doors[choice] == 1:
            wins += 1

    return round(wins/trials * 100 , 1)
# Simulate
stay_win_rate = monty_hall_sim(trials=100000, switch=False)
switch_win_rate = monty_hall_sim(trials=100000, switch=True)

print("Winning rate if you stay:", stay_win_rate)
print("Winning rate if you switch:", switch_win_rate)
