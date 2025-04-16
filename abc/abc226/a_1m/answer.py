import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て


X = float(input())
def remove_exponent(d):
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
# 1E0：2025.563->2026、1E1：2025.563->2030、1E2E：2025.563->2000
print(remove_exponent(Decimal(X).quantize(Decimal(f'1E0'), ROUND_HALF_UP)))
