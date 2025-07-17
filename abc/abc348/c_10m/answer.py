N = int(input())

res = 0
res_dict = {}
for _ in range(N):
    A, C = map(int, input().split())
    if C not in res_dict:
        res_dict[C] = A
    else:
        if res_dict[C] > A:
            res_dict[C] = A

print(sorted(list(res_dict.values()), reverse=True)[0])