X = input().strip()

if len(set(X)) == 1:
    print("Weak")
    exit()

count = 0
for i in range(3):
    if (int(X[i]) + 1) % 10 == int(X[i+1]):
        count += 1
    if count == 3:
        print("Weak")
        exit()

print("Strong")