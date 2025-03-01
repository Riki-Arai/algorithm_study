import itertools

N = int(input())
pos_list = []
for _ in range(N):
    pos_list.append(list(map(int, input().split())))

town_list = [n for n in range(N)]
route_list = list(itertools.permutations(town_list, N))

dis_list = []
for route in route_list:
    dis = 0
    for i in range(len(route)):
        if i + 1 == len(route):
            break
        dis += pow(pow(pos_list[route[i]][0] - pos_list[route[i+1]][0], 2) + pow(pos_list[route[i]][1] - pos_list[route[i+1]][1], 2), 0.5)
    dis_list.append(dis)

print(sum(dis_list) / len(dis_list))
