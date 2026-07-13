stdName =  input(" enter student name")
classna = input("enter class name ")
score=[]
subjectsnum=int(input("subject number "))
subjects=[]
for i in range(subjectsnum):
    sub=input("enter subject name ")
    subjects.append(sub)

    scr=int(input("enter score"))
    score.append(scr)
def average(score):
        total=sum(score)
        avg=total/len(score)
        return avg

def grade(avg):
        if avg>85:
            grade ="A"
            return grade
        elif avg>70 :
            grade="B"
            return grade
        elif avg >60 :
            grade ="C"
            return grade 
        else:
            grade="F"
            return grade
avg=average(score)
student_grade=grade(avg)

print("student name is ",stdName)
print("class name is ",classna)

for i in range (subjectsnum):
     print("subject name is ",subjects[i])
     print("score is ",score[i])

print("Average:", avg)
print("Grade:", student_grade)