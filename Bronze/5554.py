time = []
time_total = 0
hour = 0

for i in range(4):
    time_in = int(input())
    time.append(time_in)
    
for j in range(4):
    time_total += time[j]
    
if time_total >= 60:
    hour = time_total // 60
    time_total = time_total % 60

print(hour)
print(time_total)