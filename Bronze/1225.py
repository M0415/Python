A, B = (input().split())
total = 0; sum = 0
for i in range(len(B)):
    total += int(B[i])
for j in range(len(A)):
    sum += int(A[j]) * total
print(sum)    