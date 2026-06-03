a, b, C = map(int,input().split())

x = 0
y = 0
i_list = []
for i in range(60):
    if C >> i & 1:
        if a == 0 and b == 0:
            print(-1)
            exit()
        elif a > b:
            a -= 1
            x += 2**i
        else:
            b -= 1
            y += 2**i
    else:
        i_list.append(i)

if a != b:
    print(-1)
    exit()

if len(i_list) < a:
    print(-1)
    exit()

for j in range(a):
    i = i_list[j]
    x += 2**i
    y += 2**i

print(x, y)