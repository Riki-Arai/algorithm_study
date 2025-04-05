S = input().strip()

if len(S) % 2 == 0 :
    for i in range(len(S)//2):
        if S[2*i] == S[2*i+1] and len(set(list(S))) == len(S) // 2:
            continue
        else:
            print("No")
            exit()
    print("Yes")
else:
    print("No")