import matplotlib.pyplot as plt

x = ['Maths', 'Science', 'History', 'English', 'Physics', 'Biology', 'Geography', 'Chemistry']
y = [80, 90, 75, 85, 92, 88, 82, 78]

colors = ['green', 'red', 'grey', 'yellow', 'blue', 'orange', 'purple', 'black']
plt.bar(x, y, color=colors)
plt.xlabel("Subject")
plt.ylabel("Grades")
plt.title("Student Grades")
plt.show()
