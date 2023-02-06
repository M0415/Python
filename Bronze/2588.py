x = int(input()); y = list(input()); y.reverse()
sum = 0
for i in range(3):
    to = x*int(y[i])
    print(to)
    sum += to * (10**i)
print(sum)