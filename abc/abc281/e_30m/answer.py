'''
(1) SortedListを使う方法はすぐに思いついたが実装がだるいので他の方法も検討
(2) しかし結局は良い方法がなかったので愚直に実装をした
'''
#  SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedList

N, M, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_a_list = SortedList(A_list[:M])
sum_ = sum(s_a_list[:K])
res_list = [sum_]
for i in range(M, N):
    b_i = s_a_list.bisect_right(A_list[i-M])
    if b_i > K:
        s_a_list.discard(A_list[i-M])
        s_a_list.add(A_list[i])
        b_ii = s_a_list.bisect_right(A_list[i])
        if b_ii > K:
            res_list.append(sum_)
        else:
            sum_ -= s_a_list[K]
            sum_ += A_list[i]
            res_list.append(sum_)
    else:
        sum_ -= A_list[i-M]
        s_a_list.discard(A_list[i-M])
        s_a_list.add(A_list[i])
        b_ii = s_a_list.bisect_right(A_list[i])
        if b_ii > K:
            sum_ += s_a_list[K-1]
            res_list.append(sum_)
        else:
            sum_ += A_list[i]
            res_list.append(sum_)

print(*res_list)