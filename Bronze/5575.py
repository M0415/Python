A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

if A[5] < A[2]:
    A[4] -= 1
    sec_A = (A[5]+60) - A[2]
else:
    sec_A = A[5] - A[2]

if A[4] < A[1]:
    A[3] -= 1
    min_A = (A[4]+60) - A[1]
else:
    min_A = A[4] - A[1]
hour_A = A[3] - A[0]

if B[5] < B[2]:
    B[4] -= 1
    sec_B = (B[5]+60) - B[2]
else:
    sec_B = B[5] - B[2]

if B[4] < B[1]:
    B[3] -= 1
    min_B = (B[4]+60) - B[1]
else:
    min_B = B[4] - B[1]
hour_B = B[3] - B[0]

if C[5] < C[2]:
    C[4] -= 1
    sec_C = (C[5]+60) - C[2]
else:
    sec_C = C[5] - C[2]

if C[4] < C[1]:
    C[3] -= 1
    min_C = (C[4]+60) - C[1]
else:
    min_C = C[4] - C[1]
hour_C = C[3] - C[0]

print(hour_A, min_A, sec_A)
print(hour_B, min_B, sec_B)
print(hour_C, min_C, sec_C)