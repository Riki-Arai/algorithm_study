N = int(input())
a_list = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            res_1 = a_list[i][j]
            res_2 = a_list[j][i]
            if res_1 == "W" and res_2 == "W":
                print("incorrect")
                exit()
            if res_1 == "L" and res_2 == "L":
                print("incorrect")
                exit()
            if (res_1 == "D" and res_2 != "D") or (res_1 != "D" and res_2 == "D"):
                print("incorrect")
                exit()

print("correct")
