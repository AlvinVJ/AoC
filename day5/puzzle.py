input = open("input.txt").read().strip().split('\n\n')
ranges = input[0].splitlines()
productIds = list(map(int, input[1].splitlines()))

unmergedRanges = []
mergedRanges = []
for r in ranges:
    a, b = r.split('-')
    unmergedRanges.append((int(a), int(b)))
unmergedRanges.sort()

l = 0
r = 1
while r < len(unmergedRanges):
    if unmergedRanges[l][1] >= unmergedRanges[r][0]:
        unmergedRanges[l] = (unmergedRanges[l][0], max(unmergedRanges[l][1], unmergedRanges[r][1]))
    else:
        mergedRanges.append(unmergedRanges[l])
        l = r
    r += 1
mergedRanges.append(unmergedRanges[l])

count = 0

for p in productIds:
    for r in mergedRanges:
        if r[0] <= p <= r[1]:
            count += 1
            break
print(count)


#part 2

total = 0
for l, r in mergedRanges:
    total += r-l+1
print(total)