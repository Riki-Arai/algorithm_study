L, R = map(int, input().split())
S = input().strip()
print(S[:L-1] + S[L-1:R][::-1] + S[R:])