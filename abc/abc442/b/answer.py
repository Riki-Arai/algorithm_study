import sys; sys.setrecursionlimit(10**7)

Q = int(input()) # 数値：1

res = 0
play_flag = False
for _ in range(Q) :
    A = int(input()) # 数値：1
    if A == 1:
        res += 1
        if play_flag and res >= 3:
            print("Yes")
        else:
            print("No")
    elif A == 2:
        res = max(res-1, 0)
        if play_flag and res >= 3:
            print("Yes")
        else:
            print("No")
    else:
        if play_flag:
            play_flag = False
        else:
            play_flag = True
        if play_flag and res >= 3:
            print("Yes")
        else:
            print("No")