N, X = list(map(int, input().split()))
S = input()

for s in S:
    if s == "o":
        X += 1
    elif s == "x":
        X -= 1
        X = max(0, X)

print(X)
