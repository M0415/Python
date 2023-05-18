A ,B ,C = map(int, input().split())
empty = 0

if A > B:
   empty = A
   A = B
   B = empty
if A > C:
   empty = A
   A = C
   C = empty
if B > C:
   empty = B
   B = C
   C = empty
if A > C:
   empty = A
   A = C
   C = empty
   
print(A, B, C)