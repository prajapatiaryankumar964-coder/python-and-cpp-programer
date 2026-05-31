n=int(input("How many students data u want to insert?"))

class student:

    def read(self):
        self.rollno=int(input("Enter Roll No:"))
        self.sname=input("Enter Student Name:")
        
    def show(self):
        print(str(self.rollno)+"\t"+self.sname)


stdlist=[]

for i in range(n):
    stdlist.append(student())


for dr in stdlist:
    dr.read();

print("RollNo\tName")

for ds in stdlist:
    ds.show()