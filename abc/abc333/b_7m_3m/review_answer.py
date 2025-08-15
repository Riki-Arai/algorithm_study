S = input()
T = input()

g_list = ["A", "B", "C", "D", "E"]
e_list = ["A", "E", "D", "C", "B"]
s_l = min(abs(g_list.index(S[0])-g_list.index(S[1])), abs(e_list.index(S[0])-e_list.index(S[1])))
t_l = min(abs(g_list.index(T[0])-g_list.index(T[1])), abs(e_list.index(T[0])-e_list.index(T[1])))

if s_l == t_l:
    print("Yes")
else:
    print("No")

# first
#S = input()
#T = input()
#
#S_1, S_2 = S[0], S[1]
#T_1, T_2 = T[0], T[1]
#a_list = ["A", "B", "C", "D", "E"]
#
#s1_idx = a_list.index(S_1)
#s2_idx = a_list.index(S_2)
#t1_idx = a_list.index(T_1)
#t2_idx = a_list.index(T_2)
#s_dis = min(abs(s1_idx-s2_idx), 5-(abs(s1_idx-s2_idx)))
#t_dis = min(abs(t1_idx-t2_idx), 5-(abs(t1_idx-t2_idx)))
#
#if s_dis == t_dis:
#    print("Yes")
#else:
#    print("No")