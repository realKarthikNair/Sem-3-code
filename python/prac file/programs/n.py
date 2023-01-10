"""    14. Create a binary file with roll number, name and marks. 
Input a roll number and perform the following operations:
    • update the marks. 
    • Delete the record 
    • Display the record 
    • Append the record 
    • Search the record"""

import os, pickle

def writerec(rno,name,marks):
     f=open(os.path.join("files", "students.data"),'ab')
     srec={"rno":rno,"name":name,"marks":marks}
     pickle.dump(srec,f)
def readrec():
     f=open(os.path.join("files", "students.data"),'rb')
     print("Display Student Details")
     r=int(input("Enter roll no whose record is to be displayed: "))
     print("Roll No",'','Name','\t','Marks',end='')
     print()
     while True:
          try:
               rec=pickle.load(f)
               if rec['rno']==r:
                    print('',rec['rno'],'\t',rec['name'],'\t',rec['marks'])
          except:
               break
def Input():
     n=int(input("How many records do you want to enter?"))
     for i in range(n):
          rno=int(input("Enter roll no: "))
          name=input("Enter name: ")
          marks=int(input("Enter marks: "))
          writerec(rno,name,marks)
def searchrec(rno):
     f=open(os.path.join("files", "students.data"),'rb')
     while True:
          try:
               rec=pickle.load(f)
               if rec['rno']==rno:
                    print("Roll no: ",rec['rno'])
                    print("Name: ",rec['name'])
                    print("Marks: ",rec['marks'])
                    break
          except EOFError:
               print("Record not found \nTry again ")
               break
def update():
     f=open(os.path.join("files", "students.data"),'rb+')
     rno=int(input("Enter roll no whose marks you want to update: "))
     try:
          while True:
               pos=f.tell()
               rec=pickle.load(f)
               if rec['rno']==rno:
                    um=int(input("Enter updated marks: "))
                    rec['marks']=um
                    f.seek(pos)
                    pickle.dump(rec,f)
     except EOFError:
          f.close()
def delete():
     f=open('Student.dat','rb')
     l=[]
     while True:
          try:
               rec=pickle.load(f)
               l.append(rec)
          except EOFError:
               break
     f.close()
     rn=int(input("Enter roll no to delete record: "))
     f=open('Student.dat','wb')
     for i in l:
          if i['rno']==rn:
               continue
          pickle.dump(x,f)
     f.close()
while True:
     print("1. Update marks \n2. Delete record\n3.Display record\n4.Append record\n5.Search record\n6.Exit")
     ch=int(input("Enter choice: "))
     if ch==1:
          update()
     elif ch==2:
          delete()
     elif ch==3:
          readrec()
     elif ch==4:
          Input()
     elif ch==5:
          r=int(input("Enter roll no to be searched: "))
          searchrec(r)
     else:
          exit 
          
     
          
    