A, B, C, D = map(int, input().split())

if A > C:
    print("Aoki")
elif A == C:
    if B > D:
        print("Aoki")
    elif B == D:
        print("Takahashi")
    else:
        print("Takahashi")
elif A < C:
    print("Takahashi")