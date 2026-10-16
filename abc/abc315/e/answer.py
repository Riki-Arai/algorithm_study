'''
(1) 前提となる本の数が2秒以内に収まるので全てを1度だけ探索する分には問題ない
(2) 深く探索したり、引き返すような処理なのでDFSで実装
(3) C問題に類題があるのですぐにできた
'''

import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
input_lists = [[]]
for _ in range(N):
    input_lists.append(list(map(int, input().split())))

seen_set = set()
res_list = []
def dfs(a):
    if input_lists[a][0] == 0:
        seen_set.add(a)
        res_list.append(a)
        return

    for b in input_lists[a][1:]:
        if b not in seen_set:
            dfs(b)

    seen_set.add(a)
    res_list.append(a)

dfs(1)
print(*res_list[:-1])