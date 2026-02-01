S_list = list(input()) # 取得例：["A","B"・・・]

count = 0
res_lists = []
tmp_list = []
for i, s in enumerate(S_list, 1):
    if s == "#":
        count += 1
        tmp_list.append(i)
        if count == 2:
            res_lists.append(tmp_list)
            tmp_list = []
            count = 0

for l, r in res_lists:
    print(f"{l},{r}")