N = int(input())
S = input().strip()

for i in range(N+1):
    if "A" in S[:i] and "B" in S[:i] and "C" in S[:i]:
        print(i)
        exit()