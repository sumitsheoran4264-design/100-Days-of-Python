#Highest score
student_score = [150,142,185,120,171,123,156,245,345,455,456,452,457] 

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)