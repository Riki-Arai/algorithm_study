'''
※解けなかった
(1) https://programming-hiroba.com/abc371-e/ の解説にあるように余事象、種類数の合計という考え方がなかったので解けるわけがない
(2) しかし余事象を検討していたとしても、区間の種類数の合計を分解することができるという考え方はできそうになかったので、どちらにせよ厳しかったかも
(2) 数え上げでは余事象を考える、区間の種類数などでは分解することができるかも考慮してみると良さそう
'''
import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
N, M = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"
S, T = input().split() # 取得例："A" "B"
S_list = list(input()) # 取得例：["A","B"・・・]
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
A_list = input().split() # 取得例：["A","B","C"]、1行の入力用
A_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用
A_list = [int(input()) for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)
g_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力
input_lists = [list(map(int, list(input()))) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、12や34のようの連続文字列をint型に変換してリスト化
input_lists = [input().split() for _ in range(N)] # 取得例:[["A","B"], ["B",2]・・["F",6]]、2列の入力を型変換せずに取得
input_lists = [[s, int(x)] for s, x in (input().split() for _ in range(N))] # 取得例:[["A",1], ["B",2]・・["E",5]]
input_lists = [[int(x), s] for x, s in (input().split() for _ in range(N))] # 取得例:[[1,"A"], [2,"B"] ・・[5,"E"]]

import sys

A_lists = []
for i in sys.stdin:
    A_lists.append(i.strip())
