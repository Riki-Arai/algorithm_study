S = input().strip()

res = 0
for s in range(1, len(S)+1):
    tmp_res = 0
    for i in range(len(S)):
        if S[i:i+s] == S[i:i+s][::-1]:
            tmp_res = max(len(S[i:i+s]), tmp_res)

    res = max(tmp_res, res)

print(res)