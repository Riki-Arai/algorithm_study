from collections import Counter

N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_lists = []
for k, v in Counter(A_list).items():
    res_lists.append(k*v)

res_lists.sort(reverse=True)
print(sum(res_lists)-sum(res_lists[:K]))