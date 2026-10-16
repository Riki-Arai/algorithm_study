from collections import deque

N = int(input()) # 数値：1

res = 0
l = 1
dq = deque()
for r in range(2, N+1):
    dq.append(r)
    while len(dq):
        print(f"? {l} {r}", flush=True)
        ans = input().strip()
        if ans == "Yes":
            break
        l = dq.popleft()

    res += len(dq)

print(f"! {res}")