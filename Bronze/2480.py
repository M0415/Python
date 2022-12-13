x, y, z = map(int, input().split())
result = 0

#세 수가 같을 때
if (x == y) and (x == z): 
   result = 10000 + (x*1000)
     
# 두 수가 같고 나머지 하나가 다를 때 , if문에서 \로 단 변화할 시 해당하는 행에 주석추가 불가
elif (x == y) or \
     (x == z) or \
     (y == z):
         if (x == y):
             result = 1000 + (x*100)
         elif (x == z):
             result = 1000 + (x*100)
         elif (y == z):
             result = 1000 + (y*100)
# 세 수가 모두 다를 때             
elif (x != y) and \
     (x != z) and \
     (y != z):
         if (x>y) and (x>z):
             result = (x*100)
         elif (y>x) and (y>z):
             result = (y*100)
         elif (z>x) and (z>y):
             result = (z*100)

print(result)