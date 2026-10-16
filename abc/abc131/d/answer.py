'''
(1) 簡単すぎて戸惑ったが、区間スケジューリングの問題として解けた
'''
N = int(input()) # 数値：1
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

t = 0
input_lists.sort(lambda x: x[1])
for a, b in input_lists:
    if t+a > b:
        print("No")
        exit()
    t += a

print("Yes")