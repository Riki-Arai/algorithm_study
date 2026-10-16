A, B, N = map(int, input().split()) # 取得例：1 2

if B-1 > N:
    print(A*N//B)
else:
    print(A*(B-1)//B)