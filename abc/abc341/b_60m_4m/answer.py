N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
A_lists = [list(map(int, input().split())) for _ in range(N-1)] # 取得例:[[1,2], [3,4]・・[9,10]]