line = list(map(int, input().split()))
line.sort

line_1 = line[0] + line[3]
line_2 = line[1] + line[2]
if line_1 >= line_2:
    total = line_1 - line_2
else:
    total = line_2 - line_1
print(total)