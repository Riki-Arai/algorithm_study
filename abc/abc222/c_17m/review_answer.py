# 結果を辞書などで持つ、判定を関数化する、ソートの際に2つの値を指定して片方は-1にするといった工夫ができたのがよかった
# 順位をみてみると意外と早いACだった
N, M = map(int, input().split())
A_lists = [list(input()) for _ in range(N*2)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

def judge(x, y):
    if x == y:
        return "d"
    elif (x == "G" and y == "C") or (x == "C" and y == "P") or (x == "P" and y == "G"):
        return "w"
    else:
        return "l"

res_lists = [[i, 0] for i in range(N*2)]
for i in range(M):
    for j in range(N):
        f_idx = res_lists[2*j][0]
        s_idx = res_lists[2*j+1][0]
        f = A_lists[f_idx][i]
        s = A_lists[s_idx][i]
        r = judge(f, s)
        if r == "w":
            res_lists[2*j][1] += 1
        elif r == "l":
            res_lists[2*j+1][1] += 1

    res_lists.sort(key=lambda x: [x[1], x[0]*-1], reverse=True)

for res, _ in res_lists:
    print(res+1)