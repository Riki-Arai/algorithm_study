import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"

if len(S)%5 == 0:
    print("Yes")
else:
    print("No")