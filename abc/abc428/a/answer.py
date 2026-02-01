S, A, B, X = map(int, input().split()) # 取得例：1 2

print(X//(A+B)*A*S + min(X%(A+B), A)*S)