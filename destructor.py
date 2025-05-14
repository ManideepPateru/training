class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
    def __del__(self):
        print("deleted")
s=Student("manideep",86,97)
s.display()
del s