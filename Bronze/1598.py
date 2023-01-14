A, B = map(int, input().split())
# 좌표 1,1 로 설정하기 위해 값들에 -1를 한다
A -= 1
B -= 1
length_A = A % 4
Transverse_A = (A // 4)
length_B = B % 4
Transverse_B = (B // 4)
  
if length_A > length_B:
    length = length_A - length_B
else:
    length = length_B - length_A
    
if Transverse_A > Transverse_B:
    Transverse = Transverse_A - Transverse_B
else:
    Transverse = Transverse_B - Transverse_A
    
sum = length + Transverse
print(sum)