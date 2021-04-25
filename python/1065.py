a = int(input())
sum = 0
for i in range(1, a+1):
    p = 10; n = 10
    isit = True
    for j in str(i):
        if p == 10: p = int(j) # 첫 수일 경우
        elif n == 10:  n = int(j) - p; p = int(j) # 두번쨰 수일 경우
        elif p + n == int(j): p = int(j)
        else: isit = False; break
    if not isit: continue
    else: sum += 1
print(sum)