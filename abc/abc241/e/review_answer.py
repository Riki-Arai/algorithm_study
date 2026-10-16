'''
(1) K回の操作が大きすぎる、数列内を移動する条件からどこかしらでループが発生すると予想
    →過去にそのような問題にあたったことがあったので、そのように予想ができた
(2) いくつか考察をしてもループに入りそうだったので、そのような仮定で実装をしていった
(3) 正解はできたが確証がないところが良くなかったので、GPTに聞いたところ鳩の巣原理とよばれるものらしい
(4) K回の操作が大きいなどでループがキーになりそうなときはループに着目したいところ
'''
# GPTは累積和を利用してコンパクトに回答
N, K = map(int, input().split())
A = list(map(int, input().split()))

seen = {}
S = [0]
i = 0

while i not in seen:
    seen[i] = len(S) - 1
    S.append(S[-1] + A[i])
    i = (i + A[i]) % N

if K < len(S):
    print(S[K])
else:
    start = seen[i]
    length = len(S) - 1 - start
    total = S[-1] - S[start]

    q, r = divmod(K - start, length)
    print(q * total + S[start + r])


import sys; sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

k = 0
res = 0
seen_set = set()
con_list = []
i = 0
while i not in seen_set:
    k += 1
    res += A_list[i]
    seen_set.add(i)
    con_list.append(i)
    i = (i+A_list[i])%N
    if k == K:
        print(res)
        exit()

roop_sum = 0
roop_count = 0
roop_cum_list = [0]
for j in range(con_list.index(i), len(con_list)):
    res -= A_list[con_list[j]]
    k -= 1
    roop_count += 1
    roop_sum  += A_list[con_list[j]]
    roop_cum_list.append(roop_cum_list[-1]+A_list[con_list[j]])

m, r = divmod(K-k, roop_count)
print(res+m*roop_sum+roop_cum_list[r])