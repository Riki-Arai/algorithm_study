n = int(input())
s = input()
t = input()
a = ['l','1']
b = ['0','o']
for i in range(n):
    if s[i] == t[i]:
        continue
    elif s[i] in a and t[i] in a:
        continue
    elif s[i] in b and t[i] in b:
        continue
    else:
        print('No')
        exit()
print('Yes')