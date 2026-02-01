N = int(input())

m = 3**N
g_lists = [["#"]*3**N for _ in range(3**N)]
for k in range(N):
    for i in range(3**N):
        for j in range(3**N):
            ii = i//(3**k)
            jj = j//(3**k)
            if ii%3 == 1 and jj%3 == 1:
                g_lists[i][j] = "."


for g_list in g_lists:
    print("".join(g_list))

N = int(input())

grid = [["#"]*(3**N) for _ in range(3**N)]
for k in range(N):
    for i in range(3**N):
        for j in range(3**N):
            # (3**k)のブロックで割ることで新しくマッピングしたidxを与える
            # k=0であればマッピングは特にせずに通常のiとjとして扱い、iとjで%3することで9分割するイメージ
            # k=1であれば3~5は全て1になるので同じ扱いにすることができる
            if ((i // (3**k))%3 == 1) and ((j // (3**k))%3 == 1):
                grid[i][j] = "."

for g in grid:
    print("".join(g))

# 以下はわかりにくいいので参考程度
#N = int(input().strip())
#
#s = ["#"]
#for _ in range(N):
#    m = len(s)
#    m3 = m * 3
#    # m3 x m3 の'.'埋め2次元リストを作成するが、[list('.' * m3)]*3だと浅いコピーになるので注意
#    t = [list('.' * m3) for _ in range(m3)]
#    # sのパターンをタイル状に t にコピー
#    for i in range(m3):
#        for j in range(m3):
#            # %を用いることでiやjがある地点からsにおける0のインデックスになってくれる。タイル模様などの書き換えでよくあるパターン。
#            t[i][j] = s[i % m][j % m]
#    # for文を用いて書き換えたい時の定型的なコード
#    # 1*1パーツであれば1回のループで(1,1)を書き換え
#    # 3*3=9パーツであれば9パーつごとの担当部分を書き換える
#    for i in range(m):
#        for j in range(m):
#            t[m + i][m + j] = '.'
#
#    s = [''.join(row) for row in t]
#
#for line in s:
#    print(line)