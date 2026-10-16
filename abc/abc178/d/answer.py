S = int(input()) # 取得例：1

dp_lists = [[0]*(S+1) for _ in range(S//3+1)]
for i in range(3, S+1):
    dp_lists[0][0]