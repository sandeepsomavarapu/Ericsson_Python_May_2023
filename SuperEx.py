class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)


class Student (Person):#is-a,has-a
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)#
        self.rollno = rollno
        self.marks = marks
		
    def display(self):
        super().display()
        print('Roll No:', self.rollno)
        print('Marks:', self.marks)



s1 = Student('sandeep',26, 101, 90)
s1.display()
