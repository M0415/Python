sum = 0
for i in range(8):
    A = input()
    
    if  i % 2 == 0:
        for j in 0, 2, 4, 6:
            if A[j] == 'F':
                sum += 1
    else:
        for j in 1, 3, 5, 7:
            if A[j] == 'F':
                sum += 1
print(sum) 
