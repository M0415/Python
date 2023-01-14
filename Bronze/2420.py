N, M = map(int, input().split())
sum = N - M

if sum < 0:
    print(-sum)
else:
    print(sum)