F = open("day1/input.txt").read().strip()
L = F.split("\n")

l1 = []
l2 = []

for c in L:
    l1.append(int(c.split()[0]))
    l2.append(int(c.split()[1]))
    
l1.sort()
l2.sort()

ans = 0

for x in range(len(l1)):
    ans += abs(l1[x] - l2[x])
    
print(ans)

ans2 = 0

for x in l1:
    nb = 0
    for y in l2:
        if x == y:
            nb+=1
    ans2 += nb * x
    
print(ans2)
