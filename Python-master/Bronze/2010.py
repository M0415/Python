import sys
N = int(input())
plug = 0
for i in range(N):
    plug += int(sys.stdin.readline())
    
total = plug - (N - 1)
print(total)