'''
(1) ソートは必要だが毎回はできないので、1つの追加と削除を通じてソートする形を採用する
(2) また毎回K個取得して合計を取る形はTLEになるので1つのクエリごとに合計を持つようにする
(3) 更新が発生するパターンは最低値が入れ替わる、最低値は同じだが同じインデックスで値が入れ替わるケースあたりか
(4) 最低値を境目として(3)の観点で条件分岐をすれば解けそう
(5) 今回の問題はナイーブな実装で検証をできたのでいくつかのテストケースを作成し、照らし合わせることでデバッグができた
(6) 毎回ソートをして追加・削除をするときはSortedList、K個を注目するのではなく1個の変化に着目、ナイーブな実装でデバッグを学べた
'''
#  SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedList

N, K, Q = map(int, input().split()) # 取得例：1 2

A_list = [0]*N
x_set = set()
res = 0
b_list = SortedList([0]*N, key=lambda x: -x)
K -= 1
for _ in range(Q):
    X, Y = map(int, input().split()) # 取得例：1 2
    X -= 1
    if len(x_set) >= K:
        min_b = b_list[K]
        if A_list[X] >= min_b:
            if Y >= min_b:
                res -= A_list[X]
                b_list.remove(A_list[X])
                b_list.add(Y)
                res += Y
            else:
                res -= A_list[X]
                b_list.remove(A_list[X])
                b_list.add(Y)
                res += b_list[K]
        else:
            if Y >= min_b:
                res -= min_b
                b_list.remove(A_list[X])
                b_list.add(Y)
                res += Y
            else:
                b_list.remove(A_list[X])
                b_list.add(Y)
    else:
        if X in x_set:
            res -= A_list[X]
            res += Y
        else:
            res += Y
        b_list.remove(A_list[X])
        b_list.add(Y)

    A_list[X] = Y
    x_set.add(X)
    print(res)