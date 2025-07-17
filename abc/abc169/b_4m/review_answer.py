N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort()
res = 1
for a in A_list:
    res *= a
    if res > 10**18:
        print(-1)
        exit()

print(res)