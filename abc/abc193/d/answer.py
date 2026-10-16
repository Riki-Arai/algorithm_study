from collections import Counter

K = int(input()) # 数値
S = input().strip() # 文字列
T = input().strip() # 文字列

rem_list = [K]*10
for k, v in Counter(S[:-1]+T[:-1]).items():
    rem_list[int(k)] -= int(v)

mol = 0
den = 0
for s in range(1, 10):
    c_rem_list = rem_list.copy()
    if c_rem_list[s] > 0:
        c_rem_list[s] -= 1
        s_c2n_dict = Counter(map(int, list(S[:-1]+str(s))))
        s_score = sum([i*10**s_c2n_dict[i] if i in s_c2n_dict else i for i in range(1, 10)])
        for t in range(1, 10):
            if c_rem_list[t] > 0:
                t_c2n_dict = Counter(map(int, list(T[:-1]+str(t))))
                t_score = sum([i*10**t_c2n_dict[i] if i in t_c2n_dict else i for i in range(1, 10)])
                if s == t:
                    pat = (rem_list[s]*(rem_list[s]-1))
                    if s_score > t_score:
                        mol += pat
                    den += pat
                else:
                    pat = rem_list[s]*rem_list[t]
                    if s_score > t_score:
                        mol += pat
                    den += pat

print(mol/den)