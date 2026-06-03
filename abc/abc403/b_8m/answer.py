T = input().strip()
U = input().strip()

for i in range(len(T) - len(U) + 1):
    for j in range(len(U)):
        if T[i + j] != "?" and T[i + j] != U[j]:
            break
    else:
        print("Yes")
        exit()

print("No")