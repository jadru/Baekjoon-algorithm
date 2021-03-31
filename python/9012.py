import sys

N = int(sys.stdin.readline())
for i in range(0, N):
    k = sys.stdin.readline()
    cnt = 0
    for j in k:
        if cnt < 0:
            break
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')
