N = int(input()) # 数値：1
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

l_set = set([0])
r_set = set([N])
for i in range(N):
    if L_list[i] == 0:
        l_set.add(i)
        l_set.add(i+1)
    else:
        break

for i in range(N-1, -1, -1):
    if L_list[i] == 0:
        r_set.add(i)
        r_set.add(i+1)
    else:
        break

print(N+1-len(l_set|r_set))