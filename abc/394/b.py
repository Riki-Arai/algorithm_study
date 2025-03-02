N = int(input())
dic_ = {}
for i in range(N):
    S = input()
    dic_[len(S)] = S

dic_2 = sorted(dic_.items())
s = ''
for x in dic_2:
    s += x[1]
print(s)
