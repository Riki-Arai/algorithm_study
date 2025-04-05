N = int(input())
S = input().strip()

if N % 2 != 0:
    if S[:(N+1)//2-1] == "1" * ((N+1)//2-1) and S[(N+1)//2-1] == "/" and S[(N+1)//2:] == "2" * (N-((N+1)//2)): 
        print("Yes")
    else:
        print("No")
else:
    print("No")