N, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 1
res_list = [False] * N
res_list[X-1] = True
while True:
    if res_list[A_list[X-1]-1]:
        print(res)
        break

    res_list[A_list[X-1]-1] = True
    res += 1
    X = A_list[X-1]

    if res == N:
        print(res)
        break