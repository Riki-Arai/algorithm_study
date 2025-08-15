import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
B_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_sets = set()
for i in range(N):
    for j in range(N):
        if B_lists[i][j] == "1":
            res_sets.add((i, j))

for _ in range(4):
    r_a_lists = [[0]*N for _ in range(N)]
    tmp_sets = set()
    for i in range(N):
        for j in range(N):
            r_a_lists[N-j-1][i] = A_lists[i][j]
            if A_lists[i][j] == "1":
                tmp_sets.add((N-j-1, i))

    if tmp_sets <= res_sets:
        print("Yes")
        exit()

    A_lists = copy.deepcopy(r_a_lists)

print("No")

## first
#import copy
#
#N = int(input())
#A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#B_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
#b_set = set()
#for i in range(N):
#    for j in range(N):
#        if B_lists[i][j] == "1":
#            b_set.add((i, j))
#
#count = 0
#tmp_A_lists = copy.deepcopy(A_lists)
#while True:
#    for i in range(N):
#        for j in range(N):
#            tmp_A_lists[i][j] = A_lists[N-1-j][i]
#
#    A_lists = copy.deepcopy(tmp_A_lists)
#    a_set = set()
#    for i in range(N):
#        for j in range(N):
#            if A_lists[i][j] == "1":
#                a_set.add((i, j))
#
#    if a_set <= b_set:
#        print("Yes")
#        exit()
#
#    count += 1
#    if count == 4:
#        print("No")
#        break