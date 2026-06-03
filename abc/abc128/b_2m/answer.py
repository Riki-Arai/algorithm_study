N = int(input()) # 数値：1

res_lists = []
for i in range(1, N+1):
    S, P = input().split()
    res_lists.append((S, -int(P), i))

res_lists.sort(key=lambda x: (x[0], x[1]))
for res in res_lists:
    print(res[2])