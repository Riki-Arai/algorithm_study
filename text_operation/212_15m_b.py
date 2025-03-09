x_list = list(map(int, list(input())))

def solve():
    if len(set(x_list)) == 1:
        return "Weak"
    count = 0
    for i in range(0, len(x_list)-1, 1):
        if (x_list[i] + 1 == x_list[i+1]) or (x_list[i] == 9 and x_list[i+1] == 0):
            count += 1
    if count == 3:
        return "Weak"
    else:
        return "Strong"

print(solve())
