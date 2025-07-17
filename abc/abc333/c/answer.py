N = int(input())

res_list = []
n_list = [int("1"*i) for i in range(1, 101)]
for i in range(100):
    for j in range(100):
        for k in range(100):
            v = n_list[i] + n_list[j] + n_list[k]
            res_list.append(v)

res_list = list(set(res_list))
res_list.sort()
print(res_list[N-1])