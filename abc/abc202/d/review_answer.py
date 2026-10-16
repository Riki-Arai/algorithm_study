import sys, math
sys.setrecursionlimit(10**7)

A, B, K = map(int, input().split())

a, b = A, B
res_list = []
k = 1
for _ in range(A+B):
    if a == 0:
        res_list.append("b")
        continue
    if b == 0:
        res_list.append("a")
        continue

    a_k = math.factorial(a+b-1) // (math.factorial(a-1) * math.factorial(b))
    # aを選択した時にパターン数がK未満だと、K番目のパターンに辿り着かないないので、その時はbを選択していく
    if K > a_k:
        # bを選択した時点でaを選択した時のパターン分だけKの数を削ることができる
        K -= a_k
        b -= 1
        res_list.append("b")
    else:
        a -= 1
        res_list.append("a")

print("".join(res_list))

from math import comb

A, B, K = map(int, input().split())

a = A
b = B
ans = []
while a > 0 or b > 0:
    if a == 0:
        ans.append('b')
        b -= 1
    elif b == 0:
        ans.append('a')
        a -= 1
    else:
        cnt = comb(a + b - 1, a - 1)
        if K <= cnt:
            ans.append('a')
            a -= 1
        else:
            ans.append('b')
            K -= cnt # aをfixした場合の数分は除外されることになるので、順番を小さくする
            b -= 1

print(''.join(ans))