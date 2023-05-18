A = []
for i in range(3):
    B = input()
    A.append(B)

A[0] = int(A[0])
A[2] = int(A[2])

if A[1] == "+":
    print(A[0] + A[2])
elif A[1] == "*":
    print(A[0] * A[2])