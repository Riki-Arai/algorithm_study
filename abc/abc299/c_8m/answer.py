N = int(input())
S = input().strip()

if "-" not in S:
    print(-1)
    exit()

res_list = S.split("-")
res = max(list(map(len, res_list)))
if res == 0:
    print(-1)
else:
    print(res)