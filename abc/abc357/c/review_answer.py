N = int(input().strip())

s = ["#"]
for _ in range(N):
    m = len(s)
    m3 = m * 3
    # m3 x m3 の'.'埋め2次元リストを作成するが、[list('.' * m3)]*3だと浅いコピーになるので注意
    t = [list('.' * m3) for _ in range(m3)]
    # sのパターンをタイル状に t にコピー
    for i in range(m3):
        for j in range(m3):
            # %を用いることでiやjがある地点からsにおける0のインデックスになってくれる。タイル模様などの書き換えでよくあるパターン。
            t[i][j] = s[i % m][j % m]
    # for文を用いて書き換えたい時の定型的なコード
    # 1*1パーツであれば1回のループで(1,1)を書き換え
    # 3*3=9パーツであれば9パーつごとの担当部分を書き換える
    for i in range(m):
        for j in range(m):
            t[m + i][m + j] = '.'

    s = [''.join(row) for row in t]

for line in s:
    print(line)