import collections

s = list(input())
s.sort()
ans = collections.Counter(s)
ans = ans.most_common()

print(ans[0][0])