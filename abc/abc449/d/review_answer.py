"""
※ACできず
(1) 縦*横の全探索ができればいいが計算量が多いので分離をすることまでは考えたが、点の数え上げ方を設計できず
(2) 担当の枠だけに着目して数え上げるという視点をもっと持つべきだった、無理に複雑な数え上げを考えすぎた
    → 範囲を指定しているところも惑わす要因になってしまった
    → 最初は範囲を気にせずに考えてみるべきだった（まずは簡単な状況から考えるのが大事）
(3) 担当の枠を決めて塗りつぶして確かめるなどをすると、もっと下のようなコードを作れたかも？
 
"""
L, R, D, U = map(int, input().split())

ans = 0

for i in range(L, R+1):
    if i % 2 == 0:
        low = max(D, -abs(i)+1)
        high = min(U, abs(i)-1)

        cnt = high-low+1
        ans += max(cnt, 0)
        # print(cnt)

for i in range(D, U+1):
    if i % 2 == 0:
        low = max(L, -abs(i))
        high = min(R, abs(i))

        cnt = high-low+1
        ans += max(cnt, 0)
        # print(cnt)

print(ans)