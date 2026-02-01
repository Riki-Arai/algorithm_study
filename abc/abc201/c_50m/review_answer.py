S = input().strip()

res = 0
for i in range(10000):
    p_list = list("0000")
    c = 0
    while i > 0:
        p_list[c] = str(i%10)
        i //= 10
        c += 1

    p_set = set(p_list)
    for i, s in enumerate(S):
        if s == "o" and str(i) not in p_set:
            break
        elif s == "x" and str(i) in p_set:
            break
    else:
        res += 1

print(res)


# 解けはしたが、公式回答の方スマートで汎用性もあるのでそちらの解き方をぜひ覚えておく
# パターンの列挙が間に合うのでその方針の方が楽
S = input().strip()

res = 0
for i in range(10**4):
    res_list = [False] * 10
    # 例えば0であれば0000、111は0111にあたる（111でも処理内容的に0にフラグが立ってくれる）
    for _ in range(4):
        m, r = divmod(i, 10)
        res_list[r] = True
        i = m

    for j, s in enumerate(S):
        if s == "o" and res_list[j] == False:
            break
        if s == "x" and res_list[j] == True:
            break
    else:
        res += 1

print(res)


#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#S = input().strip()
#
#x_list = []
#y_list = []
#for i, s in enumerate(list(S)):
#    if s == "o":
#        x_list.append(i)
#    elif s == "?":
#        y_list.append(i)
#
#if s.count("o") >= 5 or s.count("x") == 10:
#    print(0)
#else:
#    res = 0
#    res_set = set()
#    for p in itertools.product(x_list, repeat=4):
#        if set(x_list) <= set(p):
#            res += 1
#            res_set.add(tuple(p))
#
#    for p in itertools.product(x_list+y_list, repeat=4):
#        if set(x_list) <= set(p) and tuple(p) not in res_set:
#            res += 1
#    print(res)