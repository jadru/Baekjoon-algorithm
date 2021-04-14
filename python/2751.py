import sys
input = sys.stdin.readline

a = int(input())
arr = [ 0 ] * 2000001
for i in range(a):
    k = int(input())
    arr[k + 1000000] = 1
for i in range(2000001):
    if arr[i] == 1: print(i - 1000000)