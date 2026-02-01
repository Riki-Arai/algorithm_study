import heapq as hq

Q = int(input().strip())

for _ in range(Q):
    input_ = input()
    if input_.split()[0] == "1":
        q, x = input_.split()
        x = int(x)
    elif input_.split()[0] == "2":
        q, x = input_.split()
        x = int(x)
    else: