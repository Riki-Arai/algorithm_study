A, B = list(map(int, input().split()))

if B % 3 == 0:
    if B - 1 == A or B - 2 == A:
        print("Yes")
        exit()
elif B % 3 == 2:
    if B - 1 == A:
        print("Yes")
        exit()

print("No")
