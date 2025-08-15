N = int(input())

res = 0
d = len(str(N))
for i in range(d-1):
    res += (1 + int("9"*(i+1))) * int("9"*(i+1)) // 2

N -= 10**(d-1)
print(res + ((1+N+1)*(N+1))//2)