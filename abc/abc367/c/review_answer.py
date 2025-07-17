# 再帰or直積の典型パターン
# returnをしたらfor文がない限りはdfs(0)まで戻るイメージ
# 条件を満たした時のreturnとdfs(lv + 1)が大事
N, K = map(int, input().split())
R_list = list(map(int, input().split()))

def dfs(lv):
    # lvまで要素を決め終えている。もしN個すべて決まったらチェックと出力。
    if lv == N:
        total = sum(current)
        if total % K == 0:
            print(' '.join(map(str, current)))
        return
    # lv番目の要素を 1 から R[lv] まで順に試す
    for val in range(1, R_list[lv] + 1):
        current[lv] = val
        dfs(lv + 1)

current = [0] * N  # 再帰処理で構築するための一時的な配列
dfs(0)

## second
#N, K = map(int, input().split())
#R_list = list(map(int, input().split()))
#
#def dfs(i):
#    if i == N:
#        if sum(tmp_res_list) % K == 0 and len(tmp_res_list) == N:
#            res_lists.append(tmp_res_list.copy())
#        return
#
#    n = R_list[i]
#    for j in range(1, n+1):
#        tmp_res_list.append(j)
#        dfs(i+1)
#        tmp_res_list.pop(-1)
#
#res_lists = []
#for i in range(N):
#    tmp_res_list = []
#    dfs(i)
#
#for res_list in res_lists:
#    print(*res_list)

# 直積で解いても良いらしい
#from itertools import product
#
#n, k = map(int, input().split())
#r = list(map(int, input().split()))
#
#for a in product(*(range(1, x + 1) for x in r)):
#    if not sum(a) % k:
#        print(*a)
#