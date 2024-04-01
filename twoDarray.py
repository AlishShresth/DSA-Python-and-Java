T = [[1, 2, 3], [3, 4, 5], [4, 5]]
T.insert(3, [4, 5, 6, 7])
for r in T:
    for c in r:
        print(c, end=" ")
    print()
