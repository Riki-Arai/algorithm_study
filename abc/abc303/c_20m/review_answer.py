# 追加、削除、探索の計算量が優秀なsetを使うことに気づくかどうかがポイント
# 自分の中では少し時間がかかってしまった
# 時間がかかった原因としてはダラダラしたのもあるが、茶色だったのでこんな簡単な回答なわけはないと思ってしまって無駄に悩んだこともありそう（経験不足？？）
N, M, H, K = map(int, input().split())
S = input().strip()

res_set = set()
for _ in range(M):
    res_set.add(tuple(map(int, input().split())))

res_list = [0, 0]
# 上、右、下、左
move_dict = {"L":(-1, 0), "U":(0, 1), "R":(1, 0), "D":(0, -1)}
for s in S:
    H -= 1
    if H < 0:
        print("No")
        exit()
    h, w = move_dict[s]
    res_list[0] += h
    res_list[1] += w

    if H < K and (res_list[0], res_list[1]) in res_set:
        H = K
        res_set.discard((res_list[0], res_list[1]))

print("Yes")