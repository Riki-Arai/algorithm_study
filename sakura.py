S = input().strip()

if len(set(list(S))) == 1:
    print("Weak")
    exit()

for i in range(3):
    x = int(S[i])
    n_x = int(S[i+1]) % 10
    if (x + 1) % 10 != n_x:
        print("Strong")
        exit()

print("Weak")
