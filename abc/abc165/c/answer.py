N, M, Q = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

def dfs(n_list, res):
    if len(n_list) == N:
        tmp_res = 0
        for A_list in A_lists:
            a, b, c, d = A_list
            if n_list[b-1] - n_list[a-1] == c:
                tmp_res += d
        return max(tmp_res, res)
    for v in range(1, M+1):
        n_list.append(v)
        res = dfs(n_list, res)
        n_list.pop()

res = 0
dfs([], res)
print(res)