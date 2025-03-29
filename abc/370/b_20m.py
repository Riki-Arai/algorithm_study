N = int(input())

item_dic = {}
for i in range(N):
    a_list = list(map(int, input().split()))
    for j, a in enumerate(a_list):
        item_dic[(i, j)] = a

res = 1
for j in range(N):
    if res - 1 >= j:
        res = item_dic[(res - 1, j)]
    else:
        res = item_dic[(j, res - 1)]

print(res)
