# breakをする前はCpythonでAC、pypyではTLEする現象が起きた
# 問題自体は全探索をすることが一番のポイント、あとは重複して数えあげないことくらい
N = int(input()) # 数値

res_set = set()
end = 10**5+1
for a in range(2, end):
    for b in range(2, 35):
        n = a**b
        if 1 <= n <= N:
            res_set.add(n)
        # これを追加することでpypyでもACしたので、無駄な処理を抑える工夫もした方が良いらしい
        elif n > N:
            break

print(N-len(res_set))