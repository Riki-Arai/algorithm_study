N = int(input()) # 数値：1
S = input().strip() # 取得例："A"

r_dp_list = [-float("INF")]*(N+1) # グー
s_dp_list = [-float("INF")]*(N+1) # チョキ
p_dp_list = [-float("INF")]*(N+1) # パー
if S[0] == "R":
    r_dp_list[1] = 0
    p_dp_list[1] = 1
elif S[0] == "S":
    r_dp_list[1] = 1
    s_dp_list[1] = 0
else:
    s_dp_list[1] = 1
    p_dp_list[1] = 0

for i, s in enumerate(S[1:], 2):
    if s == "R":
        r_dp_list[i] = max(s_dp_list[i-1], p_dp_list[i-1])
        p_dp_list[i] = max(s_dp_list[i-1]+1, r_dp_list[i-1]+1)
    elif s == "S":
        r_dp_list[i] = max(s_dp_list[i-1]+1, p_dp_list[i-1]+1)
        s_dp_list[i] = max(r_dp_list[i-1], p_dp_list[i-1])
    else:
        s_dp_list[i] = max(r_dp_list[i-1]+1, p_dp_list[i-1]+1)
        p_dp_list[i] = max(r_dp_list[i-1], s_dp_list[i-1])

print(max(r_dp_list[N], s_dp_list[N], p_dp_list[N]))