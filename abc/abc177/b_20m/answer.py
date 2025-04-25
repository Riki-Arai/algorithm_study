S = input().strip() # 取得例：A
T = input().strip() # 取得例：A

res = 0
t_l = len(T)
for i in range(len(S)-t_l+1):
    tmp_res = 0
    sub_s = S[i:i+t_l]
    for j in range(t_l):
        if sub_s[j] == T[j]:
            tmp_res += 1

    res = max(res, tmp_res)

print(t_l-res)