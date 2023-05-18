N = int(input())
max = 0
round = 0

for i in range(1, N+1):
    round += i
    max += 1
    if round > N:
        max -= 1
        break

print(max)