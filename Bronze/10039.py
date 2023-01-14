import sys
result = 0

for i in range(5):
    student = int(sys.stdin.readline())
    
    if student <=40:
        student = 40
    
    result += student
    
print(result // 5)