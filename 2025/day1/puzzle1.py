value=50
count = 0

def doTurn(instr):
    global value
    if instr[0]=='L':
        value = value - int(instr[1:])
    else:
        value = value + int(instr[1:])

def normalize():
    global value
    value = value % 100


with open("puzzle1input.txt") as f:
    lines = f.read().splitlines()
    for instr in lines:
        doTurn(instr)
        normalize()
        print(instr, value)
        if not value:
            count+=1


print(count)
    