N = int(input())

h = N // 3600
m = (N - 3600*h) // 60
s = N - h*3600 - m*60

str_h = str(h)
str_m = str(m)
str_s = str(s)
if h < 10:
    str_h = "0" + str_h
if m < 10:
    str_m = "0" + str_m
if s < 10:
    str_s = "0" + str_s

print(str_h+":"+str_m+":"+str_s)