from collections import Counter

# with sequence of items
myCounter = Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

print(myCounter.keys())
