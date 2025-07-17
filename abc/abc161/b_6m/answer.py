N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

t = sum(A_list)
res_list = []
for a in A_list:
    if a >= t * (1/(4*M)):
        res_list.append(a)

if len(res_list) >= M:
    print("Yes")
else:
    print("No")