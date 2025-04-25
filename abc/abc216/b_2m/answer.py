N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["A",1], ["B",2]・・["F",6]]

A_lists = list(map(lambda x: (x[0], x[1]), A_lists))
if len(A_lists) != len(set(A_lists)):
    print("Yes")
else:
    print("No")