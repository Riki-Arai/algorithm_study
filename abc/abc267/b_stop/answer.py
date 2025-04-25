S = input().strip()

pin_list = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
stand_list = [False] * 7

if S[0] == "1":
    print("No")
    exit()

for i, s in enumerate(list(S)):
    if s == "1":
        stand_list[pin_list[i]-1] = True

for i in range(7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            if stand_list[i] and not stand_list[j] and stand_list[k]:
                print("Yes")
                exit()

print("No")