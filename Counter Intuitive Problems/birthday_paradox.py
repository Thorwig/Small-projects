import random

def birthday_simulation(trials, group_size):
    success_count = 0
    
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            success_count += 1
    
    probability = success_count / trials
    return probability

trials = 10000
group_size = 41
probability = birthday_simulation(trials, group_size)

print(f"Probability of at least two people sharing a birthday in a group of {group_size}: {probability*100:.2f}%")
