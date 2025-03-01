S = input( )

a_index_list, b_index_list, c_index_list = [], [], []
for i, x in enumerate(S, 1):
    if x == 'A':
        a_index_list.append(i)
    elif x == 'B':
        b_index_list.append(i)
    elif x == 'C':
        c_index_list.append(i)

count = 0
for i in a_index_list:
    for j in b_index_list:
        for k in c_index_list:
            if j - i == k - j and i < j and j < k:
                count += 1
print(count)
