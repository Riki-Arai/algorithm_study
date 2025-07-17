N = int(input())

c_min_list = [0, float("INF")]
a_max_list = [0, float("INF")]
x_lists = []
for i in range(N):
    A, C = map(int, input().split())
    x_lists.append([A, C])
    if c_min_list[1] > C:
        c_min_list = [A, C]
    if a_max_list[0] < A:
        a_max_list = [A, C]

res_set = set()
for i in range(N):
    c = a_max_list[1]
    if x_lists[i][1] > c:
        res_set.add(i+1)

for i in range(N):
    a = c_min_list[0]
    if x_lists[i][0] < a:
        res_set.add(i+1)

res_list = []
for i in range(1, N+1):
    if i not in res_set:
        res_list.append(i)

print(len(res_list))
print(*res_list)