class Parent:

    name=""
    def display(self,name):
        self.name=name
        print(self.name)

class Child(Parent):  
    name="satish kumar"
    def display(self,name):
        self.name=name
        super().display(name)
        print(self.name)
obj=Child()
obj.display("suresh")   #satish kumar

# obj1=Parent()
# obj1.display()  #satish