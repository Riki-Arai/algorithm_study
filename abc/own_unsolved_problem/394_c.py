S = list(input())
i = 0

while i < len(S) - 1:
    if S[i] == 'W' and S[i + 1] == 'A':
        S[i] = 'A'
        S[i + 1] = 'C'
        i = max(0, i - 1)  # This can be removed for efficiency, as we no longer need to move back
    else:
        i += 1

result = ''.join(S)
print(result)

