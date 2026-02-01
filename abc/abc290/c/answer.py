N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
s_a_list = sorted(list(set(A_list)))
for i in range(N-1):
    if s_a_list[i] + 1 != s_a_list[i+1]:
        print(s_a_list[i])
        exit()

print(s_a_list[i+1])