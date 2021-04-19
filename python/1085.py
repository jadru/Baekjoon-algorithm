import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
min = 1000
if x < min:
    min = x
if w - x < min:
    min = w - x
if y < min:
    min = y
if h - y < min:
    min = h - y
print(min)