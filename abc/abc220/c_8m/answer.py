N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
X = int(input())

sum_ = sum(A_list)
res = (X//sum_)*N
r = X % sum_
tmp_sum = 0
for a in  A_list:
    res += 1
    tmp_sum += a
    if tmp_sum > r:
        print(res)
        exit()

print(res)