A, B = map(int, input().split()) # 取得例：1 2

for i in range(1, 10000):
    a_i = (i*8)//100
    b_i = (i*10)//100
    if a_i == A and b_i == B:
        print(i)
        exit()

print(-1)