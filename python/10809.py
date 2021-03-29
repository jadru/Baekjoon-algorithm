a = list(input())

for i in range(97, 123):
    if a.count(chr(i)) == 0:
        print(-1, end=' ')
    else:
        print(a.index(chr(i)), end=' ')