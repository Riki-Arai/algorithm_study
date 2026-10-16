N, Q = map(int, input().split())

parent = [0]
current = [0] * (N + 1)
add = [""]
for _ in range(Q):
    q = list(map(str, input().split()))

    if q[0] == "1":
        p = int(q[1])
        current[p] = current[0]
    elif q[0] == "2":
        p = int(q[1])
        c = q[2]
        parent.append(current[p])
        add.append(c)
        current[p] = len(add) - 1
    else:
        p = int(q[1])
        current[0] = current[p]

ans = []
cur = current[0]
while cur != 0:
    ans.append(add[cur])
    cur = parent[cur]

print("".join(ans[::-1]))
