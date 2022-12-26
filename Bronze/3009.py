A = []
for i in range(3):
    B = input().split()
    A.append(B)

C, D = 0, 0
if A[0][0] == A[1][0]:
    C = A[2][0]
elif A[0][0] == A[2][0]:
    C = A[1][0]
elif A[1][0] == A[2][0]:
    C = A[0][0]
    
if A[0][1] == A[1][1]:
    D = A[2][1]
elif A[0][1] == A[2][1]:
    D = A[1][1]
elif A[1][1] == A[2][1]:
    D = A[0][1]

print(C, D,end = " ")