import matplotlib.pyplot as plt

student_names = ["James", "Sunny", "Lara", "Bob", "David", "Eden", "Sarah", "John"]
student_marks_subj1 = [43,41,34,46,45,33,37,39]
student_marks_subj2 = [45,47,38,48,41,39,36,44]

student_perc = []

for x in student_marks_subj1:
    res = (x/50) * 100
    student_perc.append(res)
print(student_perc)

def marks_line_graph():
    plt.plot(student_names, student_marks_subj1)
    plt.plot(student_names, student_marks_subj2)
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
marks_line_graph()

def marks_bar_graph():
    plt.bar(student_names, student_perc)
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
marks_bar_graph()