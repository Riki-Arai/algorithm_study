N = int(input()) # 数値

if len(str(N)) < 4:
    print(0)
    exit()

res = 0
if int(str(9)*3*2) < N:
    res += int(str(9)*3*2)-10**3+1
else:
    print(N-10**3+1)
    exit()

if int(str(9)*3*3) < N:
    res += 2*(int(str(9)*3*3)-10**6+1)
else:
    print(res+2*(N-10**6+1))
    exit()

if int(str(9)*3*4) < N:
    res += 3*(int(str(9)*3*4)-10**9+1)
else:
    print(res+3*(N-10**9+1))
    exit()
if int(str(9)*3*5) < N:
    res += 4*(int(str(9)*3*5)-10**12+1)
else:
    print(res+4*(N-10**12+1))
    exit()

res += 5
print(res)