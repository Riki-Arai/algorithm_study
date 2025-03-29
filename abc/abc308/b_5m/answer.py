N, M = map(int, input().split())
C_list = input().split()
D_list = input().split()
P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

p_dic = {}
for i, j in zip(D_list, P_list[1:]):
    p_dic[i] = j

res = 0
for c in C_list:
    if c in p_dic:
        res += p_dic[c]
    else:
        res += P_list[0]

print(res)