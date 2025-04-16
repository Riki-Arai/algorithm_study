import math

A, M, L, R = map(int, input().split())

if A == L or A == R:
    print((R-L) // M + 1)
elif A < L:
    print(math.ceil((R - (L+(M-(L-A)%M)))/ M))
elif L < A < R:
    print(math.ceil((A-L) // M + (R-A) / M))
elif R < A:
    print(math.ceil((L - (R+(M-(R-A)%M)))/ M))