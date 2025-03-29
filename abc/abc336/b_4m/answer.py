N = int(input())

bin_n = bin(N)
res = 0
for i in bin_n[::-1]:
    if i == "0":
        res += 1
    else:
        print(res)
        exit()