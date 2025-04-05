N = int(input())

res = ""
div_list = [i for i in range(1, N+1) if N % i ==0]
for num in range(N+1):
    flag = True
    for x in div_list:
        if 1 <= x <= 9 and num % (N / x) == 0:
            res += str(x)
            flag = False
            break
    if flag:
        res += "-"

print(res)