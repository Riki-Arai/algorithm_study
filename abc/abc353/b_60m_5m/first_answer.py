N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
boat = K
while len(A_list) > 0:
    if boat - A_list[0] == 0:
        A_list.pop(0)
        res += 1
        boat = K
    elif boat - A_list[0] > 0:
        if len(A_list) == 1:
            res += 1
        boat -= A_list.pop(0)
    else:
        res += 1
        boat = K

print(res)