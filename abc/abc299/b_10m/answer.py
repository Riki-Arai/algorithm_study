import collections

N, T = map(int, input().split())
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
R_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

score_dic = collections.defaultdict(list)
for i in range(N):
    score_dic[C_list[i]].append([i+1, R_list[i]])

if T in score_dic:
    res_lists = score_dic[T]
    res_lists.sort(key=lambda x: x[1])
    print(res_lists[-1][0])
else:
    res_lists = score_dic[C_list[0]]
    res_lists.sort(key=lambda x: x[1])
    print(res_lists[-1][0])