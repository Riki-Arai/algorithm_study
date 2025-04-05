S = input().strip()

if len(S) % 2 == 0 :
    for i in range(len(S)//2):
        if 2*i < len(S) and 2*i-1 < len(S) and S[2*i] == S[2*i-1] and S.count("0") == 2 and S.count("2") == 2:
            print("Yes")
    print("No")
            
else:
    print("No")