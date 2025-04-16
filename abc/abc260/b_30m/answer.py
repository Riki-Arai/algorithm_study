N, X, Y, Z = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
A_lists = [[i, a] for i, a in enumerate(A_list, 1)]
B_lists = [[i, b] for i, b in enumerate(B_list, 1)]

s_A_lists = sorted(A_lists, key=lambda x: x[1], reverse=True)
if len(s_A_lists[:X]) > 0:
    for x in s_A_lists[:X]:
        res_list.append(x[0])
        A_lists.remove(x)

B_lists = list(filter(lambda x: x[0] not in res_list, B_lists))
s_B_lists = sorted(B_lists, key=lambda x: x[1], reverse=True)
if len(s_B_lists[:Y]) > 0:
    for y in s_B_lists[:Y]:
        res_list.append(y[0])
        B_lists.remove(y)

A_lists = list(filter(lambda x: x[0] not in res_list, A_lists))
z_lists = []
for a, b in zip(A_lists, B_lists):
    z_lists.append([a[0], a[1]+b[1]])

s_z_lists = sorted(z_lists, key=lambda x: x[1], reverse=True)
if len(s_z_lists[:Z]) > 0:
    for z in s_z_lists[:Z]:
        res_list.append(z[0])

for res in sorted(res_list):
    print(res)