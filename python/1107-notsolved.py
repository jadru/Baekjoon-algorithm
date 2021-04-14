import sys

ch = sys.stdin.readline()
brkn_btn_cnt = int(sys.stdin.readline())
brkn_btn_input = list(map(int, sys.stdin.readline().split()))
brkn_btn = list(range(0, 10))
for i in range(0, 10):
    for j in brkn_btn_input:
        if i == j:
            brkn_btn.remove(i)
is_low = list()
is_high = list()
for i in range(1, len(ch)):
    is_low.append(0)
    is_high.append(0)

def findright(location):
    for i in range(location, len(ch) - 1):
        lowest = 10
        for brkn_btn_num in brkn_btn:
            if lowest > brkn_btn_num:
                lowest = brkn_btn_num
        is_high[i] = lowest

def findleft(location):
    for i in range(location, len(ch) - 1):
        highest = 0
        for brkn_btn_num in brkn_btn:
            if highest < brkn_btn_num:
                highest = brkn_btn_num
        is_low[i] = highest

for i in range(len(ch) - 1):
    b = False
    ch_num = int(ch[i])
    min = 0
    max = 10
    for brkn_btn_num in brkn_btn:
        if ch_num == brkn_btn_num:
            is_low[i] = ch_num
            is_high[i] = ch_num
            b = True
            break
        elif ch_num > brkn_btn_num:
            if min < brkn_btn_num:
                min = brkn_btn_num
        else:
            if max > brkn_btn_num:
                max = brkn_btn_num
    if b:
        continue
    if i == len(ch) - 2 and abs(int(''.join(map(str, is_low))) - int(''.join(map(str, is_high)))) < 10: # 두 변수의 차가 10 이하일 경우
        is_low[i] = min
        is_high[i] = max
        break
    findright(i)
    findleft(i)
answer = 0
cnt = 0
if abs(int(ch) - 100) < abs(int(''.join(map(str, is_low))) - int(ch)) or abs(int(ch) - 100) < abs(int(''.join(map(str, is_high))) - int(ch)):
    print(abs(int(ch) - 100))
else:
    if abs(int(''.join(map(str, is_low))) - int(ch)) > abs(int(''.join(map(str, is_high))) - int(ch)):
        answer = int(''.join(map(str, is_high)))
        cnt = len(ch) - 1 + abs(int(''.join(map(str, is_high))) - int(ch))
    else:
        answer = int(''.join(map(str, is_low)))
        cnt = len(ch) - 1 + abs(int(''.join(map(str, is_low))) - int(ch))
    print(cnt)