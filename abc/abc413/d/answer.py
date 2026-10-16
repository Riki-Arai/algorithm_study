'''
(1) 値が少ないものから徐々に大きくなる数列を軸に考えると基本的に絶対値が低い順に並べると良い
(2) しかし値が全て同じ or -1をかけたもののみで構成している数列は別で考えると良い
(3) 数列の判定で割り算はあまり使うべきではなかった・・・（なるべく判定は整数同士にした方がいいことを改めて学んだ学んだ）
'''
from collections import Counter

T = int(input()) # 数値：1

for _ in range(T):
    N = int(input()) # 数値：1
    A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

    a2c_dict = Counter(A_list)
    s_a_list = sorted(A_list, key=lambda x: abs(x))
    if s_a_list[0]*-1 in a2c_dict:
        if a2c_dict[s_a_list[0]]+a2c_dict[s_a_list[0]*-1] == N and abs(a2c_dict[s_a_list[0]]-a2c_dict[s_a_list[0]*-1]) <= 1:
            print("Yes")
        else:
            print("No")
    elif a2c_dict[s_a_list[0]] == N:
        print("Yes")
    else:
        for i in range(1, N-1):
            if s_a_list[i]*s_a_list[i] != s_a_list[i-1]*s_a_list[i+1]:
                print("No")
                break
        else:
            print("Yes")