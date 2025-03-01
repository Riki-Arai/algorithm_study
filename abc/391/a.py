A_list = list(map(int,input().split()))

count = 0
correct_list = [1, 2, 3, 4, 5]
idx_list = []
for idx in range(len(A_list)):
    if correct_list[idx] != A_list[idx]:
        count += 1
        idx_list.append(idx)

if count == 2 and idx_list[1] - idx_list[0] == 1:
    print("Yes")
else:
    print("No")
