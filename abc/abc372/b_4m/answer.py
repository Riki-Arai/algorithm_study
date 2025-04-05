M = int(input())

res_list = []
for _ in range(20):
    while M > 0:
        for i in range(10, -1, -1):
            if 3 ** i <= M:
                M -= 3 ** i
                res_list.append(i)
                break

print(len(res_list))
print(*res_list)