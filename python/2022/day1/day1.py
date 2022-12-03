import os
from itertools import groupby

puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2022/day1/puzzle.txt")

with open(puzzle_file) as file:
    data = [line.strip() for line in file]
elves = [[(int(cal)) for cal in elf] for k, elf in groupby(data, lambda x: x == "") if not k]

# Part one
sum_calories_list = [sum(cal) for cal in elves]
max_calory = max(sum_calories_list)
print(max_calory)

# Part two
sum_calories_list.sort(reverse=True)
top_three = sum_calories_list[:3]
print(sum(top_three))