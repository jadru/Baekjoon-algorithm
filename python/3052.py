a = []
for i in range(0, 10):
    a.append(int(input()))
b = []
for i in a:
    b.append(i % 42)
b = list(set(b))
print(len(b))