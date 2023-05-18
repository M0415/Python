N = int(input())
N_number = list(map(int, input().split()))
min = 1000000
max = -1000000

for i in range(N):
    if N_number[i] < min:
        min = N_number[i]

for j in range(N):
    if N_number[j] > max:
        max = N_number[j]
        
print(min, max)        