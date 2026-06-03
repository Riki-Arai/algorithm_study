N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
C_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

dp_list = [-float("INF")]*(N-1)
sum_c = sum(C_list)-sum(C_list[:2])
res = A_list[0]+B_list[1]+sum_c
sum_a = A_list[0]
dp_list[1] = A_list[0]+B_list[1]
for i in range(2, N-1):
    sum_a += A_list[i-1]
    dp_list[i] = max(sum_a+B_list[i], dp_list[i-1]+B_list[i])
    sum_c -= C_list[i]
    res = max(dp_list[i]+sum_c, res)

print(res)