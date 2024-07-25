import numpy as np
from picturebooks import jaccard_index

num_objects = 8
dataset_size = 50
num_monte_carlo_iterations = 20
all_objects = range(num_objects)

totals = []
for i in range(num_monte_carlo_iterations):
    total_score = 0
    for j in range(dataset_size):
        objects = list(np.random.choice(all_objects, np.random.randint(4,len(all_objects)+1)))
        correct = set(np.random.choice(objects, np.random.randint(1,len(objects))))
        random_guess = set(np.random.choice(objects, np.random.randint(1,len(objects))))

        total_score += jaccard_index(correct, random_guess)
    totals.append(total_score)

print(f"Average random jaccard score was {np.mean(totals):.4f} with standard deviation {np.std(totals):.4f}.")

totals = []
for i in range(num_monte_carlo_iterations):
    total_score = 0
    for j in range(dataset_size):
        objects = list(np.random.choice(all_objects, np.random.randint(4,len(all_objects)+1)))
        correct = set(np.random.choice(objects, np.random.randint(1,len(objects))))
        random_guess = set(np.random.choice(objects, np.random.randint(1,len(objects))))

        total_score += 1 if correct == random_guess else 0
    totals.append(total_score)

print(f"Average random absolute score was {np.mean(totals):.4f} with standard deviation {np.std(totals):.4f}.")

