N = int(input())
num = [input() for i in range(N)]
num.sort()
coun = []
for j in range(N):
    coun.append(num[j][0])
k = []
count = 1
for j in range(N-1):
    if coun[j] == coun[j+1]:
        count += 1
        if count == 5:
           k.append(coun[j])
           count = 1
    else:
        count = 1
if len(k) == 0:
    print('PREDAJA')
else:
    k = list(set(k))
    k.sort()
    k =''.join(k)
    print(k)