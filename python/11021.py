import sys
input = sys.stdin.readline
a = int(input())
for i in range(1, a+1):
    a, b = map(int, input().split())
    print("Case #"+ str(i) + ": " + str(a + b))