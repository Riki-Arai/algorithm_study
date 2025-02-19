N = int(input())

flag = False
for x in range(1, 10):
    if flag:
        break
    for y in range(1, 10):
        if x * y == N:
            print("Yes")
            flag = True
            break

if not flag:
    print("No")
