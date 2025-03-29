X = input().rstrip("0")

if X[-1] == ".":
    print(int(X[:-1]))
else:
    print(float(X))