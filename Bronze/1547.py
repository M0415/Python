M = int(input())

min = [0, 1, 2, 3, 4]

for i in range(M):
    x, y = map(int, input().split())
    
    min[4] = min[x]
    min[x] = min[y]
    min[y] = min[4]
    
del min[4]

print(min.index(1))
