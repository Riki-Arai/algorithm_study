'''
(1) Nの値次第でTLEになるので、おそらくループをする箇所を見つけて計算をする問題だと予想
(2) ナイーブなコードで出力を確認してみたところループがやはり発生していた
(3) 確証はないところもあるが、ループが解答のポイントだとして解答を作成
(4) ループは途中から始まることやループの途中で終了をすることに気をつけた
(5) ちなみに鳩の巣原理によって計算量はO(M)で収まるとのこと（一番時間がかかる数列は+1ずつするものだが、M+1目で重複が発生する）
'''
N, X, M = map(int, input().split())

x_list = []
x_set = set()
for i in range(N):
    if X in x_set:
        break
    x_list.append(X)
    x_set.add(X)
    X = (X ** 2) % M

if len(x_list) == N:
    print(sum(x_list))
else:
    x_i = x_list.index(X)
    x_n = len(x_list) - x_i
    
    m, r = divmod(N - x_i, x_n)
    
    before_loop = sum(x_list[:x_i])       # 周期に入る前の部分
    loop_sum = sum(x_list[x_i:])          # 周期1回分の合計
    remaining_sum = sum(x_list[x_i:x_i+r]) # 余りの部分
    
    print(before_loop + loop_sum * m + remaining_sum)