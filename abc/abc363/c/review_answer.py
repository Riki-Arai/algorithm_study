from more_itertools import distinct_permutations
N,K = map(int,input().split())
S = input()
ans = 0
for S in distinct_permutations(S):
    for i in range(N-K+1):
        for j in range(K):
            if S[i+j] != S[i+K-j-1]:
                break
        else:
            break
    else:
        ans += 1
print(ans)