N = int(input())

# 列を base からの差分で管理
A = [0] + list(map(int, input().split()))
base = 0

# 差分が 0 でないかもしれない場所
# はじめは 1, ..., N すべて
added_index = list(range(1, N + 1))

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[0]

    if t == 1:
        # 差分が 0 でないところを消去
        while added_index:
            A[added_index.pop()] = 0

        base = query[1]

    elif t == 2:
        # index 番目の差分に加える
        index, value = query[1], query[2]
        A[index] += value
        added_index.append(index)

    else:
        # base に index 番目の差分を加える
        index = query[1]
        print(str(base + A[index]))