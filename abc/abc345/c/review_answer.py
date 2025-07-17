# 同じ文字列と入れ替える時は変化がなく、違う文字列だと変化があるのがポイント
from collections import defaultdict
S=input()
N=len(S)

ans=0
res_dict=defaultdict(int)
for j in range(N):
  ans+=j-res_dict[S[j]]  # i として選べるのは、j までの文字のうち S[j] と同じでないもの
  res_dict[S[j]]+=1
if max(res_dict.values())>1: # 重複して出現した文字列があるときは入れ替え時に同じ文字列になるパターンが存在する
  ans+=1 # その場合は入れ替えてもSとなるが、それも1種類としてカウント
print(ans)


## 以下は自分の回答
#S = input().strip()
#alp_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
#for s in S:
#    alp_dict[s] += 1
#
#res = 0
#sum_ = len(S)
#if max(list(alp_dict.values())) > 1:
#    res += 1
#
#for i, s in enumerate(list(S), 1):
#    n = alp_dict[s] - 1
#    res += sum_ - n - i
#    alp_dict[s] = n
#
#print(res)