import sys

N = int(sys.stdin.readline())
d = []
for i in range(0, N):
    s = sys.stdin.readline()
    d.append(s)
d = list(set(d))
d.sort()
d.sort(key=lambda x:len(x))
for j in d: print(j, end='')