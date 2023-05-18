import sys
N = sys.stdin.readline().rstrip(); F = int(sys.stdin.readline())
N_1 = list("".join(reversed(N))); del N_1[0:2]; N_1.reverse()
N_2 = "".join(N_1)
N = int(N_2 + '00')
count = 0

while True:
    if (N%F) != 0:
        N += 1
        count += 1
    else:
        break
if count < 10:
    count = '0' + str(count)
    print(count)
else:
    print(count) 