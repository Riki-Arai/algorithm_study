A, B, C, X, Y = list(map(int, input().split()))

res = 0
if A + B > 2 * C:
    res += 2 * C * min(X, Y)
    if X > Y:
        rem_num = X - min(X, Y)
        if 2 * C * rem_num > A * rem_num:
            res += A * rem_num
        else:
            res += 2 * C * rem_num
    elif X < Y:
        rem_num = Y - min(X, Y)
        if 2 * C * rem_num > B * rem_num:
            res += B * rem_num
        else:
            res += 2 * C * rem_num
else:
    res += A * X + B * Y

print(res)
