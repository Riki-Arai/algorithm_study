s_list = list(input())
rd_s_list = reversed(s_list)

print(int(len([(s,rs) for s, rs in zip(s_list, rd_s_list) if s != rs]) / 2))
