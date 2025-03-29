S = input()
T = input()

S_1, S_2 = S[0], S[1]
T_1, T_2 = T[0], T[1]
a_list = ["A", "B", "C", "D", "E"]

s1_idx = a_list.index(S_1)
s2_idx = a_list.index(S_2)
t1_idx = a_list.index(T_1)
t2_idx = a_list.index(T_2)
s_dis = min(abs(s1_idx-s2_idx), 5-(abs(s1_idx-s2_idx))) 
t_dis = min(abs(t1_idx-t2_idx), 5-(abs(t1_idx-t2_idx))) 

if s_dis == t_dis:
    print("Yes")
else:
    print("No")