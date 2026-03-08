input = open("input.txt").read().strip().split(',')
print(input)

def solvePuzzle1(input):
    sum = 0
    for ranges in input:
        start, end = ranges.split('-')
        start = int(start)
        end = int(end)+1
        for i in range(start, end):
            midpoint = len(str(i))//2
            left = str(i)[:midpoint]
            right = str(i)[midpoint:]
            if left==right:
                sum+=i
    print(sum)

def checkInvalid(num):
    numStr = str(num)
    m = len(numStr)//2
    for i in range(m+1):
        pattern = numStr[:i]
        if pattern*numStr.count(pattern) == numStr:
            return True
    return False

def solvePuzzle2(input):
    sum = 0
    for ranges in input:
        start, end = map(int, ranges.split('-'))
        end = end
        for i in range(start, end+1):
            if checkInvalid(i):
                sum+=i
    print(sum)

solvePuzzle1(input)
solvePuzzle2(input)