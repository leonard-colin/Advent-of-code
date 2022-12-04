import os

puzzle_file = os.path.join(os.environ.get("BASE_DIR"), "2022/day2/puzzle.txt")

with open(puzzle_file) as file:
    data = [line.strip() for line in file]
    guide = [i.split(" ") for i in data]

opponent = {
    "A": 1,
    "B": 2,
    "C": 3,
}

player = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

player_score = 0

for opponent_move, player_move in guide:
    if (
        opponent_move == "A" and player_move == "X"
        or opponent_move == "B" and player_move == "Y"
        or opponent_move == "C" and player_move == "Z"
    ):
        player_score += (player.get(player_move) + 3)
    elif (
        opponent_move == "A" and player_move == "Y" 
        or opponent_move == "B" and player_move == "Z" 
        or opponent_move == "C" and player_move == "X"
    ):
        player_score += (player.get(player_move) + 6)
    else:
        player_score += player.get(player_move)
    

print(player_score)


