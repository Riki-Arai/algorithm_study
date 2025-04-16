N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
if len(A_list) >= 3:
    for i in range(2, len(A_list)):
        if A_list[i-2] == A_list[i]:
            res += 1
    print(res)
else:
    print(0)