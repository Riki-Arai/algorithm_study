N = int(input()) # 数値：1

for i in range(1, 10):
    for j in range(1, 10):
        if i*j == N:
            print("Yes")
            exit()

print("No")