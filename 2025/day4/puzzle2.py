from collections import deque

grid = [list(row) for row in open("input.txt").read().splitlines()]
R = len(grid)
C = len(grid[0])

dirs = [
    (0,1),(0,-1),(1,0),(-1,0),
    (1,1),(1,-1),(-1,1),(-1,-1)
]

degrees = [[0] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if grid[rr][cc] == '@':
                        degrees[rr][cc] += 1

queue = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == '@' and degrees[r][c] < 4:
            queue.append((r, c))

removed = 0

while queue:
    r, c = queue.popleft()
    if grid[r][c]!= '@':
        continue
    grid[r][c] = '.'
    removed +=1

    for dr, dy in dirs:
        rr, cc = r + dr, c + dy
        if 0 <= rr < R and 0 <= cc < C:
            if grid[rr][cc] == '@':
                degrees[rr][cc] -= 1
                if degrees[rr][cc] == 3:
                    queue.append((rr, cc))

print(removed)