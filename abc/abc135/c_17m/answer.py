N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(N):
    f_v = A_list[i]
    s_v = A_list[i+1]
    if B_list[i] >= f_v:
        res += f_v + min(B_list[i]-f_v, s_v)
        A_list[i] = 0
        A_list[i+1] = max(A_list[i+1]-(B_list[i]-f_v), 0)
    else:
        res += B_list[i]
        A_list[i] = f_v-B_list[i]

print(res)