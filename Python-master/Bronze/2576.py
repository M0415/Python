x = []
sum = 0
for i in range(7):
    y = int(input())
    if (y / 2) != (y // 2):
        x.append(y)
if len(x) == 0:
    print(-1)
else:
    for i in range(len(x)):
        sum += x[i]
    x.sort()
    print(sum, x[0], sep='\n')