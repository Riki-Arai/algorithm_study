import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"

n = len(S)
for _ in range(n+1):
    S = S[-1] + S[:-1]
    if S == T:
        print("Yes")
        exit()

print("No")