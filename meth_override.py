class Employee:
    r_amt=1.04
    def __init__(self,fname=0,lname=0,eid=0,sal=0):
        self.fname=input("Enter first name: ")
        self.lname=input("Enter last name: ")
        self.eid=input("Enter id: ")
        self.sal=int(input("Enter salary: "))

    def disp(self):
        print(self.fname)
        print(self.lname)
        print(self.eid)
        print(self.sal)

    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("R Emp: ",self.final)

class Manager(Employee):
    r_amt=1.00
    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("M :",self.final)

class Director(Employee):
    r_amt=1.00
    def raise_amt(self):
        self.final=self.sal*self.r_amt
        print("D",self.final)

e = Employee()
e1=Manager()
e2=Director()
e.disp()
e.raise_amt()
e1.disp()
e1.raise_amt()
e2.disp()
e2.raise_amt()


        
        
