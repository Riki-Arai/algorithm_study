N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

called_list = [False] * N
for i, a in enumerate(A_list, 0):
    if called_list[i] == False:
        called_list[a-1] = True

res_list =  [i for i, a in enumerate(called_list, 1) if a == False]
print(len(res_list))
print(*res_list)