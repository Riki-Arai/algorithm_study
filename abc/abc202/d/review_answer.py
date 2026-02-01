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
