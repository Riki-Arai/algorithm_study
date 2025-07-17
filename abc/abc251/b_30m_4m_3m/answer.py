N, W = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

w_set = set()
for i in range(N):
    w_1 = A_list[i]
    if w_1 <= W:
        w_set.add(w_1)
    for j in range(N):
        if w_1 > W:
            break
        w_2 = A_list[j]
        if i != j and w_1 + w_2 <= W:
            w_set.add(w_1 + w_2)
        for k in range(N):
            if w_1 + w_2 > W:
                break
            w_3 = A_list[k]
            if i != j and i != k and j != k and w_1 + w_2 + w_3 <= W and w_1 + w_2 + w_3 not in w_set:
                w_set.add(w_1 + w_2 + w_3)

print(len(w_set))