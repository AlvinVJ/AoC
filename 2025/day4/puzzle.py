input = open("day4/input.txt").read().strip().splitlines()

neighbors = [
    [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]
]


def checkNeighbors(r, c):
    count = 0
    for [dx, dy] in neighbors:
        x = c + dx
        y = r + dy
        if x < 0 or x >= len(input[r]) or y < 0 or y >= len(input):
            continue
        if input[y][x] == "@":
            count += 1
    return count


def solvePuzzle1(input):
    sum = 0
    for rowIdx in range(len(input)):
        for colIdx in range(len(input[rowIdx])):
            if input[rowIdx][colIdx] == "@":
                neighboringRolls = checkNeighbors(rowIdx, colIdx)
                if neighboringRolls < 4:
                    sum += 1
    print(sum)


solvePuzzle1(input)


