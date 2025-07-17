N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["A",1], ["B",2]・・["F",6]]

res_dict = {}
res_set = set()
for i, A_list in enumerate(A_lists, 1):
    s, t = A_list[0], int(A_list[1])
    if s not in res_set:
        res_set.add(s)
        res_dict[i] = t

res_list = list(res_dict.items())
res_list.sort(key=lambda x: x[1], reverse=True)
print(res_list[0][0])