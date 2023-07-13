import matplotlib.pyplot as plt

x = ['Maths', 'Science', 'History', 'English', 'Physics', 'Biology', 'Geography', 'Chemistry']
y = [80, 90, 75, 85, 92, 88, 82, 78]
grades_sum = 0
count = 0

colors = ['green', 'red', 'grey', 'yellow', 'blue', 'orange', 'purple', 'black']
plt.bar(x, y, color=colors)
plt.xlabel("Subject")
plt.ylabel("Grades")
plt.title("Student Grades")
for i in y:
   grades_sum += i
   overal_grade = grades_sum / int(len(y))
   if (i >= 80):
      count += 1

print(overal_grade)
print(count * 100 / int(len(y)))
   
plt.show()
