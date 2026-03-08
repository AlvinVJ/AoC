input = open("input.txt").read().strip().splitlines()

def puzzle1():
    grid = input
    h = len(grid)
    w = len(grid[0])

    start_col = grid[0].index("S")

    beams = {start_col}
    splits = 0

    for r in range(1, h):
        new_beams = set()

        for c in beams:
            if c < 0 or c >= w:
                continue

            if grid[r][c] == "^":
                splits += 1
                new_beams.add(c - 1)
                new_beams.add(c + 1)
            else:
                new_beams.add(c)

        beams = new_beams

    print(splits)

def puzzle2():
    grid = input
    h = len(grid)
    w = len(grid[0])

    start_col = grid[0].index("S")

    beams = {start_col: 1}

    for r in range(1, h):
        new = {}

        for c, count in beams.items():
            if c < 0 or c >= w:
                continue

            if grid[r][c] == "^":
                new[c-1] = new.get(c-1, 0) + count
                new[c+1] = new.get(c+1, 0) + count
            else:
                new[c] = new.get(c, 0) + count

        beams = new

    print(sum(beams.values()))

puzzle1()
puzzle2()