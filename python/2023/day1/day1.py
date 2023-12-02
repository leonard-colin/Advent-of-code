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
    print(sum(cal_values))

# part 2
def day_one_part_two():
    data = read_puzzle()
    cal_values = []
    letter_to_digit =  {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))"
    for line in data:
        first_num = re.findall(pattern, line)[0]
        last_num = re.findall(pattern, line)[-1]

        first_num = first_num if first_num.isdigit() else letter_to_digit[first_num]
        last_num = last_num if last_num.isdigit() else letter_to_digit[last_num]

        cal_values.append(int(f"{first_num}{last_num}"))

    print(sum(cal_values))

day_one_part_one()
day_one_part_two()

