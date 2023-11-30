class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print("The first name of the person is ",self.firstname)
        print("The sencond name of the person is ",self.lastname)
        print("The first name of the person is ",self.firstname,"\n" "The sencond name of the person is ",self.lastname )
x=Person("Munna","chaudhary")
x.printname()