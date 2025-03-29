S = input().strip()

l_count = [s.islower() for s in S].count(True)
u_count = [s.isupper() for s in S].count(True)
if l_count > u_count:
    print(S.lower())
else:
    print(S.upper())