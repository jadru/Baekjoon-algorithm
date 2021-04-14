import sys
input = sys.stdin.readline

# 입력 부분
channel = int(input())
brkn_btn_cnt = int(input())
if brkn_btn_cnt != 0:
    brkn_btn_input = list(map(int, input().split()))
brkn_btn = list(range(10))

# 정의 및 버튼 정의
min = 500000
if brkn_btn_cnt != 0:
    for i in range(10):
        for j in brkn_btn_input:
            if i is j:
                brkn_btn.remove(i)

# 있는 버튼들로 최솟값 계산
if channel <= 10: howmanycal = 20
else: howmanycal = channel * 2
for i in range(howmanycal): # channel의 2배 숫자를 구함
    isnot = False
    length = 0 # 문자열 길이
    for j in str(i): # i의 숫자를 하나씩 대조
        if isnot: break
        temp = length + 1
        for x in brkn_btn:
            if int(j) == x:
                length += 1
        if temp != length: isnot = True
    if isnot: continue
    if abs(channel - i) + len(str(i)) < min:
        min = abs(channel - i) + len(str(i))

# 출력 부분
if channel == 100:
    print(0)
elif brkn_btn_cnt == 10 or abs(channel-100) < min:
    print(abs(channel-100))
else:
    print(min)