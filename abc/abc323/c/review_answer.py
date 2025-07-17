# 最初は計算量の見積もりを勘違いしていたが、for文のループではない限りは意外と処理ができる
# スコアを加算する時は未解答の問題のスコアを加算してあげることもポイント

N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

max_score = 0
S_list = []
score_list = []
for i in range(N):
    S = input().strip()
    S_list.append(S)
    tmp_score = 0
    for j, s in enumerate(list(S)):
        if s == "o":
            tmp_score += A_list[j]

    max_score = max(tmp_score+i+1, max_score)
    score_list.append(tmp_score+i+1)

for i in range(N):
    S = S_list[i]
    score = score_list[i]
    if score == max_score:
        print(0)
    else:
        tmp_score_list = []
        for i, s in enumerate(list(S)):
            if s == "x":
                tmp_score_list.append(A_list[i])

        diff = max_score - score
        cum_score = 0
        tmp_score_list.sort(reverse=True)
        for j in range(len(tmp_score_list)):
            cum_score += tmp_score_list[j]
            if cum_score > diff:
                print(j+1)
                break