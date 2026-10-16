'''
(1) うまい方法を模索したがあまりなかったので愚直な方法で解いた（公式解説でもそのようなことを言っていた）
(2) 時間がかかってしまったが、図に起こして仕組みを可視化すことで実装スピードや正確性が上がることを改めて実感した
'''
import sys; sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_a_list = sorted(A_list)
sub_a = 0
d, r = 0, 0
for i, a in enumerate(s_a_list):
    if a-sub_a == 0:
        continue
    if K >= (a-sub_a)*(N-i):
        K -= (a-sub_a)*(N-i)
        sub_a = a
    else:
        d, r = divmod(K, N-i)
        break

res_list = [max(a-(sub_a+d), 0) for a in A_list]
count = 0
for i in range(N):
    if count == r:
        break
    if res_list[i]:
        res_list[i] -= 1
        count += 1

print(*res_list)