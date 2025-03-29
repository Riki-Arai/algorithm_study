N = int(input())
A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

for i in range(N):
    for j in range(N):
        if i != j:
            s_i = A_list[i]
            s_j = A_list[j]
            concat_s = s_i + s_j
            if concat_s == concat_s[::-1]:
                print("Yes")
                exit()

print("No")