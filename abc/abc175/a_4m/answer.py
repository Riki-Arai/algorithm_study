S = input().strip() # 取得例：A

res = 0
tmp_res = 0
for i, s in enumerate(list(S), 1):
    if s == "R":
        tmp_res += 1
        if i == 3:
            res = max(tmp_res, res)
    else:
        res = max(tmp_res, res)
        tmp_res = 0

print(res)