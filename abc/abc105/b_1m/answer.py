import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

for i in range(100):
    for j in range(100):
        if i*4+j*7 == N:
            print("Yes")
            exit()

print("No")