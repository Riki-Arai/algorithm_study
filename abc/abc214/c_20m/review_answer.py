# 一番最初にもらう人のindexを決めて、あとは次のSへ渡す時間とTからもらう時間を比較することに気づけるかが大事
N = int(input())
S_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
T_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [0] * N
min_v = min(T_list)
s_idx = T_list.index(min_v)
res_list[s_idx] = min_v
for _ in range(N-1):
    s_idx = (s_idx+1) % N
    res_list[s_idx] = min(T_list[s_idx], res_list[s_idx-1] + S_list[s_idx-1])

for res in res_list:
    print(res)