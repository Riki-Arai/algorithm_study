'''
※解説AC
できなかった原因
(1) 余事象に気づくまでは良かったが、余りを取るという発想には至らず
(2) 例えば(A+B)//2 MOD 1//2のような方法でも一致するらしい
(3) 直線であれば中点が一致するものを集計すればいいが、円にまつわる問題なのでその時は余りを取るという発想が大事だと学んだ
'''
from collections import defaultdict

N, M = map(int, input().split()) # 取得例：1 2

m2c_dict = defaultdict(int)
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    m2c_dict[abs(A+B)%N] += 1

res = M*(M-1)//2
for k, v in m2c_dict.items():
    res -= v*(v-1)//2

print(res)