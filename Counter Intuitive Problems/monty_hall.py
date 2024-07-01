import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

switch_wins = 0
stay_wins = 0
trials = 10000

for i in range(trials):
    winning_door = random.randint(0, 2)

    contestant_door = random.randint(0, 2)

    monty_opens = random.randint(0, 2)
    while monty_opens == winning_door or monty_opens == contestant_door:
        monty_opens = random.randint(0, 2)

    switch_door = 3 - contestant_door - monty_opens

    if switch_door == winning_door:
        switch_wins += 1

    if contestant_door == winning_door:
        stay_wins += 1

switch_win_percentage = switch_wins / trials * 100
stay_win_percentage = stay_wins / trials * 100

fig, ax = plt.subplots()
ax.bar(['Switch Wins','Stay Wins'], [switch_wins, stay_wins], color=['green', 'red'])
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('Number of Wins/Losses')
ax.set_title('Monty Hall Simulation Results')
plt.show()

print(f'Switch Win Percentage: {switch_win_percentage:.2f}%')
print(f'Stay Win Percentage: {stay_win_percentage:.2f}%')