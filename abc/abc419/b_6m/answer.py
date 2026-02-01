Q = int(input()) # 数値：1

res_list = []
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        _, x = input_
        x = int(x)
        res_list.append(x)
    else:
        res = min(res_list)
        print(res)
        res_list.remove(res)