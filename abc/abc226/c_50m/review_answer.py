# whileで解こうとしたが、探索しきったら戻る性質を利用したいのでDFSの方が相性が良いと判断
# 深く生きすぎるとメモリーエラーではなく、REが発生してしまうことを学んだ（DFS時にはsys.setrecursionlimit(10**7)は必須）
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
skill_set = set()
def dfs(i):
    global res
    if A_lists[i][1] == 0:
        skill_set.add(i+1)
        res += A_lists[i][0]
        return

    for a in A_lists[i][2:]:
        if a not in skill_set:
            dfs(a-1)

    res += A_lists[i][0]
    skill_set.add(i+1)

dfs(N-1)
print(res)