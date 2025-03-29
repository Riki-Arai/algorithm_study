S = input().strip()

i = 0
res = 0
while i < len(S):
    res_list = []
    for j in range(len(S)-i):
        res_list.append(S[j:j+i+1])
    res += len(set(res_list))
    i += 1

print(res)