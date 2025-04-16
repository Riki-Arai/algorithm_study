import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

X, K = map(int, input().split())

for i in range(K):
    def remove_exponent(d):
        return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
    # 1E0：2025.563->2026、1E1：2025.563->2030、1E2E：2025.563->2000
    X = remove_exponent(Decimal(X).quantize(Decimal(f'1E{i+1}'), ROUND_HALF_UP))

print(X)

## second
#X, K = map(int, input().split())
#
#for i in range(K):
#    y = (X // (10 ** (i + 1))) * (10 ** (i + 1))
#    yy = (X // (10 ** (i + 1)) + 1) * (10 ** (i + 1))
#    if abs(y - X) < abs(yy - X):
#        X = y
#    elif abs(y - X) >= abs(yy - X):
#        X = yy
#
#print(X)

## first
#X, K = map(int, input().split())
#
#for i in range(K):
#    j = (i + 1)
#    y_1 = 10 ** j * (X // (10 ** j))
#    y_2 = 10 ** j * (X // (10 ** j) + 1)
#    if abs(y_1 - X) > abs(y_2 - X):
#        X = y_2
#    elif abs(y_1 - X) < abs(y_2 - X):
#        X = y_1
#    else:
#        X = max(y_1, y_2)
#
#print(X)