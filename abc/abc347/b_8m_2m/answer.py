S = input().strip()

n = len(S)
mi = 0
res_list = []
while mi < n:
    for i in range(n):
        res_list.append(S[i:i+1+mi])
    mi += 1

print(len(set(res_list)))