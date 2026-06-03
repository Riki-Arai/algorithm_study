N = int(input()) # 数値：1
P_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_p_list = sorted(P_list)
for i in range(N):
    for j in range(N):
        c_p_list = P_list.copy()
        c_p_list[i], c_p_list[j] = c_p_list[j], c_p_list[i]
        if c_p_list == s_p_list:
            print("YES")
            exit()

print("NO")