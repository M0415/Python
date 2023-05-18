hour, min, sec = map(int, input().split())
D = int(input())
sec += D

while sec >= 60:
    if sec >= 60:
        sec -= 60
        min += 1

while min >= 60:
    if min >= 60:
        min -= 60
        hour += 1

while hour >=24:
    if hour >= 24:
        hour -= 24

print(hour, min, sec)