N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["A",1], ["B",2]・・["F",6]]

A_lists.sort(key=lambda x: int(x[1]))
print(A_lists[-2][0])