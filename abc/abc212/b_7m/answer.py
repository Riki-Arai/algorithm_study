X_list = list(input())

if len(set(X_list)) == 1:
    print("Weak")
    exit()

res = 0
for i in range(3):
    if (int(X_list[i])+1)%10 == int(X_list[i+1]):
        res += 1

if res == 3:
    print("Weak")
else:
    print("Strong")