N = int(input())
S = input().strip()

res = ""
for i in range(len(S)):
    if i == 0:
        continue
    elif i - 1 >= 0 and S[i-1] == S[i]:
        continue
    else:
        res += S[i]

# 条件分岐では最後の1文字を考慮いしていなかったので+1しておく
print(len(res)+1)