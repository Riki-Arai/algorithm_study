'''
(1) ポーションを拾うべきかどうかはモンスターがどのように出現するかで決まるのでクエリの先読みが必要
(2) しかしモンスターが未来でどのように出現をするかを把握しても、それに合わせてポーションを管理することは大変
    →ポーションとモンスターの出現位置を適切に把握していないと、すぐにバグが起きたりしそう・・・
(3) そこでもう少し見方を変えて、未来から逆に遡ることを考えて出現済みのモンスターの種類と数に合わせて必要な分だけのポーションを拾うことで対応
(4) 未来の情報から現在の行動を決めるケースは後ろから解いてみるアイディアを持つようにしたい
'''
import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

input_lists.reverse()
n2c_list = [0]*(2*10**5+1)
res, tmp_res = 0, 0
res_list = []
for t, x in input_lists:
    if t == 1:
        if n2c_list[x]:
            res_list.append(1)
            n2c_list[x] -= 1
            tmp_res -= 1
        else:
            res_list.append(0)
    else:
        n2c_list[x] += 1
        tmp_res += 1

    res = max(tmp_res, res)

if max(n2c_list) >= 1:
    print(-1)
else:
    print(res)
    print(*reversed(res_list))