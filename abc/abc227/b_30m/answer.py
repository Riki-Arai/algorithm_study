N = int(input())
S_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_set = set()
for a in range(1, 201):
    for b in range(1, 201):
        s = 4*a*b + 3*a + 3*b
        res_set.add(s)

res = 0
for s in S_list:
    if s not in res_set:
        res += 1

print(res)