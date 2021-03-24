a = int(input())
b = int(input())
a = a - a % 100
for i in range(a, a+99):
    if i % b == 0:
        i = i % 100
        if i < 10:
            print('0' + str(i))
        else:
            print(i)
        break