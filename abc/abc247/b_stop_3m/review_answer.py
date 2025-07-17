N = int(input())
A_lists = [input().split() for _ in range(N)]

for i, A_list in enumerate(A_lists):
    s, t = A_list
    a_flag, b_flag = False, False
    for j, B_list in enumerate(A_lists):
        if i != j:
            ss, tt = B_list
            if (s == ss or s == tt):
                a_flag = True
            if (t == ss or t == tt):
                b_flag = True

    if a_flag and b_flag:
        print("No")
        exit()

print("Yes")

#N=int(input())
#
#s=[""]*N; t=[""]*N
#for i in range(N):
#    s[i],t[i]=input().split()
#
#Ans=1
#for i in range(N):
#    f=g=1
#    for j in range(N):
#        if i==j:
#            continue
#        if s[i]==s[j] or s[i]==t[j]:
#            f=0
#        if t[i]==s[j] or t[i]==t[j]:
#            g=0
#    if f==g==0:
#        Ans=0
#        break
#
#print("Yes" if Ans else "No")
#