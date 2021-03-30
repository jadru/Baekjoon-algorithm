from collections import deque
import sys

N = int(sys.stdin.readline())
l = deque(range(1, N+1))
while len(l) > 1:
    l.popleft()
    if len(l) == 1:
        break
    l.append(l.popleft())
print(l[0])
