N, D = map(int, input().split())
S = list(input().strip())

sorted_S = S[::-1]
for _ in range(D):
    sorted_S[sorted_S.index("@")] = "."

print("".join(sorted_S[::-1]))