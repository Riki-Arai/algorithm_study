N, X = map(int, input().split())
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 1
dis = 0
for l in L_list:
    dis += l
    if dis <= X:
        res += 1

print(res)