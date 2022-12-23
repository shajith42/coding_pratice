class college:
    def student(self,name,age,degree,rollno):
        self.name=name
        self.age=age
        self.degree=degree
        self.rollno=rollno
        print("Name:",name)
        print("Age:",age)
        print("degree",degree)
        print("rollno:",rollno)

o=college()
name=input("Enter your name:")
age=int(input("Enter your age:"))
degree=input("Enter your degree:")
rollno=input("Enter your Roll no:")
o.student(name,age,degree,rollno)


 