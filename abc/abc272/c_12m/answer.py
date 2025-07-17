N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort(reverse=True)
x_list, y_list = [], []
for a in A_list:
    if len(x_list) == 2:
        break
    if a % 2 == 0:
        x_list.append(a)

for a in A_list:
    if len(y_list) == 2:
        break
    if a % 2 != 0:
        y_list.append(a)

if len(x_list) == 2 and len(y_list) == 2:
    print(max(sum(x_list), sum(y_list)))
elif len(x_list) == 2 and len(y_list) != 2:
    print(sum(x_list))
elif len(x_list) != 2 and len(y_list) == 2:
    print(sum(y_list))
else:
    print(-1)