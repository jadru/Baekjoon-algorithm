import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    b = int(input())
    lst = list(map(int, input().split()))
    sum = 0
    for j in lst: sum+= j
    print(float(sum / b))