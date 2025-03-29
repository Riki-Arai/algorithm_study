S, T, X = map(int, input().split())

if S < T:
    if S <= X and T > X:
        print("Yes")
    else:
        print("No")
else:
    if (X >= S) or (T > X):
        print("Yes")
    else:
        print("No")