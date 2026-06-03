N = int(input()) # 数値：1
T = input().strip() # 取得例："A"

count = 0
dp_list = [[0, 0] for _ in range(N+1)]
if T[0] == "1":
    dp_list[0][0] = 1
else:
    count += 1

for i, t in enumerate(T[1:], 1):