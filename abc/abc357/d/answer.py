N = int(input())
A, B = input().split()
A, B = map(int, input().split())
N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用
A_list = [int(input()) for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用(int型に変換)
A_lists = [list(input().split()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
S = input().strip()
S_list = list(input())

import sys

A_list = []
for i in sys.stdin:
    A_list.append(i)
