'''
(1) 最小値+最大値 or 最大値の2通りのみ
(2) 最小値+最大値のケースではリストが偶数であり、かつ対応する端を比較したときに全てが最小値+最大値になるかを確認すればいい
(3) 最大値の場合は最大値を除去したあとに(2)と同じような確認をしていけばいい
'''
N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()
res_list = []
if len(A_list)%2 == 0:
    for i in range(len(A_list)//2):
        if i == 0:
            base = A_list[i]+A_list[-1]
        elif i != 0:
            if not(base == A_list[i]+A_list[-i-1]):
                break
    else:
        res_list.append(base)

max_a = max(A_list)
while len(A_list) and A_list[-1] == max_a:
    A_list.pop()

if len(A_list)%2 == 0:
    for i in range(len(A_list)//2):
        if not(max_a == A_list[i]+A_list[-i-1]):
            break
    else:
        res_list.append(max_a)

print(*sorted(res_list))