#  周期性を利用して解く問題
N, M = map(int, input().split())

MOD = 998244353
bin_m = bin(M)[2:][::-1]
res = 0
for i, b in enumerate(bin_m):
    if b == "1" and N >= 2**i:
        # i bit目が 1 になる最初の位置を導出するために2**iを引いている
        m, r = divmod((N+1)-2**i, 2**(i+1))
        #  1の数は2**(i+1)の半分以下なので最大でも2**iでなければいけない
        res = (res + m*2**i + min(r, 2**i))%MOD

print(res%MOD)