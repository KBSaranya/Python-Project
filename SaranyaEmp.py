import re
import datetime
def findage(birthDate):
     today = datetime.date.today()
     age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
     return age
     
def isrepeated(ename):
    for i in range (0,len(ename)-2):
           if ename[i]==ename[i+1] and ename[i+1]==ename[i+2]:
               return True
    return False


 
def qualify(args):
    thislist = ["BTech Information Technology", "BE Computer Science", "BE Mechanical","BE Automobile","BE EEE","BE ECE","BTech BioMedical","Others"]
    return thislist[args]

     
def validatephoneno():
    while True:
        Phonenumber = (input('Enter your Phone Number:'))
        if (not(Phonenumber.isdigit())):
            print(' Mobile number should be in numeric.Give it an another try')
            continue
        elif len(Phonenumber)!=10:
            print("Please Enter the valid Phonenumber it should not be greater or less then 10 digits")
            continue
        elif Phonenumber.startswith(('0' , '1' , '2', '3', '4', '5')):
            print("Please Enter the valid Phonenumber it should not starts with 1,2,3,4,5")
            continue
        else :
           return Phonenumber
def validateEmailid():   
  while True:
    email=input("Enter yout Email")
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if email_regex.match(str(email)):
        return email
    else:
        print("Please Enter the valid Email id")
        continue


def validateEmpID():
    while True:
        ID=input('Enter your Employee ID:')
        EmpID= 'ACE'+ID
        if (not(ID.isdigit())):
            print('Oops :( ! ID should be in numeric. You got an another chance')
            continue
        elif int(ID)==0:
            print('Oh-no! Employee ID cannot be null. Please enter  valid ID')
            continue
        elif len(ID)!=4:
            print('Oh-no! Employee ID contain must 4 characters. Enter zeroes if it is a single ,double or triple digit number')
            continue
        else:
            return EmpID
        
def validateEmpname():
    while True:
        Emp_name=input("Enter the Employee Name")
        space=''
        if ' ' in Emp_name:
            print("Enter the valid employee name it should not empty")
            continue
        elif (not(Emp_name.isalpha())):
            print("please Enter the valid employee id t should not be numeric")
            continue
            continue
        elif isrepeated(Emp_name):
            print('Sorry! The Name you entered has repeated alphabets. Please enter a valid Name')
            continue
        elif len(Emp_name)<=2:
            print("Please enter the valid name it should not be less then 2 character")
        else:
            return Emp_name
def Qualification():
    print("Option 0 :  BTech Information Technology")
    print("Option 1 :  BE Computer Science")
    print("Option 2 :  BE Mechanical")
    print("Option 3 :  BE Automobile")
    print("Option 4 :  BE EEE")
    print("Option 5 :  BE ECE")
    print("Option 6 :  BTech BioMedical")
    print("Option 7 :  Others")
    option=int(input("Select one of the options:"))
    while option>7:
        print("Oops! choose a valid number between 1 and 8. Retry")
        option=int(input())
    q=qualify(option)
    if(q=='Others'):
        p=input('Enter your qualification:')
        return p
    else:
        return q
      

def validatedob():
    while True:
        try:
            dob1=input('Enter your DOB in the format YYYY-MM-DD:')
            dob= datetime.datetime.strptime(dob1, '%Y-%m-%d')
            age=findage(dob)
            if age<0:
                print("you have entered a future date")
            elif age<18:
                print('You are too young. You have time to come again')
            elif age>60:
                print("Happy to bid you bye")
            else:
                return age,dob1
        except:
            print("Sorry you entered the invalid don ,Try Again!!")
            validatedob()

def validatedoj():
    try:
        doj1=input('Enter your DOJ in the format YYYY-MM-DD:')
        doj= datetime.datetime.strptime(doj1, '%Y-%m-%d')
        exp=findage(doj)
        if exp<0:
            print("you have entered a future date")
        else:
            return str(exp),doj1
    except:
            print("Sorry You entered the invalid doj Try Again!!")
            validatedoj()

def validatesalary():
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    while True:
        salary = input('Enter any salary: ')
        
        if (special_char.search(salary)!= None):
            print('Salary should be in special character')
            continue
        elif(not(salary.isdigit())):
            print('Salary should be in numeric')
            continue
        elif int(salary)==0:
             print('salary should not be null')
             continue
        elif int(salary)<1000 or int(salary) >10000000:
            print("Salary should be between 1000 and 1 crore")
            continue
        
        else:
            return salary

            
def printinfo(eid,ename,eno,eemail,edob,edoj,equalification,esalary,eempdob,eempdoj):
    print("\nEMPLOYEE DETAILS\n")
    print('Employee ID      : '+eid)
    print('Employee Name    : '+ename)
    print('Mobile Number    : '+ eno)
    print('Email ID         : '+eemail)
    print('D.O.B            : '+eempdob)
    print("Age              : you are {} years and We are happy to have you here".format(edob))
    print('D.O.J            : '+eempdoj)
    print("Experience       : "+edoj)
    print('Qualification    : '+equalification)
    print("Salary           : Rs."+esalary)



if __name__ == '__main__':
    while True:
        print('\nWelcome to the Employee managament system.\nPlease enter your credentials\n')
        EMPLOYEEID=validateEmpID()
        EMPLOYEENAME=validateEmpname()
        EMPLOYEENUMBER=validatephoneno()
        EMPLOYEEEMAIL=validateEmailid()   
        EMPLOYEEAGE,EMPDOB=validatedob()
        EMPLOYEEEXP,EMPDOJ=validatedoj()
        EMPLOYEEQUALIFICATION=Qualification()
        EMPLOYEESALARY=validatesalary()
        printinfo(EMPLOYEEID,EMPLOYEENAME, EMPLOYEENUMBER,EMPLOYEEEMAIL,EMPLOYEEAGE,EMPLOYEEEXP,EMPLOYEEQUALIFICATION,EMPLOYEESALARY,EMPDOB,EMPDOJ)
        final=input('\nDo you you want to enter another employee record?(Y/N)')
        if final=='Y':
            continue
        else:
            print('\nThank You\n')
            break




