N, M = map(int, input().split()) # 取得例：1 2
A_lists = [[int(x), s] for x, s in (input().split() for _ in range(M))]

ac_num, wa_num = 0, 0
ac_list = [False] * (N+1)
wa_list = [0] * (N+1)
for p, s in A_lists:
    if not ac_list[p]:
        if s == "WA":
            wa_list[p] += 1
        else:
            ac_list[p] = True
            ac_num += 1

for x, y in zip(ac_list, wa_list):
    if x:
        wa_num += y

print(ac_num, wa_num)


#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N, M = map(int, input().split()) # 取得例：1 2
#A_lists = [[int(x), s] for x, s in (input().split() for _ in range(M))]
#
#ac_sets = set()
#wa_dict = defaultdict(int)
#wa_num = 0
#for p, s in A_lists:
#    if s == "AC" and (p, s) not in ac_sets:
#        ac_sets.add((p, s))
#        wa_num += wa_dict[p]
#    elif s == "WA" and (p, "AC") not in ac_sets:
#        wa_dict[p] += 1
#
#print(len(ac_sets), wa_num)