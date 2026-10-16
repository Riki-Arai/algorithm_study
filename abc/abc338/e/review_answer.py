'''
(1) 直線に置き換えて共通の区間判定も考えてはみたが、うまくはまらずに別の方法に・・・（公式ではこれを正式としていた）
(2) 右端か左端をソートして考えた方が良さそうなので区間スケジューリングの要領で右端でソート
(3) そして右端で一番右にあるもので、左端を区間に含むかどうかで判定をしていく
    →含んでいなければその弦は交差を含まないことを証明できたので、今後のノイズにならないように削除
    →そうしないと入力例2のような事例で間違った判定をしてしまう
(4) この問題でも片方を固める、右端でソートという着眼点が役には立ったが、公式解答も抑えておきたいところ
'''
#  SortedListは「key=lambda x: -x」で降順にできる。SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedList

N = int(input()) # 数値：1

st_lists = []
l_list = SortedList()
for _ in range(N):
    A, B = map(int, input().split()) # 取得例：1 2
    ab_list = sorted([A, B], reverse=True)
    st_lists.append(ab_list)
    l_list.add(ab_list[1])

st_lists.sort()
for r, l in st_lists:
    l_i = l_list.bisect_right(l)
    r_i = l_list.bisect_left(r)
    if r_i-l_i >= 1:
        print("Yes")
        exit()
    l_list.discard(l)

print("No")