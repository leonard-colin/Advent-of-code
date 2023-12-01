import os

puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2023/day1/puzzle.txt")

with open(puzzle_file, 'r') as file:
    data = [line.strip() for line in file]

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

print(sum(cal_values))
