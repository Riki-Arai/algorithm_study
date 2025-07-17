N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

h_num = 0
for a in A_list:
    h_num += a

if h_num > N:
    print(-1)
else:
    print(N-h_num)