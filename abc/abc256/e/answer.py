#import heapq as hq

N = int(input())
X_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

#e_list = [0]*(N+1)
#for x in X_list:
#    e_list[x] += 1
#
#hq_list = []
#for i in range(N):
#    hq_list.append((e_list[i+1], -C_list[i], i+1))
#
#hq.heapify(hq_list)
#p_list = []
#seen_set = set()
#while len(hq_list):
#    _, _, i = hq.heappop(hq_list)
#    #_, i = hq.heappop(hq_list)
#    if i not in seen_set:
#        p_list.append(i)
#        seen_set.add(i)
#        e_list[X_list[i-1]] -= 1
#        hq.heappush(hq_list, (e_list[X_list[i-1]], -C_list[X_list[i-1]-1], X_list[i-1]))
#
#res = 0
#seen_set = set()
#for p in p_list:
#    if X_list[p-1] in seen_set:
#        res += C_list[p-1]
#    seen_set.add(p)
#
#print(res)