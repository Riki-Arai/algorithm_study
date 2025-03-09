H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
rows = [row for row in A if "#" in row]
cols = [col for col in zip(*rows) if "#" in col]
print(*("".join(s) for s in zip(*cols)), sep="\n")
