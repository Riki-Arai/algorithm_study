min_x,min_y,max_x,max_y = 10**48,10**48,0,0

S = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            min_x = min(min_x,i)
            max_x = max(max_x,i)
            min_y = min(min_y,j)
            max_y = max(max_y,j)

print(min_x+1,max_x+1)
print(min_y+1,max_y+1)
