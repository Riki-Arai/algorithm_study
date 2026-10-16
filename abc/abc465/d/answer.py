'''
(1) 数式だけではとっかかりが掴みにくい
(2) 問題の整理を通じて図にしてみることでアプローチに気づくことができるきっかけになる
(3) 普段から図に起こして考えてみる習慣が重要
'''
import sys; sys.setrecursionlimit(10**7)

T = int(input()) # 数値：1

for _ in range(T):
    X, Y, K = map(int, input().split()) # 取得例：1 2
    res = 0
    z = max(X, Y)
    while X != Y:
        z //= K
        if X > Y:
            X = z
            z = max(X, Y)
        else:
            Y = z
            z = max(X, Y)
        res += 1

    print(res)