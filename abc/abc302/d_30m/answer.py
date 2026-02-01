import bisect as bi

N, M, D = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

B_list.sort()
res = -1
for a in A_list:
    b_i = bi.bisect_left(B_list, a)
    if b_i == 0:
        b = B_list[0]
        if abs(a-b) <= D:
            res = max(a+b, res)
    elif b_i == M:
        b = B_list[M-1]
        if abs(a-b) <= D:
            res = max(a+b, res)
    else:
        b = B_list[b_i]
        if abs(a-b) <= D:
            res = max(a+b, res)
        b = B_list[b_i-1]
        if abs(a-b) <= D:
            res = max(a+b, res)

    # a=3、b=[2 4 5 15]の場合だと上の処理だけだと4を選択してしまうのでこの処理も必要
    b_i = bi.bisect_right(B_list, a+D)
    if b_i != 0:
        b = B_list[b_i-1]
        if abs(a-b) <= D:
            res = max(a+b, res)

print(res)