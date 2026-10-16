'''
(1) DPも検討したが相性が良くなかったので言い換えをすることができないかを検討
(2) 操作を検証する中で-の数の偶奇に着目し、奇数の時に-が1つ残ることがわかった
(3) よって-の数が偶数のときはA_listの絶対値の合計、奇数は絶対値の合計-絶対値の最小値*2で導出
'''
N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

if [True for a in A_list if a < 0].count(True)%2 == 0:
    print(sum(list(map(abs, A_list))))
else:
    a_list = list(map(abs, A_list))
    print(sum(a_list)-2*min(a_list))