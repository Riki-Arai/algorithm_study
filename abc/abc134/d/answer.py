'''
(1) 小さい箱からボールを入れるかどうかを決めてしまうと、それより大きい箱にボールを入れた時に小さい倍数の総数に影響が出てしまう
(2) よって大きい箱から順番にaの値に従って入れるかどうかを決めていくことで、それより小さい箱はaのよって後出し的に入れるかどうかの判断が可能
(3) 倍数の合計については、大きくなるほど計算量が少なくなる性質（級数）があるのでN*logNに収まる
'''
N = int(input()) # 数値：1
a_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

b2b_list = [0]*N
for i in range(N-1, -1, -1):
    a = a_list[i]
    cum = 0
    for j in range(i, N, i+1):
        cum += b2b_list[j]

    if cum%2 != a:
        b2b_list[i] += 1

res_list = []
for i in range(N):
    if b2b_list[i]:
        res_list.append(i+1)

print(len(res_list))
print(*res_list)