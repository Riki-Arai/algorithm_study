from collections import Counter

N = int(input())
S = input().strip()

cnt_s = Counter(S)
ans = 0
i = 0
while len(str(i * i)) <= N:
    sq = str(i * i).zfill(N)
    if Counter(sq) == cnt_s:
        ans += 1
    i += 1

print(ans)