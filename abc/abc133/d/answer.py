'''
(1) 解説AC
(2) x1+x2=2A1、x2+x3=2A2・・・と置いてx1について求めようとするとx1=A1-A2+A3-A4・・・の構造となる
(3) よってfor文で偶数回と奇数回の時で加減してx1を導出すれば、残りは芋蔓式に求められる
'''
N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

x = 0
for i, a in enumerate(A_list):
    if i%2 == 0:
        x += a
    else:
        x -= a

res_list = []
for a in A_list:
    res_list.append(x)
    x = 2*a-x

print(*res_list)