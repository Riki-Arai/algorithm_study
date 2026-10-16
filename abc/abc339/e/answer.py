'''
(1) bit全探索をできればいいが当然ながらTLE
(2) 手戻りがないのでDPを使用したいが、問題は情報をどのように管理するべきか
(3) 右端がAiの時の最大値を管理することを考えるが、Ai+1を起点としたD以内のものを全て探索しなければいけない
(4) なので最大値と最小値だけをすることも考えたが、これだけだと情報不足なので区間の情報が欲しい
(5) そこでネット調べたところSegTreeを使う手法があるらしく、これを使えば問題解決できることがわかった
(6) 綺麗に問題解決ができたのも良かったが、SegTreeのDPは使い所がありそうなのでぜひストックしておきたい 
'''
#  使用例：SegTree(定義した関数, 単位元, 対象のリスト) ※詳細：https://atcoder.github.io/ac-library/production/document_ja/segtree.html?utm_source=chatgpt.com
from atcoder.segtree import SegTree # 単位元→和：0、乗算：1、最大：-float('INF'), 最小：float('INF')、GCD：0、LCM：1、OR：0、XOR：0、AND：(1<<60)-1(bit数が不足していれば増やす)

N, D = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

def op(a, b):
    return max(a, b)

min_a, max_a = min(A_list), max(A_list)
n2l_list = [0]*(max_a+1)
seg_tree = SegTree(op, -float("INF"), n2l_list)
seg_tree.set(A_list[0], 1)
for a in A_list[1:]:
    l = seg_tree.prod(max(a-D, min_a), min(a+D, max_a)+1)
    seg_tree.set(a, l+1)

print(seg_tree.all_prod())