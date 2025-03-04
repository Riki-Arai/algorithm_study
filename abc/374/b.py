S = list(input())
T = list(input())

if S == T:
    print(0)
else:
    if len(S) == len(T):
        count = 1
        for s, t in zip(S, T): 
            if s != t:
                print(count)
                break
            else:
                count += 1
    else:
        count = 1
        flag = False
        for s, t in zip(S, T): 
            if s != t:
                print(count)
                flag = True
                break
            else:
                count += 1

        if not flag:
            if len(S) > len(T):
                print(len(T) + 1)
            else:
                print(len(S) + 1)
