import os
import re

def read_puzzle():
    puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2023/day2/puzzle.txt")
    with open(puzzle_file, 'r') as file:
        return [line.strip() for line in file]

def day_two_part_one():
    cubes = {"red": 12, "green": 13, "blue": 14}
    pattern = r"(\d+) (red|blue|green)"
    games = read_puzzle()
    valid_games = 0
    for game_number, game in enumerate(games):
        results = re.findall(pattern, game)
        if all(cubes[result[1]] >= int(result[0]) for result in results):
            valid_games += game_number + 1
    print(valid_games)

day_two_part_one()
