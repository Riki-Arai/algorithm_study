N = int(input())
H_list = list(map(int, input().split()))

b_list = []
res_list = []
for i in range(N-1, -1, -1):
    h = H_list[i]
    res_list.append(len(b_list))

    while len(b_list) and h > b_list[-1]:
        b_list.pop()

    b_list.append(h)

print(*list(reversed(res_list)))