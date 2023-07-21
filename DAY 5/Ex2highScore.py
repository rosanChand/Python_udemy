# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print(len(student_scores))
max1 = 0
for i in range(0, (len(student_scores))):
    # j = i + 1
    # print(j)
    
    if(max1 <= student_scores[i]):
      max1 = student_scores[i]
        
    # print(max1)
print("The highest score in the class is:",max1)
