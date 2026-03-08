value=50
count = 0

with open("puzzle1input.txt") as f:
    lines = f.read().splitlines()
    for instr in lines:
        fullTurns = int(instr[1:])//100
        partialTurns = int(instr[1:])%100
        count+=fullTurns
        if instr[0]=='L':
            if value<partialTurns:
                count+=1
            value = (value - partialTurns) % 100
        else:
            if value+partialTurns>=100:
                count+=1
            value = (value + partialTurns) % 100

print(count)
    