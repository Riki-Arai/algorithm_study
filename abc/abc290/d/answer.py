import math

T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    K -= 1
    g = math.gcd(N, D)
    d = D//g
    n = N//g
    print((d*K)%n*g+K//n)