A = []
a,b,c = map(int, input().split())
A.append(a)
A.append(b)
A.append(c)

A.remove(max(A))
A.remove(min(A))
print(A[0])