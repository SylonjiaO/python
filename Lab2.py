#Lab Excercise 2
answer="Y"
#input always takes in charactors
while (answer=="Y" or answer=="y"):
    empname= input("Enter the Employee Name : ").upper().strip()
    if (len(empname)==0):
        print("Sorry employee name can not be blank")
        continue
    while True: #conditional loop
        salary= int(input("Enter the Salary : "))
        if (salary <30):
            print("invalid salary....")
            continue
        else:
            break
    while True:
        emailid=input("Enter Official Email ID :").strip().lower()
        if(emailid.endswith("@coltnet")):
            break
        else:
            print("Sorry It's not Your Official ID...")
            continue
        
    print("NAME\t\t\tSALARY")
    print("*****\t\t\t******")
    print("%s\t\t\t$%.2f" %(empname,salary))
    answer=input("Want to continue(Y/N)?")
    if (answer=="Y" or answer=="y"):
         continue
    else:
        break
print("Program Stopped")

while (answer=="Y" or answer=="y"): #unconditional loop
    empname= input("Enter the Employee Name : ")
    salary= int(input("Enter the Salary : "))    
    print("NAME\t\t\tSALARY")
    print("*****\t\t\t******")
    print("%s\t\t\t$%.2f" %(empname,salary))
    answer=input("Want to continue(Y/N)?")
    if (answer=="Y" or answer=="y"):
         continue
    else:
        break
print("Program Stopped")
