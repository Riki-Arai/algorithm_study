N = int(input()) # 数値：1
V_list = list(map(int, input().split()))

V_list.sort()
res = (V_list[0]+V_list[1]) / 2
for v in V_list[2:]:
    res = (v + res) / 2

print(res)