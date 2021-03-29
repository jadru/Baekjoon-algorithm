a, b = map(str, input().split())
a = a[2::-1]
b = b[2::-1]
if int(a) > int(b):
    print(a)
else:
    print(b)