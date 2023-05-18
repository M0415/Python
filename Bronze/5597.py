people = [i for i in range(1, 31)]

for j in range(28):
    people.remove(int(input()))
    
print(people[0])
print(people[1])