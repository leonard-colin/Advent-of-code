with open("/Users/leonardcolin/code/AdventOfCode/day3/map.txt") as file:
    area = [line[0:-1] for line in file]


def number_of_trees(right_step, down_step):
    x, y = 0, 0
    trees_count = 0
    last_row = len(area) - 1
    col_modulo = len(area[0])

    while y <= last_row:
        if area[y][x] == "#":
            trees_count += 1

        x = (x + right_step) % col_modulo
        y += down_step

    return trees_count


# Part one:
print("There is " + str(number_of_trees(3, 1)) + " trees")

# Part two:
first = number_of_trees(1, 1)
second = first * number_of_trees(3, 1)
third = second * number_of_trees(5, 1)
fourth = third * number_of_trees(7, 1)
fifth = fourth * number_of_trees(1, 2)
print(fifth)
