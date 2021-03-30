import sys

a, b = map(int, sys.stdin.readline().split())
c = set()
d = set()
for i in range(1, a):
    for j in range(1, a):
        if i * j == a:
            c.add(i)
            c.add(j)
for i in range(1, b):
    for j in range(1, b):
        if i * j == b:
            d.add(i)
            d.add(j)
max = 0
for i in c:
    for j in d:
        if i == j and i > max:
            max = i
print(max)
