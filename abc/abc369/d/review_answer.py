N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

dp_lists = [[0, 0] for _ in range(N)]
dp_lists[0] = [0, A_list[0]]
for i, a in enumerate(A_list[1:], 1):
    dp_lists[i][0] = max(dp_lists[i-1][1]+2*a, dp_lists[i-1][0])
    dp_lists[i][1] = max(dp_lists[i-1][1], dp_lists[i-1][0]+a)

print(max(dp_lists[N-1]))