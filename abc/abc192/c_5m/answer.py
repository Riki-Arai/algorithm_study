N, K = map(int, input().split())

res = N
for _ in range(K):
    f_list = sorted(list(map(int, list(str(res)))), reverse=True)
    s_list = sorted(list(map(int, list(str(res)))))
    res = int("".join(map(str, f_list))) - int("".join(map(str, s_list)))

print(res)