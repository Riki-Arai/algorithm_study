N, L, R = map(int, input().split())
A_list = list(map(int, input().split()))

cum_diff_l = 0
max_cum_diff_l = 0
cum = 0
# 最初に全てRだった時と何も変更しなかった時でどちらが最小化を比較
res = min(R*N, sum(A_list))
#　次にLを徐々に増増や場合の比較
for i in range(N):
    # A_list[i]-Lが大きいほどLに置き換えた時に累積和が小さくなる
    cum_diff_l += A_list[i]-L
    cum += A_list[i]
    # 状況次第ではむしろ差分が小さくなってしまうことがあるので、今までの差分の累積和と比較して最大値をとるようにする
    max_cum_diff_l = max(cum_diff_l, max_cum_diff_l)
    res = min(cum-max_cum_diff_l+(N-i-1)*R, res)

print(res)