import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"
Q = int(input())

t_set, a_set = set(S), set(T)
for _ in range(Q):
    w = input().strip() # 取得例："A"
    w_set = set(w)
    if w_set <= t_set and not(w_set <= a_set):
        print("Takahashi")
    elif not(w_set <= t_set) and w_set <= a_set:
        print("Aoki")
    else:
        print("Unknown")