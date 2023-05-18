P = list(map(int, input().split()))
A = list(map(int, input().split()))
count = 0
for i in range(4):
    if P[i] == A[0]:
        print(i+1)
        count += 1
if count == 0:
    print(0)