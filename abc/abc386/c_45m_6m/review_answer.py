# secondの解き方もそこまで個人的にはごちゃついていないので、その回答方法でもよしとみなす
K = int(input())
S = list(input())
T = list(input())

for _ in range(2):
    while len(S) and len(T) and S[-1] == T[-1]:
        S.pop()
        T.pop()
    S = S[::-1]
    T = T[::-1]

if len(S) <= 1 and len(T) <= 1:
    print("Yes")
else:
    print("No")


## second
#K = int(input())
#S = input().strip()
#T = input().strip()
#
#if S == T:
#    print("Yes")
#    exit()
#
#count = 0
#if len(S) == len(T):
#    for i in range(len(S)):
#        if S[i] != T[i]:
#            count += 1
#        if count >= 2:
#            print("No")
#            exit()
#    print("Yes")
#elif abs(len(S) - len(T)) == 1:
#    if len(S) < len(T):
#        S, T = T, S
#    back_idx = 0
#    for i in range(len(S)):
#        if i < len(T) and S[i] != T[i-back_idx]:
#            count += 1
#            back_idx += 1
#        if count >= 2:
#            print("No")
#            exit()
#    print("Yes")
#else:
#    print("No")