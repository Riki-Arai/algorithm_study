S = input().strip()

dir_list = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
print(dir_list[(dir_list.index(S)+4) % len(dir_list)])