from typing import Any
import os



        
# add student 
def add_student():  
    with open('student.txt','a+') as fptr:
        l1=[i for i in details()]
        fptr.write(l1[0]+","+l1[1]+","+l1[2]+",\n")


# Read all data

def read_data():
    name_check_list=set()
    with open('student.txt','r+') as fptr:
        while True:
            l=fptr.readline()
            if not l:
                break
            l1=l.split(',')
            name_check_list.add(l1[0])
    for i in name_check_list:
        details_name(i)
        print()
        

# Read specific student
def details_name(name):
# print()
    with open('student.txt','r+') as fptr:
        count =0
        total_present=0
        while(True):
        
            l=fptr.readline()
            if not l:
                print("Total Present ",f"{total_present:>2}")
                break
            if l.split(',')[0]==name:
                list1=l.split(',')
                if count==0:
                    print("Name : ",list1[0])
                    print("    :Record:")
                    print('Dates     :','Status')
                    count+=1
                # print(list1[1]," ",list1[2])
                print(f"{list1[1]:<13}","  ",list1[2])
                if list1[2]=='p':
                    total_present+=1


# add details 
def details():
    name=input("Enter student name :")
    date=input("Enter date in dd/mm/yyyy format :")
    attendance=input("attendance status(p/a) :")
    return (name,date,attendance)

# to delete data
def delete_name():
    name=input("Enter the name of the student to delete data permanently or type no")
    if(name!='no'):
        tfp=open('tempfile.txt','w')
        with open('student.txt',"r+") as fptr:
            
                while(True):
                    line=fptr.readline()
                    if not line:
                        
                        break
                    if(line.split(',')[0]!=name):
                            l1=line.split(',')
                            tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
        tfp.close()
        os.remove('student.txt')
        os.rename('tempfile.txt','student.txt')

        print("deleted successfully ")
                
# updation in name
def updation_name():
    oldname=input("Enter old name :")
    new_name=input("Enter new name :")
    tfp=open("tempfile.txt",'w')
    with open('student.txt',"r+") as fp:
        while True:
            line =fp.readline()
            if not line:
                break
            l1=line.split(',')
            if l1[0]==oldname:
                
                tfp.write(new_name+","+l1[1]+","+l1[2]+",\n")
            else:
                tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
    tfp.close()
    os.remove('student.txt')
    os.rename('tempfile.txt','student.txt')
    print(" Updated ")

          
## updation in attendence
def updation_attendance():
    name=input("Enter name of student :")
    date=input("Enter  date(dd/mm/yyyy) :")
   
    tfp=open("tempfile.txt",'w')
    with open('student.txt',"r+") as fp:
        while True:
            line =fp.readline()
            if not line:
                break
            l1=line.split(',')
            if l1[0]==name and l1[1]==date:
                updated_attendece = 'a' if l1[2]=='p' else 'p'
                tfp.write(l1[0]+","+l1[1]+","+updated_attendece+",\n")
            else:
                tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
    tfp.close()
    os.remove('student.txt')
    os.rename('tempfile.txt','student.txt')
    print(" Updated successfully")    



#login  code
flag=0
while flag==0:
    print("Enter your choice:")
    print("Press  : 1.SignUp   and    2.SignIn")
    choice=int(input("Enter your choice:"))
    if choice==1:
        user_name=input("Enter  user_name :")
        pass_word=input("Enter password :")

        with open('user.data','a+') as fptr:
            fptr.writelines(user_name+","+pass_word+","+"\n")
    elif choice ==2:
        userid=input("Enter user name :")
        password=input("Enter password :")

        with open('user.data','r') as fptr:
        
            while True:
                line=fptr.readline()
                if not line:
                    print("Data not found ")
                    break
                if line.split(',')[0] ==userid and line.split(',')[1]==password:
                    print("Authentication successfull... ")

                    flag=1
                    break
    
    else:
        print("enter again")





while(True):
    os.system("cls")
    print("Authentication successfull")
    print("Enter your choice :")
    print("1.Add Student")
    print("2.View student")
    print("3.view one student")
    print("4.Delete student ")
    print("5.Update student")
    print("6 Exit")

    choice=input("Enter your choice :  ")
    if choice=='1':
        add_student()
        print("Data entered successfully")
        input("Press enter")
        
    elif choice=='2':
        read_data()
        input("Press Enter")
    elif choice=='3':
        name=input("Enter the name of student to search attenedence:")
        details_name(name)
        input("Press Enter")
    elif choice=='4':
        delete_name()
        input("Press Enter")
    elif choice=='5':
        print("Press 1 to update name \nPress 2 to Update  attendance")
        subchoice=input()
        if subchoice=='1':
            updation_name()
            print("updated successfully")
        else:
            updation_attendance()
            print("updated successfully")
        
        
    elif choice=='6':
        print("Exititng......")
        break
































                

            



            

