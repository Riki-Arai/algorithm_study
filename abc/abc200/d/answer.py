'''
(1) 構築問題なのでDPの線をあまり考えなかったが、部分和の考え方を導入しなければACは難しそう
(2) 制約は200と小さく、さらに最大長200のリストを2つ管理すれば良いので計算量的に間に合いそう
(3) afterの200、5といったケースのみが通らなかったが、ひとまず自力ACしたことにする
'''
from collections import defaultdict, deque, Counter

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list = [a%200 for a in A_list]
m2list_dict = defaultdict(list)
dp_list = [False]*200
dp_list[0] = True
m2list_dict[0] = []
for i, a in enumerate(A_list, 1):
    # ★追加: 過去に余り0の非空部分列が見つかっていれば、要素iを組み合わせるだけで即解となる
    if len(m2list_dict[0]):
        print("Yes")
        print(1, i)
        c_list = m2list_dict[0] + [i]
        print(len(c_list), *c_list)
        exit()

    new_dp_list = dp_list.copy()
    for j in range(200):
        if dp_list[j]:
            aa = (j+a)%200
            src_list = [] if j == 0 else m2list_dict[j]
            if len(m2list_dict[aa]):
                print("Yes")
                b_list = m2list_dict[aa]
                print(len(b_list), *b_list)
                c_list = src_list.copy()
                c_list.append(i)
                print(len(c_list), *c_list)
                exit()

            new_dp_list[aa] = True
            tmp_list = src_list.copy()
            tmp_list.append(i)
            m2list_dict[aa] = tmp_list

    dp_list = new_dp_list.copy()

print("No")