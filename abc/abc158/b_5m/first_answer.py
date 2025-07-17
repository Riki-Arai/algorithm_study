N, A, B = map(int, input().split()) # 取得例：1 2

print(N//(A+B)*A + min(A, (N%(A+B))))