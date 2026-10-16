from collections import defaultdict

N, M = map(int, input().split()) # 取得例：1 2

m2c_dict = defaultdict(int)
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    m2c_dict[abs(A+B)%N/2] += 1

p_c = 0
for v in m2c_dict.values():
    p_c += v*(v-1)//2

print(M*(M-1)//2-p_c)