while True:
    try:
        s = input()
        try:
            a, b = s.split(' ')
            print( int(a) + int(b) )
        except:
            continue
    except:
        break
