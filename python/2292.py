import sys
input = sys.stdin.readline

a = int(input())
sum = 1; i = 1
while True:
    if sum >= a:
        print(i)
        break
    sum += 6 * i
    i += 1