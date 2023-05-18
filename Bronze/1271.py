import sys
n, m = map(int, sys.stdin.readline().split())

money = n // m
now = n % m

print(money)
print(now)

