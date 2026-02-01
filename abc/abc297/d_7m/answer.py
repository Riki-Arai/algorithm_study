A, B = map(int, input().split())

res = 0
while A != B:
    if A > B:
        if A%B == 0:
            res += (A-B)//B
            A = B
        else:
            d = A//B
            res += d
            A -= B*d
    else:
        if B%A == 0:
            res += (B-A)//A
            B = A
        else:
            d = B//A
            res += d
            B -= A*d

print(res)