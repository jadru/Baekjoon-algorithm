import sys

input = sys.stdin.readline


def getRoom(H, W, T):
    if T - H > 0:
        getRoom(H, W + 1, T - H)
    else:
        if W < 10: print(str(T) + '0' + str(W))
        else: print(str(T) + str(W))


N = int(input())
for i in range(N):
    H, W, T = map(int, input().split())
    getRoom(H, 1, T)

