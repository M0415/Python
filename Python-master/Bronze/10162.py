import sys
A = 0
B = 0
C = 0

time = int(sys.stdin.readline())
# A = 5분  B = 1분  C = 10초
if time >= 300:
       A = time // 300
       time = time % 300
       
if time >= 60:
        B = time // 60
        time = time % 60
        
if time >= 10:
        C = time // 10
        time = time % 10 
    
if time > 0:
    print(-1)
else:
    print(A, B, C)
    
