N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
A_list.sort()
a_set = set(A_list)
for a in range(0, 101):
    count = 0
    for aa in A_list:
        if aa >= a:
            count += 1

    if count >= a:
        res = max(a, res)

print(res)