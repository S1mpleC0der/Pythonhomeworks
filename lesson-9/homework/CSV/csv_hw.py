import csv

with open('grades.csv', mode="r") as file:
    read = csv.DictReader(file)
    grades_data = list(read)
        
grades ={}

for row in grades_data:
    subject = row['subject']
    grade = row['grade']  
    if subject not in grades:
        grades[subject] = []
    grades[subject].append(grade)
    
avg_grades ={}
for subject,total_grades in grades.items():
    avg_grades[subject] = sum(total_grades)/len(total_grades) 
    
with open('avg_grades.csv', mode="w") as file:
    write = csv.writer(file)
    write.writerow(['subject','average'])
    for subject,avg_grade in avg_grades.items():
        write.writerow([subject,round(avg_grade,2)])

        
              
    
