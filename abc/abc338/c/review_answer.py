# 片方の料理の個数を固定して、もう片方の料理の個数を探索していく
N = int(input())
Q_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

a_num = float("INF")
for i, a in enumerate(A_list):
    if a > 0:
        a_num = min(Q_list[i]//a, a_num)

res = 0
b_num = float("INF")
for j in range(a_num+1):
    for k, b in enumerate(B_list):
        if b > 0:
            q = Q_list[k] - A_list[k]*j
            b_num = min(q//b, b_num)
    res = max(j+b_num, res)

print(res)