f = open("sqr.txt","w")
n = int(input("Enter number "))
for i in range(1,n+1):
    f.write(str(i*i))
f.close()
