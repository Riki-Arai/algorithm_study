N = int(input()) # 取得例：1

res_list = []
alp_dict = {chr(i):chr(i) for i in range(ord('a'), ord('z') + 1)}
alp_list = list(alp_dict.keys())
while N > 0:
    r = (N-1)%26
    res_list.append(alp_list[r])
    N = (N - 1) // 26

print("".join(res_list)[::-1])