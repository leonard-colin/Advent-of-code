from itertools import combinations

target = 2020
with open("/Users/leonardcolin/code/AdventOfCode/day1/expense_list.txt") as file:
    data = [int(line) for line in file]

# part one
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if int(data[i]) + int(data[j]) == target:
            print(data[i], data[j])
            result = int(data[i]) * int(data[j])
            print(result)


# part two
for num in combinations(data, 3):
    if num[0] + num[1] + num[2] == target:
        result = num[0] * num[1] * num[2]
        print(result)
