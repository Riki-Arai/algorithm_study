N, A = map(int, input().split())
t_list = list(map(int, input().split()))

res = 0
for t in t_list:
    res = max(res, t)
    res += A
    print(res)