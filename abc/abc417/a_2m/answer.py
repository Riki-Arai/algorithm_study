N, A, B = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

if B > 0:
    print(S[A:-B])
else:
    print(S[A:])