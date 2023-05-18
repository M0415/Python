import sys

while True:
   man, female = map(int, sys.stdin.readline().split())
   if man > 0 and female > 0:
       print(man + female)
   else:
       break