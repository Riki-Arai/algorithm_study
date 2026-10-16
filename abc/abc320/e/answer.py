'''
(1) 一番のポイントとしては1つのクエリで離脱をする人数が最大でもひとりであること
(2) このような場合は列などに復帰する処理をwhileで行っても、実は計算量がそこまで重くならない
    →最大Nまで待たせるためにはN行の処理が必要で、それを全て復帰させてもその1回のみがN回の処理になるだけ
    →再びNまで待たせたければN行の処理が必要となってしまう
(3) このようにあるクエリで一つだけが待ち状態になるなどの変化をするタイプは実は計算量がそこまで重くならないことを疑うようにしたい
(4) このような問題はCやD問題でたまに見かける
'''
import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2

res_list = [0]*N
ac_lists, wt_lists = [i for i in range(N)], []
hq.heapify(ac_lists)
hq.heapify(wt_lists)
for _ in range(M):
    T, W, S = map(int, input().split()) # 取得例：1 2
    if len(wt_lists):
        while len(wt_lists):
            if wt_lists[0][0] <= T:
                _, w_i = hq.heappop(wt_lists)
                hq.heappush(ac_lists, w_i)
            else:
                break

    if len(ac_lists):
        a_i = hq.heappop(ac_lists)
        res_list[a_i] += W
        hq.heappush(wt_lists, (T+S, a_i))

for res in res_list:
    print(res)