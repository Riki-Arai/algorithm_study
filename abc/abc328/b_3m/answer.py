N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for m, a in enumerate(A_list, 1):
    date = ""
    for d in range(1, a+1):
        date = str(m) + str(d)
        if len(set(list(date))) == 1:
            res += 1

print(res)