S = input().strip()

s_n = S[::-1]
res = 0
for i in range(len(s_n)):
    n = (int(s_n[i])-res)%10
    res += n

print(res+len(s_n))