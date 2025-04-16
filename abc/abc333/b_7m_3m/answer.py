S = input()
T = input()

sorted_s = "".join(sorted(list(S)))
sorted_t = "".join(sorted(list(T)))
e_list = ["AB", "BC", "CD", "DE", "AE"]
if (sorted_s in e_list and sorted_t in e_list) or (sorted_s not in e_list and sorted_t not in e_list):
    print("Yes")
else:
    print("No")