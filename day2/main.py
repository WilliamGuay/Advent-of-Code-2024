F = open("day2/input.txt").read().strip()
L = [[int(y) for y in x.split()] for x in F.split("\n")]

ans = 0

for x in L:
    for z in range(len(x)):
        
        isValid = True
        isIncreasing = False 
        i = False
        
        a = [y for y in x]
        a.pop(z)
        
        for y in range(len(a) - 1):
            if not i:
                i = True
                if a[y] < a[y + 1]:
                    isIncreasing = True
            
            if a[y] < a[y + 1] and not isIncreasing:
                isValid = False
                break
            if a[y] > a[y + 1] and isIncreasing:
                isValid = False
                break
            if not 1 <= abs(a[y] - a[y + 1]) or not 3 >= abs(a[y] - a[y + 1]):
                isValid = False
                break
            
        if isValid:
            print(x, a, x[z])
            break
        
    if isValid:
        ans += 1
            
print(ans)