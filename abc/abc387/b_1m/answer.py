X = int(input())

res_list = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j != X:
            res_list.append(i*j)

print(sum(res_list))