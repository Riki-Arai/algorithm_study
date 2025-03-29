N, T, A = list(map(int, input().split()))

if T > A:
    if A + (N - (T + A)) > T:
        print("No")
    else:
        print("Yes")
elif T < A:
    if T + (N - (T + A)) > A:
        print("No")
    else:
        print("Yes")
else:
    print("No")