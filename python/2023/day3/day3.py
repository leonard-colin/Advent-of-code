import os
import re


def read_puzzle():
    puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2023/day3/puzzle.txt")
    with open(puzzle_file, "r") as file:
        return [line.strip() for line in file]


def is_symbol(chars_list):
    return any(char != "." and not char.isdigit() for char in chars_list)


def day_three_part_one():
    schema = read_puzzle()
    number_pattern = r"\d+"
    sum_part_numbers = 0
    for line_index, line in enumerate(schema):
        results = re.finditer(number_pattern, line)
        for number in results:
            if line_index == 0:
                if number.start() == 0 and is_symbol(
                    schema[line_index][: number.end() + 1]
                    + schema[line_index + 1][: number.end() + 1]
                ):
                    sum_part_numbers += int(number.group())
                elif number.end() == len(line) and is_symbol(
                    schema[line_index][number.start() - 1 :]
                    + schema[line_index + 1][number.start() - 1 :]
                ):
                    sum_part_numbers += int(number.group())
                elif is_symbol(
                    schema[line_index][number.start() - 1 : number.end() + 1]
                    + schema[line_index + 1][number.start() - 1 : number.end() + 1]
                ):
                    sum_part_numbers += int(number.group())
            elif line_index == len(schema) - 1:
                if number.start() == 0 and is_symbol(
                    schema[line_index][: number.end() + 1]
                    + schema[line_index - 1][: number.end() + 1]
                ):
                    sum_part_numbers += int(number.group())
                elif number.end() == len(line) and is_symbol(
                    schema[line_index][number.start() - 1 :]
                    + schema[line_index - 1][number.start() - 1 :]
                ):
                    sum_part_numbers += int(number.group())
                elif is_symbol(
                    schema[line_index][number.start() - 1 : number.end() + 1]
                    + schema[line_index - 1][number.start() - 1 : number.end() + 1]
                ):
                    sum_part_numbers += int(number.group())
            elif number.start() == 0 and is_symbol(
                schema[line_index][: number.end() + 1]
                + schema[line_index - 1][: number.end() + 1]
                + schema[line_index + 1][: number.end() + 1]
            ):
                sum_part_numbers += int(number.group())
            elif number.end() == len(line) and is_symbol(
                schema[line_index][number.start() - 1 :]
                + schema[line_index - 1][number.start() - 1 :]
                + schema[line_index + 1][number.start() - 1 :]
            ):
                sum_part_numbers += int(number.group())
            elif is_symbol(
                schema[line_index][number.start() - 1 : number.end() + 1]
                + schema[line_index - 1][number.start() - 1 : number.end() + 1]
                + schema[line_index + 1][number.start() - 1 : number.end() + 1]
            ):
                sum_part_numbers += int(number.group())

    print(sum_part_numbers)


day_three_part_one()
