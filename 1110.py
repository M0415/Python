N = int(input())
result = N
i = 0

while True:
    x = result // 10
    y = result % 10
    z = (x+y)%10
    result = (y*10)+z
    i += 1
    
    if N == result:
        break

print(i)    