n = int(input()) # 数値：1
p_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(1, n-1):
    if (p_list[i-1] < p_list[i] and p_list[i] < p_list[i+1]) or (p_list[i-1] > p_list[i] and p_list[i] > p_list[i+1]):
        res += 1

print(res)