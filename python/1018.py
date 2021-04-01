a, b = map(int, input().split())

line = list()
for i in range(0, a):
    line.append(input())
min = 32
for x in range(0, a - 7):
        for y in range (0, b - 7):
            cnt1 = 0
            cnt2 = 0
            for i in range(x, x + 8):
                if i % 2 == 0:
                    find1 = 'W'
                    find2 = 'B'
                else:
                    find1 = 'B'
                    find2 = 'W'
                for j in range(y, y + 8):
                    if not line[i][j] == find1:
                        cnt1 += 1
                    if not line[i][j] == find2:
                        cnt2 += 1
                    if find1 == 'W':
                        find1 = 'B'
                    else:
                        find1 = 'W'
                    if find2 == 'B':
                        find2 = 'W'
                    else:
                        find2 = 'B'
            if cnt1 < min:
                min = cnt1
            elif cnt2 < min:
                min = cnt2
print(min)
