'''
(1) 今までの個数の積み重ねを求めるタイプの問題っぽいのでDPが相性良さそう
(2) しかし愚直にやろうとするとO(M*N*N)となるので計算量を削減する工夫が必要
(3) abs(Ai-Ai)>=Kの条件的に一度満たすiを見つけたらそれよりも大きい or 小さいものは全て加算できる
(4) これを踏まえると累積和のようなDPで設計すればうまくいきそう
(5) しかしこれだけだとうまくいかずに悩んだが、エッジケースの入力を試した際にK=0の出力がおかしいことが判明
(6) 条件によって違うDPにするケースがあることが学べた
'''

import sys; sys.setrecursionlimit(10**7)

N, M, K = map(int, input().split()) # 取得例：1 2

dp_lists = [[0]*(M+1) for _ in range(N)]
for j in range(1, M+1):
    dp_lists[0][j] = j

MOD = 998244353
for i in range(1, N):
    for j in range(1, M+1):
        if K == 0:
            dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][-1])%MOD
        else:
            if j-K >= 0:
                dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][j-K])%MOD
            if j+K-1 <= M:
                dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][M]-dp_lists[i-1][j+K-1])%MOD

        dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i][j-1])%MOD

print(dp_lists[-1][-1]%MOD)