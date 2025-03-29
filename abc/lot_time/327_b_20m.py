a = int(input())
b = 1
while a >= b**b:
    if a == b**b:
        print(b)
        exit()
    b += 1
print(-1)