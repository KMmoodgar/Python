class Operate:
    def __init__(self):
        self.li=[]

    def accept(self):
        n = int(input("enter number of elements: "))
        for i in range(0,n):
            ele = int(input("Enter element: "))
            self.li.append(ele)

        print("The List is: ",self.li)

    def __add__(self,other):
        newlist = []

        for i in range(0,len(self.li)):
            newlist.append(self.li[i] + other.li[i])

        print("List after adding: ",newlist)

    def __sub__(self,other):
        newlist = []

        for i in range(0,len(self.li)):
            newlist.append(self.li[i] - other.li[i])

        print("List after sustraction: ",newlist)

    def __mul__(self,other):
        newlist = []
        
        for i in range(0,len(self.li)):
            newlist.append(self.li[i] * other.li[i])

        print("List after multiplication: ",newlist)

    def __floordiv__(self,other):
        newlist = []

        for i in range(0,len(self.li)):
            newlist.append(self.li[i] // other.li[i])

        print("List after division: ",newlist)

