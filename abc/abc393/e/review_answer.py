'''
(1) Aiが10**6まで、Aiを含めた時の最大の約数はAiとなる点にまずは着目
(2) また最大公約数なので約数を列挙することも必要そう、またそもそも最大公約数は約数のうちのどれかになる
(3) それぞれのaを約数に分解し、カウントをすると良さそうと気づき始める
(4) それぞれでカウントを行ったあとに、Aiの約数ごとにK以上あるかを調べてmaxになるものが答え(C++でACした)
(5) 今回からはGCDを見たら約数列挙を疑うことや要素の最大値に着目することが学べた
'''
N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

def get_all_divisors(n):
    # 各整数の約数を格納するリストを初期化
    divisors = [[] for _ in range(n + 1)]
    
    # 1からNまでの各整数iについて、その倍数にiを追加していく
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j].append(i)
            
    return divisors

max_a = max(A_list)
d_lists = get_all_divisors(max_a)
n2k_list = [0]*(max_a+1)
for a in A_list:
    for d in d_lists[a]:
        n2k_list[d] += 1

for a in A_list:
    res = 1
    for d in d_lists[a]:
        if n2k_list[d] >= K:
            res = max(d, res)
    print(res)