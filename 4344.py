import sys
input = sys.stdin.readline

a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    sum = 0
    for j in range(1, b[0] + 1):
        sum += b[j]
    avg = float(sum / b[0])
    result = 0
    for j in range(1, b[0] + 1):
        if b[j] > avg:
            result += 1
    result = float(result / b[0] * 100.000)
    print('%.3f' % round(result, 3), '%', sep='')