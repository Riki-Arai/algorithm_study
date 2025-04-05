from collections import defaultdict

N = int(input())

A_lists = []
for _ in range(N):
    C = int(input())
    A_lists.append(list(map(int, input().split())))

X = int(input())

res_dic = defaultdict(list)

for i, A_list in enumerate(A_lists, start=1):
    if X in A_list:
        res_dic[len(A_list)].append(i)

if not res_dic:
    print(0)
    print()
else:
    min_len = min(res_dic.keys())
    res_list = sorted(res_dic[min_len])
    print(len(res_list))
    print(*res_list)

from collections import defaultdict

N = int(input())

A_lists = []
for _ in range(N):
    C = int(input())
    A_lists.append(list(map(int, input().split())))

X = int(input())

res_dic = defaultdict(list)
res_num = float("INF")
for i, A_list in enumerate(A_lists, 1):
    if X in A_list:
        res_dic[len(A_list)].append(i)
        res_num = min(res_num, len(A_list))

if res_num != float("INF"):
    print(len(res_dic[res_num]))
    print(*sorted(res_dic[res_num]))
else:
    print(0)
    print()

#N = int(input())
#
#A_lists = []
#for _ in range(N):
#    C = int(input())
#    A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#    A_lists.append(A_list)
#
#X = int(input())
#res_dic = {}
#min_v = 100
#for i, A_list in enumerate(A_lists, 1):
#    if X in A_list:
#        if len(A_list) not in res_dic:
#            res_dic[len(A_list)] = [i]
#        else:
#            tmp_list = res_dic[len(A_list)]
#            tmp_list.append(i)
#            res_dic[len(A_list)] = tmp_list 
#        min_v = min(min_v, len(A_list))
#
#if min_v not in res_dic:
#    print(0)
#    print()
#else:
#    res_list = res_dic[min_v]
#    res_list.sort()
#    print(len(res_list))
#    print(*res_list)