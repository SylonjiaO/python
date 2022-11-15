# To Input a Number and to Check if it is Divisible By 5 And 8

myno=int(input("Enter The Number :"))  # For e.g. Our Input Value is 40
rem1=myno % 5
rem2=myno % 8
if (rem1==0 and rem2==0):
    print(f"{myno} is Divisible by Both 5 And 8")
elif( rem1!=0 and rem2==0):
    print(f"{myno} is Divisible By 8 But Not By 5")
elif(rem1==0 and rem2!=0):
    print(f"{myno} is Divisible By 5 But Not By 8")
elif( rem1!=0 and rem2!=0):
    print(f"{myno} is Not Divisible By 5 and also Not by 8")

print("Thanks...End of Program")
