N = int(input())

res_list = []
while N != 0:
    if N % 2 == 0:
        N //= 2
        res_list.append("B")
    else:
        N -= 1
        res_list.append("A")

print("".join(res_list[::-1]))