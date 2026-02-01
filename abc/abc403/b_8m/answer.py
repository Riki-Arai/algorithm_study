T = input().strip() # 取得例："A"
U = input().strip() # 取得例："A"

for i in range(len(T)-len(U)+1):
    for j in range(len(U)):
        if T[i+j] != "?" and T[i+j] != U[j]:
            break
    else:
        print("Yes")
        exit()

print("No")