N = int(input()) # 取得例：1
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

total_a = 0
res_lists = []
for a, b in input_lists:
    res_lists.append((2*a+b, a, b))
    total_a += a

res = 0
total_b = 0
res_lists.sort(reverse=True, key=lambda x: (x[0], x[1]))
for sum, a, b in res_lists:
    if total_b > total_a:
        print(res)
        exit()
    res += 1
    total_a -= a
    total_b += (sum-a)

print(res)