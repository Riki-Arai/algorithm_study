N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
A_lists = [list(map(int, input().split())) for _ in range(N-1)] # 取得例:[[1,2], [3,4]・・[9,10]]

for i in range(N-1):
    A_list[i+1] = A_list[i+1] + (A_list[i] // A_lists[i][0]) * A_lists[i][1]

print(A_list[-1])