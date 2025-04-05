A, B, C = list(map(int, input().split()))

if B < C:
    if not B < A < C:
        print("Yes")
    else:
        print("No")
else:
    if not (B < A or A < C):
        print("Yes")
    else:
        print("No")