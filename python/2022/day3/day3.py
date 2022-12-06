import os
from string import ascii_lowercase, ascii_uppercase

puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2022/day3/puzzle.txt")

with open(puzzle_file) as file:
    data = [line.strip() for line in file]

rucksacks = data

PRIORITY_LEVEL = f'{ascii_lowercase}{ascii_uppercase}'

# Part One
sum_priorities = 0
for items in rucksacks:
    half = len(items) // 2
    first_compartment = items[:half]
    second_compartment = items[half:]

    if any((match := item) in second_compartment for item in first_compartment):
        sum_priorities += (PRIORITY_LEVEL.index(match) + 1)
print(sum_priorities)