a, b = map(int, input().split())
total = a*b
x = list(map(int, input().split()))

for i in range(5):
    x[i] -= total
    print(x[i],end=" ")