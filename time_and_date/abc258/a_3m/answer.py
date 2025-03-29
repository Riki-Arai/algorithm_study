K = int(input())
h = K // 60
m = K % 60

str_m = str(m)
if 0 <= m < 10:
    str_m = "0" + str(m)

print(str(21+h)+":"+str_m)