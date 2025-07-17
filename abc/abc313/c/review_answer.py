# 解説動画によると数列を操作して期待したいものを求める際には不変量に注目してみると良いらしい
# 最初の回答では不変量であることに注目せず、貪欲法っぽい方法で解決しようとしたが、やはりうまくはいかなかった
N = int(input())
A_list = list(map(int, input().split()))

# 1) A_list の合計と要素数Nから、最終的な「T」「R」を求める
# 動画解説にあったが、A_listはX、X、X、X、X+1、X+1のような形にしたいことからS=X*n+rとなると述べていた
S = sum(A_list)
T = S // N     # 最終的にもっとも多くの要素が揃う値
R = S % N      # T+1 にすべき要素の個数

# 2) ソートして、小さい方から (N - R) 個を T に、残り R 個を T+1 に揃える
# 後の操作でT+1との差分を計算するが、その際にわざわざ小さい値の者と比較しないように、あらかじめソートしている
A_list.sort()

# 3) それぞれの要素が目標値になるまでの差を合計する
diff_sum = 0
#  最初の N-R 個 → T に
for i in range(N - R):
    diff_sum += abs(A_list[i] - T)

#  残りの R 個 → T+1 に
for i in range(N - R, N):
    diff_sum += abs(A_list[i] - (T + 1))

# 4) diff_sum は「要素ごとの変更量の合計」だが、
#    1回の操作で 1 を減らす要素と 1 を増やす要素が同時に動く = 差が2つ分まとめて解消される。
#    よって実際の操作回数は diff_sum // 2
ans = diff_sum // 2
print(ans)

# 以下は不正解コード
#N = int(input())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#A_list.sort()
#res = 0
#l = 0
#r = N - 1
#while r - l >= 1:
#    while A_list[r] - A_list[l] > 1:
#        change = (A_list[r] - A_list[l]) // 2
#        A_list[l] += change
#        A_list[r] -= change
#        res += change
#    r -= 1
#    l += 1
#
#print(res)