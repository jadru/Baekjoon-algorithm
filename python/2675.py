while 1:
    try:
        st = input()
        try:
            a, b = st.split(' ')
        except:
             continue
        for i in b:
            for j in range(0, int(a)):
                print(i, end='')
        print('\n', end='')
    except:
        break
