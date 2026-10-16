'''
(1) 愚直な方法で解こうとしたが、処理が複雑な影響でなかなかACできず
(2) 試行錯誤の末に完成系と比較、値が異なる部分の区間がK未満であるかどうかの判定に落とし込めた
(3) 完成系と比較して判定するパターンはたまに見かけるので、その意識をもっと持つべきだった
(4) C問題だと意外とアイディアによっては簡潔に解答できる問題があるので、実装が複雑になりそうな手法である時はもっと簡単な手法がないかを考えてみる
'''
N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_a_list = sorted(A_list)
l = float("INF")
r = -float("INF")
for i in range(N):
    if A_list[i] != s_a_list[i]:
        l = min(i, l)
        r = max(i, r)

if l != float("INF") and r != -float("INF"):
    if r-l+1 <= K:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")