import sys

K = list(map(int, sys.stdin.readline().split()))

price = K[0] * K[1]
need = K[2] - price

if need >= 0:
    print("0")
elif need < 0:
    print(-need)