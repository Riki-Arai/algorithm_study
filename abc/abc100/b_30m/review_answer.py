# 例えばD=0、N=100の時は答えは100ではなくて101になる引っ掛けがあるので注意
# しかし愚直に数え上げをすればその問題も自動的に回避できる

import sys; sys.setrecursionlimit(10**7)

D, N = map(int, input().split()) # 取得例：1 2

res_list = []
for i in range(1, 10**7+1):
    count = 0
    ii = i
    while ii%100 == 0:
        ii //= 100
        count += 1
        if count > 2:
            break

    if count == D:
        res_list.append(i)

print(res_list[N-1])