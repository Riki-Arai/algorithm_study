N = int(input())
D_list = list(map(int, input().split()))

res = 0
for i, d in enumerate(D_list, 1):
    for dd in range(1, d+1):
        dd_set = set(list(str(dd)))
        if len(dd_set) == 1 and set(list(str(i))) == dd_set:
            res += 1
print(res)
