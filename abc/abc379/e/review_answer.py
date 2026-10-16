'''
(1) 二重ループだとTLEなので何かしらのテクニックで解く必要がある
(2) 例えば3、(7+30)、(9+70+300)のように分解をしてやると何かしらの法則性があることがわかる
(3) そこで最初は数値として等比数列を用いた解き方をしたがTLE
(4) 値が大きすぎることが原因なので文字列として扱う方針に切り替え、そこから過去の問題から筆算の解き方を考える
(5) 右から順番にリストに追加し、繰り上がりに気をつけることでACできた
(6) 数字が非常に大きくなるときでMODがない時は文字列で考えることが特に重要そう
    →愚直なコードでデバックをする作業もバグ発見にとても役に立った
'''
import sys; sys.setrecursionlimit(10**7)

N = int(input().strip())
S = input().strip() # 取得例："A"

sum_ = 0
for i, s in enumerate(S, 1):
    sum_ += int(s)*i

m, r = divmod(sum_, 10)
res_list = [str(r)]
for i in range(len(S)-1, 0, -1):
    sum_ -= (i+1)*int(S[i])
    m, r = divmod(sum_+m, 10)
    res_list.append(str(r))

if m != 0:
    res_list.append(str(m))

print("".join(res_list[::-1]))