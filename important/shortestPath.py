import math
path = "WNEENESENNN"
x = 0
y = 0
for p in path:
    if p == 'E':
        x += 1
    elif p == 'W':
        x -= 1
    elif p == 'N':
        y += 1
    elif p == 'S':
        y -= 1
    print(y, end=" ")
print()
dis = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
print(dis)
