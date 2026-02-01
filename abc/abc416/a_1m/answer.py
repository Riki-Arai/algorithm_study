N, L, R = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

if S[L-1:R].count("o") == R-L+1:
    print("Yes")
else:
    print("No")