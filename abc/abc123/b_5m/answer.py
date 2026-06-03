import itertools as it

A_list = [int(input()) for _ in range(5)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)

res = float("INF")
for p in it.permutations(A_list):
    tmp_res = 0
    for i, pp in enumerate(p, 1):
        tmp_res += pp
        if pp%10 != 0 and i != 5:
            tmp_res += 10-pp%10

    res = min(tmp_res, res)

print(res)