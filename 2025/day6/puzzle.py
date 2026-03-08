input = open("input.txt").read().splitlines()
total = 0
l1 = input[0].split()
l2 = input[1].split()
l3 = input[2].split()
l4 = input[3].split()
op = input[4].split()
w = len(op)
for i in range(w):
    a = int(l1[i])
    b = int(l2[i])
    c = int(l3[i])
    d = int(l4[i])
    if op[i] == "+":
        total += a + b + c + d
    elif op[i] == "*":
        total += a * b * c * d
print(total)

#puzzle 2

ops = input[-1]
grid = input[:-1]

total = 0
width = len(grid[0])
nums = []

for c, op in enumerate(ops):
    if op in "+*":
        nums.append(op)
    col = "".join(row[c] for row in grid)
    nums.append(col)

res = 0
nums2 = []
op = ""

for ele in nums:
    if ele.strip() != "":
        nums2.append(ele.strip())
nums = nums2

for ele in nums:
    if ele in "+*":
        total+=res
        op = ele
        if op == "+":
            res = 0
        elif op == "*":
            res = 1
        continue
    if ele.isdigit(): 
        if op == "+":
            res += int(ele)
        elif op == "*":
            res *= int(ele)
total+=res
    
print(total)
