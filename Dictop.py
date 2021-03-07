d = {}
class Employee:
    def salary_slip(self,name,address,pan,salary,tda,deduct):
        self.name=name
        self.address=address
        self.pan=pan
        self.salary=salary
        self.tda=tda
        self.deduct=deduct
        self.hra=self.salary*1.20
        self.gross=self.salary+self.hra
        self.net=self.gross-self.deduct
        return self.net

    def accept(self):
        name = input("Enter name: ")
        address = input("Enter address: ")
        pan = input("Enter pan number: ")
        salary = int(input("Enter salary: "))
        tda = int(input("Enter tda: "))
        deduct = int(input("Enter deduct amount: "))
        self.net = self.salary_slip(name,address,pan,salary,tda,deduct)

    def display(self):
        print("name= ",self.name)
        print("address= ",self.address)
        print("pan= ",self.pan)
        print("salary= ",self.salary)
        print("deduct= ",self.deduct)
        print("gross= ",self.gross)

    def search(self,name):
        for k,v in d.items():
            print("K: ",k)
            print("V: ",v)

            if k==name:
                print(v.__dict__)

while True:
    print("1.Add Employee \n 2.Display all employee details \n 3.Update \n 4.Search employee \n")

    ch = int(input("Enter Your Choice: "))

    if ch==1:
        e = Employee()
        e.accept()

    elif ch==2:
        e.display()

    elif ch==3:
        d.update({e.name:e})
        print("Updated")

    elif ch==4:
        name = input("Enter name to be searched: ")
        e.search(name)

    elif ch==0:
        break
