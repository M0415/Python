N = int(input())
K = list(map(int, input().split()))
count = 0; sum = 0
for i in range(N):
    if K[i] == 1:
        count += 1
        sum += count
    else:
        count = 0
print(sum)