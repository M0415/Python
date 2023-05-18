N, K = map(int, input().split())
line = []
for i in range(1, N+1):
    ni = N % i
    if ni == 0:
        line.append(i)
for j in range(1, K):
    line.remove(min(line))
    if not line:
        line.append(0)
        break
print(line[0])