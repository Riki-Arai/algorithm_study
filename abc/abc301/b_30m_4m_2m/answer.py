N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i in range(N-1):
    res_list.append(A_list[i])
    if A_list[i] + 1 != A_list[i+1]:
        if A_list[i] + 1 < A_list[i+1]:
            for j in range(A_list[i]+1, A_list[i+1]):
                res_list.append(j)
        else:
            for j in range(A_list[i]-1, A_list[i+1], -1):
                res_list.append(j)

res_list.append(A_list[-1])
print(*res_list)