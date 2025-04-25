N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
gcd = 0
for x in range(2, 1001):
    tmp_gcd = len(list(filter(lambda a: a % x == 0, A_list)))
    if tmp_gcd > gcd:
        gcd = tmp_gcd
        res = x

print(res)