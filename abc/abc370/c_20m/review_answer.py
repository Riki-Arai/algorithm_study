# 毎回全探索をしたあとにソートを行って辞書順で一番早いものを回答に含めて更新していけば良い
# 1文字ごとに全探索をするようなイメージであり、計算量はO(N^2)となるため計算量としては間に合う
S = input().strip()
T = input().strip()

res_list = []
s_list = list(S)
c_s_list = s_list.copy()
while "".join(s_list) != T:
    tmp_res_list = []
    for i in range(len(c_s_list)):
        if c_s_list[i] != T[i]:
            c_s_list[i] = T[i]
            tmp_res_list.append("".join(c_s_list))
            c_s_list = s_list.copy()

    tmp_res_list.sort()
    res_list.append(tmp_res_list[0])
    s_list = list(tmp_res_list[0])
    c_s_list = s_list.copy()

print(len(res_list))
for res in res_list:
    print(res)