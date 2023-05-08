def find(a,b):
    if a <= b:
        return a
    else:
        return b
line = list(map(int,input().split())); line.sort()
a_line = find(line[0], line[1])
b_line = find(line[2], line[3])
    
total = a_line * b_line
print(total)    