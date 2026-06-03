S = input().strip()
N = int(input())

rev_s = S[::-1]
L = len(S)

min_v = 0
max_v = 0

# lower_q[i] := i 未満、つまり重み 2^0 〜 2^(i-1) の中にある ? の合計
lower_q = [0] * (L + 1)

for_i = range(L)
for i in for_i:
    bit = 1 << i
    lower_q[i + 1] = lower_q[i]

    if rev_s[i] == "1":
        min_v += bit
        max_v += bit
    elif rev_s[i] == "?":
        max_v += bit
        lower_q[i + 1] += bit

if min_v > N:
    print(-1)
else:
    ans = max_v

    # 上位ビットから、必要なら ? を 1 -> 0 に落とす
    for i in range(L - 1, -1, -1):
        if rev_s[i] == "?":
            # このビットを 1 のままにして、下位の ? を全部 0 にしても N を超えるなら、
            # このビットは 0 にするしかない
            if ans - lower_q[i] > N:
                ans -= 1 << i

    print(ans)