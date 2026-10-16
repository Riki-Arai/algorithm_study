import sys; sys.setrecursionlimit(10**7)

H, W, K = map(int, input().split()) # 取得例：1 2
S_lists = [list(map(int, list(input()))) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]、12や34のようの連続文字列をint型に変換してリスト化