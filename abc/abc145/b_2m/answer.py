N = int(input()) # 数値：1
S = input().strip() # 取得例："A"

if S[:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")