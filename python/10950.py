while 1:
    try:
        try:
            a, b = map(int, input().split(' '))
            print( a+b )
        except:
            continue
    except:
        break
