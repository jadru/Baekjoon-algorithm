import sys

a = int(sys.stdin.readline())
b = sorted(list(map(int, sys.stdin.readline().split())))
c = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
for i in d:
    answer = 0
    left = 0
    right = a-1
    while left <= right:
        mid = (left + right) // 2
        if b[mid] == i:
            answer = 1
            break
        elif b[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    print(answer)