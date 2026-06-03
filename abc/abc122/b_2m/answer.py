S = input().strip() # 取得例："A"

res = 0
ok_set = set(["A", "C", "G", "T"])
for i in range(len(S)):
    tmp_res = 0
    for j in range(len(S)-i):
        if S[i+j] in ok_set:
            tmp_res += 1
        else:
            break
    res = max(tmp_res, res)

print(res)