P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
res = ""
for p in P_list:
    res += alp_list[p-1]

print(res)