import os
import re

PUZZLE_FILE = os.path.join(os.environ.get("BASE_DIR"), "2023/day1/puzzle.txt")

def read_puzzle():
    with open(PUZZLE_FILE, 'r') as file:
        return [line.strip() for line in file]

# part 1
def day_one_part_one():
    data = read_puzzle()
    cal_values = []
    for line in data:
        for i in line:
            try:
                first_num = int(i)
                break
            except ValueError:
                continue
        for i in reversed(line):
            try:
                last_num = int(i)
                break
            except ValueError:
                continue

        cal_values.append(int(f"{first_num}{last_num}"))
    print(cal_values)

