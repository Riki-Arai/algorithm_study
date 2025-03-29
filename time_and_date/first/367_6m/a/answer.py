A, B, C = map(int, input().split())

if B < C:
    if B > A or C < A:
        print("Yes")
    else:
        print("No")
else:
    if not (B < A or C > A):
        print("Yes")
    else:
        print("No")