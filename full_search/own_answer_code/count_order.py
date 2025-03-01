import sys
from itertools import permutations

def solve():
    data = list(map(int, sys.stdin.read().split()))
    N = data[0]
    P = tuple(data[1:N+1])
    Q = tuple(data[N+1:2*N+1])
    
    #all_perms = sorted(permutations(range(1, N+1)))
    all_perms = list(permutations(range(1, N+1)))
    
    a = all_perms.index(P) + 1
    b = all_perms.index(Q) + 1
    
    # 差の絶対値を出力
    print(abs(a - b))

if __name__ == "__main__":
    solve()
