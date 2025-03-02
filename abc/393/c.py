N = int(input())
a_list = list(map(int, input().split())) 

idx_dic = {}
res = float("inf")
for i in range(N):
    a = a_list[i]
    if a not in idx_dic: 
        idx_dic[a] = i
    else:
        post_idx = idx_dic[a]
        res = min(res, i - post_idx + 1)

if res == float("inf"):
    print(-1)
else:
    print(res)
