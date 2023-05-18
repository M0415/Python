score_bio = {"Physics": 0, "chemistry" : 0,
         "Biology" : 0, "local_science" : 0,}
score_hi = {"history" : 0, "Geography" : 0}
sum = 0
sum_else = 0
for i in "Physics", "chemistry", "Biology", "local_science":
    score_bio[i] = int(input())
    
for j in "history", "Geography":
    score_hi[j] = int(input())

bio = score_bio["Physics"]
for x in "Physics", "chemistry", "Biology", "local_science":
    if bio > score_bio[x]:
       bio = score_bio[x]
        
hi = score_hi["history"]
if hi > score_hi["Geography"]:
    hi = score_hi["Geography"]


for i in "Physics", "chemistry", "Biology", "local_science":
    sum += score_bio[i]
    
for j in "history", "Geography":
    sum += score_hi[j]
    
sum_else = bio + hi
sum -= sum_else
print(sum)