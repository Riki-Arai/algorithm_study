V, T, S, D = map(int, input().split())

if V*T > D or V*S < D:
    print("Yes")
else:
    print("No")