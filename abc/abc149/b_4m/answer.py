A, B, K = map(int, input().split()) # 取得例：1 2

if A >= K:
    print(A-K, B)
else:
    K -= A
    print(0, max(B-K, 0))