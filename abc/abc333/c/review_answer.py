# 全探索っぽいことまでは制約からわかったが、以下のような解法に辿り着くことはできなかった
# おそらく最初に数字を作るパーツの候補を生成し、それを全探索をするという発想がなかったからだと思う
# あと全探索をした結果をソートして順番を担保する発想もなかったのも解けなかった原因
N = int(input())
L = 12
r = [int("1" * (i + 1)) for i in range(L)]
s = set()
for i in range(L):
    for j in range(L):
        for k in range(L):
            s.add(r[i] + r[j] + r[k])
print(sorted(s)[N - 1])