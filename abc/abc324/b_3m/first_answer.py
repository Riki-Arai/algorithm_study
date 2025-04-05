N = int(input())

two_list = [2 ** i for i in range(61)]
three_list = [3 ** i for i in range(41)]

for x in two_list:
    for y in three_list:
        if x * y == N:
            print("Yes")
            exit()

print("No")