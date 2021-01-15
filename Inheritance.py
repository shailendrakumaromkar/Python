class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print("my first name is:" + self.fname + " & my lname is : " + self.lname)


obj=Person("Raja","Omkar")
obj.printname()

class Child(Person):
    def __init__(self,fname, lname,year):
        super().__init__(fname,lname)
        self.year=year
    
    def biodata(self):
        print("im inside child class: my first name is -> " + self.fname + " & my lname is : " + self.lname +"& i graduated in : "+ self.year)

c1=Child("Neha","Kalbhor","2009")
c1.biodata()