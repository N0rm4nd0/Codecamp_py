import random

def simulate_draws(num_experiments):
    count_success = 0

    for _ in range(num_experiments):
        hat = ['blue'] * 5 + ['red'] * 4 + ['green'] * 2
        draw = random.sample(hat, 4)  # Randomly select 4 balls without replacement

        red_count = draw.count('red')
        green_count = draw.count('green')

        if red_count >= 1 and green_count >= 2:
            count_success += 1

    probability = count_success / num_experiments
    return probability

num_experiments = 100000  # Number of experiments to perform
probability = simulate_draws(num_experiments)

print(f"Estimated probability: {probability}")