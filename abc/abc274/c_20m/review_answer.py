# 最初の一匹の番号が1とあるので、A_listの最初は1で固定っぽい？？
# また2Ai、2Ai+1と勘違いしてしまっていたが、2iと2i+1である点に注意
N = int(input())
A_list = list(map(int, input().split()))

deep_dict = {1: 0}
for i, a in enumerate(A_list, 1):
    cur_deep = deep_dict[a]
    deep_dict[2*i] = cur_deep + 1
    deep_dict[2*i+1] = cur_deep + 1

for v in deep_dict.values():
    print(v)