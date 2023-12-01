import os
from string import ascii_lowercase, ascii_uppercase
from itertools import zip_longest

puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2022/day3/puzzle.txt")

with open(puzzle_file) as file:
    data = [line.strip() for line in file]

rucksacks = data

PRIORITY_LEVEL = f'{ascii_lowercase}{ascii_uppercase}'

# Part One
# sum_priorities = 0
# for items in rucksacks:
#     half = len(items) // 2
#     first_compartment = items[:half]
#     second_compartment = items[half:]

#     if any((match := item) in second_compartment for item in first_compartment):
#         sum_priorities += (PRIORITY_LEVEL.index(match) + 1)
# print(sum_priorities)

# part two
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

sum_priorities = 0

# for items in rucksacks:
groups = list(grouper(rucksacks, 3, incomplete="ignore"))
for group in groups:
    first, second, third = group[0], group[1], group[2]
    if any((match := item) in second for item in first):
        if match in third:
            sum_priorities += PRIORITY_LEVEL.index(match)
print(sum_priorities)
    
# print(common_letter)