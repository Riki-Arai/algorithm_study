N = int(input()) # 数値
S = input().strip() # 文字列
T = input().strip() # 文字列
S_list = list(input())
A, B = input().split()
S, T = input().split()
A, B = map(int, input().split())
N, M = map(int, input().split())
N, K = map(int, input().split())
N, Q = map(int, input().split())
S, T = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
A_list = input().split() # 取得例：["a","b","c"]、1行の入力用
A_list = [input() for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用
A_list = [int(input()) for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
A_lists = [input().split() for _ in range(N)] # 取得例:[["A","B"], ["B",2]・・["F",6]]、2列の入力を型変換せずに取得
A_lists = [[s, int(x)] for s, x in (input().split() for _ in range(N))] # 取得例:[["A",1], ["B",2]・・["E",5]]
A_lists = [[int(x), s] for x, s in (input().split() for _ in range(N))] # 取得例:[[1,"A"], [2,"B"] ・・[5,"E"]]

import sys

A_list = []
for i in sys.stdin:
    A_list.append(i)
