while 1:
    try:
        a, b = input().split(' ')
        a = int(a)
        for j in b:
            for z in range(0, a):
                print(j, end='')
    except:
        break