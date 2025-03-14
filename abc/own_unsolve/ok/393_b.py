S = input()

#a_index = [i for i, x in enumerate(S) if x == 'A']
#b_index = [i for i, x in enumerate(S) if x == 'B']
#c_index = [i for i, x in enumerate(S) if x == 'C']
a_index, b_index, c_index = [], [], []
for i, x in enumerate(S, 1):
    if x == 'A':
        a_index.append(i)
    elif x == 'B':
        b_index.append(i)
    elif x == 'C':
        c_index.append(i)

res = 0
for i in a_index:
    for j in b_index:
        if j > i:
            ab_diff = j - i
            if j + ab_diff in c_index:
                res += 1

print(res)
