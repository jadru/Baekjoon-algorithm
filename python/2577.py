a = int(input())
b = int(input())
c = int(input())
s = str(a*b*c)
x = [0 for i in range(10)]
for i in s:
    x[int(i)]+= 1
for i in range(0, 10):
    print(x[i])