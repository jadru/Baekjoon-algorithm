import sys
input = sys.stdin.readline

a = int(input())
min = 1000000
for i in range(a):
    find = i
    for j in str(i):
        find += int(j)
    if find == a and i < min:
        min = i
if min == 1000000:
    min = 0
print(min)