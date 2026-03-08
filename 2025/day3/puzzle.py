input = open("input.txt").read().strip().splitlines()


def findLargestInRange(input, i, j):
    largest = i
    for k in range(i, j+1):
        if input[k] > input[largest]:
            largest = k
    return largest

def solvePuzzle1(input):
    joltagesum = 0
    for line in input:
        l = findLargestInRange(line, 0, len(line)-2)
        r = findLargestInRange(line, l+1, len(line)-1)
        joltagesum += int(line[l]+line[r])      
    print(joltagesum)  


def solvePuzzle2(input):
    joltagesum = 0
    for line in input:
        leftLimit = 0
        rightLimit = len(line) - 12
        num = 0
        for _ in range(12):
            n = findLargestInRange(line, leftLimit, rightLimit)
            num = num*10 + int(line[n])
            leftLimit = n + 1
            rightLimit = rightLimit + 1
        joltagesum += num
    print(joltagesum)



solvePuzzle1(input)
solvePuzzle2(input) 