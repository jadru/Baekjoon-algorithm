cnt = int(input())
s = map(int, input().split(' '))
max = -1000000
min = 1000000
for i in s:
    if min > i:
        min = i
    if max < i:
        max = i
print(min, max)
