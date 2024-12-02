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
    
print("Partie 1: " + str(ans))

ans2 = 0

for x in l1:
    ans2 += l2.count(x) * x
    
print("Partie 2: " + str(ans2))