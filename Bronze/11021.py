T = int(input())
sum = 0

for i in range(T):
    A, B = map(int, input().split())
    sum = A+B
    print("Case #{}: {}".format(i+1, sum))