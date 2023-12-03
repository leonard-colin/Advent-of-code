import functools
import operator
import os
import re


def read_puzzle():
    puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2023/day2/puzzle.txt")
    with open(puzzle_file, "r") as file:
        return [line.strip() for line in file]


def day_two_part_one():
    cubes = {"red": 12, "green": 13, "blue": 14}
    pattern = r"(\d+) (red|blue|green)"
    games = read_puzzle()
    valid_games = 0
    for game_number, game in enumerate(games, 1):
        results = re.findall(pattern, game)
        if all(cubes[result[1]] >= int(result[0]) for result in results):
            valid_games += game_number
    print(valid_games)


def day_two_part_two():
    games = read_puzzle()
    # for game_number, game in enumerate(games, 1):
    games = [
        game.replace(f"Game {game_number}: ", "").replace(";", ",").split(", ")
        for game_number, game in enumerate(games, 1)
    ]
    sum_power = 0
    for game in games:
        fewest_cubes = {}
        for ball in game:
            ball = ball.split()
            if ball[1] in fewest_cubes:
                if int(fewest_cubes[ball[1]]) < int(ball[0]):
                    fewest_cubes[ball[1]] = int(ball[0])
            else:
                fewest_cubes[ball[1]] = int(ball[0])
        power = functools.reduce(operator.mul, fewest_cubes.values())
        sum_power += power

    print(sum_power)


day_two_part_one()
day_two_part_two()
