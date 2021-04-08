import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    for j in arr:
        if j is not i:
            for x in arr:
                if x is not j and x is not i:
                    if i + j + x > ans and i + j + x <= m:
                        ans = i + j + x
print(ans)
