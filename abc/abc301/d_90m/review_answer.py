S = input().strip()
N = int(input())

max_v, min_v = 0, 0
for i, s in enumerate(S[::-1]):
    if s == "?":
        max_v += 2**i
    elif s == "1":
        max_v += 2**i
        min_v += 2**i

if max_v <= N:
    print(max_v)
elif min_v > N:
    print(-1)
    exit()
else:
    rev_s = S[::-1]
    rem = N - min_v
    add = 0
    for i in range(len(S)-1, -1, -1):
        s = rev_s[i]
        if s == "?" and rem >= 2**i:
            add += 2**i
            rem -= 2**i
    print(min_v+add)