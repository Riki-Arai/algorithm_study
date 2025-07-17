X_list = list(input())

if len(set(X_list)) == 1:
    print("Weak")
    exit()
else:
    for i in range(len(X_list)-1):
        if (int(X_list[i]) + 1)%10 != int(X_list[i+1]):
            print("Strong")
            exit()
    print("Weak")