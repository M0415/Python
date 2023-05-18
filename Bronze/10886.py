N = int(input())

yes, no= 0, 0

for i in range(N):
    cute = int(input())
    
    if cute == 1:
        yes += 1
    elif cute == 0:
        no += 1

if yes > no :
    print("Junhee is cute!")
elif no > yes:
    print("Junhee is not cute!")