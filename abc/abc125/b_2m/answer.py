N = int(input()) # 数値：1
V_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
C_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(N):
    diff = V_list[i]-C_list[i]
    if diff >= 0:
        res += diff

print(res)