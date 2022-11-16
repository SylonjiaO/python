#Lab 3 on Loops

answer="Y"
while (answer=="Y" or answer=="y"):
    myno=int(input("Enter A Number: "))
    for x in range (1,11):
        result=myno *x
        print(f"{myno} X {x} = {result}")
    answer=input("Want to continue(Y/N)?")
    if (answer=="Y" or answer=="y"):
        continue
    else:
        break
    print("Program Stopped")
