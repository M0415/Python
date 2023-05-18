h_1 = int(input())
h_2 = int(input())
h_3 = int(input())

j_1 = int(input())
j_2 = int(input())

h = 0
j = 0

if h_1 <= h_2 and h_1 <= h_3:
    h = h_1
elif h_2 <= h_1 and h_2 <= h_3:
    h = h_2
elif h_3 <= h_1 and h_3 <= h_2:
    h = h_3    
    
if j_1 <= j_2:
    j = j_1
else:
    j = j_2

print(h+j-50)