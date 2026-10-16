'''
(1) 試行回数的にパターンがあるタイプの問題なので、観察用コードを作成して出力を観察
(2) RLの境目に人が集まる、RとLの偶奇が同じときはそれらの和の半分、そうではないときは細かく調整することなどがわかった
(3) ランレングスを用いつつ、出力と照らし合わせて偶奇が異なる時のパターンをコードに落とし込んだ
'''
import itertools as it
from collections import deque

S = input().strip() # 取得例："A"


dq = deque()
for i in range(len(S)-1):
    if S[i] == "R" and S[i+1] == "L":
        dq.append(i)

g_lists = [(k, len(list(v))) for k, v in it.groupby(S)]
res_list = [0]*len(S)
for i in range(0, len(g_lists)-1, 2):
    k, v = g_lists[i]
    kk, vv = g_lists[i+1]
    j = dq.popleft()
    if k == "R" and kk == "L":
        if v%2 == vv%2:
            res_list[j] = int((v+vv)//2)
            res_list[j+1] = int((v+vv)//2)
        else:
            if max(v, vv)%2 == 0:
                if v > vv:
                    res_list[j] = (v+vv)//2
                    res_list[j+1] = (v+vv+1)//2
                else:
                    res_list[j] = (v+vv+1)//2
                    res_list[j+1] = (v+vv)//2
            else:
                if v > vv:
                    res_list[j] = (v+vv+1)//2
                    res_list[j+1] = (v+vv)//2
                else:
                    res_list[j] = (v+vv)//2
                    res_list[j+1] = (v+vv+1)//2

print(*res_list)