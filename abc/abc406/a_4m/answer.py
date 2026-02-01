A, B, C, D = map(int, input().split()) # 取得例：1 2

if C < A:
    print("Yes")
elif C == A:
    if D < B:
        print("Yes")
    else:
        print("No")
else:
    print("No")