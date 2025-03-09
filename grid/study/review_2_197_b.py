H, W, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
S = [list(input()) for _ in range(H)]
row = "".join(S[X]) + "#"
col = "".join(list(zip(*S))[Y]) + "#"

ans = -1
ans += row.find("#", Y) - row.rfind("#", 0, Y) - 1
ans += col.find("#", X) - col.rfind("#", 0, X) - 1
print(ans)
