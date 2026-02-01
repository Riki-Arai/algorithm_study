# 2N人をグループA,Bに分ける。→ グループBの並びを固定して、グループAを順列全探索することで全組み合わせを全探索
# 対策：まだペアができていない人のうち、番号が最も小さい人と誰かでペアを組むことで重複なくペアを数え上げれる
# 再帰関数とDFSで総当たりする。
# DFSは総当たりしたい時に応用できる！
import sys
sys.setrecursionlimit(10**7)

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(2*N-1)]

g_lists = [[0]*2*N for _ in range(2*N)]
for i, A_list in enumerate(A_lists):
    for j, a in enumerate(A_list, i+1):
        g_lists[i][j] = a
        g_lists[j][i] = a

res = 0
used_list = [False]*2*N
def dfs(tmp_res):
    global res
    n_n = -1
    # 一番最初にFalseとなっているものをとにかく選択し、常にiが小さいものを選択
    for i in range(len(g_lists)):
        if not used_list[i]:
            n_n = i
            used_list[n_n] = True
            break

    # どのiも使っていた場合は最大値を選択
    if n_n == -1:
        res = max(tmp_res, res)
        return

    # 例えばn_n=0であれば残りの(0, 1)をペアに選び、次に(2, 3)を選ぶ
    # その次は（0, 2）、（1, 3）のように選ぶ
    # 以上の流れを繰り返すようなイメージ
    for j in range(len(g_lists[n_n])):
        if not used_list[j]:
            used_list[j] = True
            # 入力時にXORの計算をすることでtmp_resを直接変更せずにすみ、かつ次の関数へ渡す値は更新できる
            dfs(g_lists[n_n][j]^tmp_res)
            used_list[j] = False

    used_list[n_n] = False

dfs(0)
print(res)