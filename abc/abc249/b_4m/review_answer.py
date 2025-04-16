s = input()
if s == s.upper():
    print("No")
    exit()
if s == s.lower():
    print("No")
    exit()
if len(s) != len(set(list(s))):
    print("No")
    exit()
print("Yes")

## first
#S = input().strip()
#
#if len(S) != len(set(list(S))):
#    print("No")
#    exit()
#
#u_flag, l_flag = False, False
#for s in S:
#    if s.isupper():
#        u_flag = True
#
#    if s.islower():
#        l_flag = True
#
#if u_flag and l_flag:
#    print("Yes")
#else:
#    print("No")