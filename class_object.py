#object oriented programming in python
#creating a class student
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade
#creating another class course
class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value=0
        for student in self.students:
            value+=student.get_grade()
            return value/len(self.students)

s1=Student("pravallika",23,65)
s2=Student("deshna",17,88)
s3=Student("uday",20,75)
course=Course("science",2)
print(course.add_student(s1))
print(course.add_student(s2))
print(course.get_average_grade())