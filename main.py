class Student:
    amount_of_students = 0
    def __init__(self, height=111):
        self.height = height
        Student.amount_of_students += 1

student1 = Student()
student2 = Student()
print(student1.amount_of_students)
student3 = Student()
student4 = Student()
student5 = Student()
print(student4.amount_of_students)
print(Student.amount_of_students)