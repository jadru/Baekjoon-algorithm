# import sys
# input = sys.stdin.readline

N = int(input())
arr = list()
for i in range(N):
    a, b = map(str, input().split())
    arr.append([int(a), b])
arr.sort(key=lambda x: x[0])
for i in arr:
    print(i[0], i[1])