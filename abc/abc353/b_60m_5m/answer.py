N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res, seat = 0, 0
while len(A_list) > 0:
    if seat + A_list[0] <= K:
        if len(A_list) == 1:
            res += 1
        seat += A_list.pop(0)
    else:
        res += 1
        seat = 0

print(res)