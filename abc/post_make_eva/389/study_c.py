heads = []
head = 0
tail_pos = 0

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heads.append(tail_pos)
        tail_pos += query[1]
    elif query[0] == 2:
        head += 1
    else:
        print(heads[head + query[1] - 1] - heads[head])

print(heads)
