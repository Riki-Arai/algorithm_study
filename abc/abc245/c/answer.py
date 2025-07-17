N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

x_lists = []
for i in range(N):
    x_lists.append([A_list[i], B_list[i]])

res_list = []
def dfs(i):
    if i == N:
        if abs(res_list[-2]-res_list[-1]) <= K:
            print("Yes")
            exit()
        return
    x_list = x_lists[i]
    for x in x_list:
        res_list.append(x)
        if len(res_list) >= 2 and abs(res_list[i-1]-res_list[i]) > K:
            res_list.pop()
            continue
        dfs(i+1)
    if len(res_list):
        res_list.pop()

dfs(0)
print("No")