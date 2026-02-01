from collections import defaultdict, Counter, deque

a, N = map(int, input().split())

res = float("INF")
count = 0
res_set = set([1])
dq = deque()
dq.append([1, 0])
while len(dq):
    tmp_res, count = dq.popleft()
    if tmp_res == N:
        res = min(count, res)
    if len(str(tmp_res)) <= 6:
        for i in range(2):
            if i == 0:
                if tmp_res*a not in res_set:
                    dq.append([tmp_res*a, count+1])
                    res_set.add(tmp_res*a)
            else:
                if tmp_res >= 10 and tmp_res%10 != 0 and tmp_res//10+10**(len(str(tmp_res))-1)*int(str(tmp_res)[-1]) not in res_set:
                    dq.append([tmp_res//10+10**(len(str(tmp_res))-1)*int(str(tmp_res)[-1]), count+1])
                    res_set.add(tmp_res//10+10**(len(str(tmp_res))-1)*int(str(tmp_res)[-1]))

if res == float("INF"):
    print(-1)
else:
    print(res)