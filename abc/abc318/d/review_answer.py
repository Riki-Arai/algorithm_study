N = int(input())

# 上三角だけ入力される
d = [[0]*N for _ in range(N)]
for i in range(N-1):
    row = list(map(int, input().split()))
    for j, v in enumerate(row, i+1):
        d[i][j] = v

dp = [0] * (1 << N)
for S in range(1 << N):
    # iビット目が1であるかどうかを確認(iビット目を右端にシフトし、&1であればiビット目は1であることがいえる)
    for l in range(N):
        if not (S >> l) & 1:
            break
    else:
        continue  # 全部使っているならスキップ

    # l とペアにする相手を選ぶ
    for i in range(l+1, N):
        if not (S >> i) & 1:
            next_S = S | (1 << l) | (1 << i)
            dp[next_S] = max(dp[next_S], dp[S] + d[l][i])

# 今回は全ての頂点同士のペアを選択した方がいいので、必然的に一番右端の値が最大値になる（ただmaxをとっても良い)
print(dp[(1 << N) - 1])

#import itertools as it
#
#N = int(input())
#
#d = [[0] * N for _ in range(N)]
#for i in range(N - 1):
#    input_ = list(map(int, input().split()))
#    for j, v in enumerate(input_, i + 1):
#        d[i][j] = v
#
#dp = [0] * (1 << N)
#
#bit_lists = list(it.product([0, 1], repeat=N))
#
#for bit_list in bit_lists:
#    b = 0
#    for i, x in enumerate(bit_list):
#        if x == 1:
#            b |= 1 << i
#
#    l = -1
#    for i, x in enumerate(bit_list):
#        if x == 0:
#            l = i
#            break
#
#    if l == -1:
#        continue
#
#    for i, x in enumerate(bit_list):
#        if x == 0:
#            nb = b | (1 << l) | (1 << i)
#            dp[nb] = max(dp[nb], dp[b] + d[l][i])
#
#print(dp[-1])