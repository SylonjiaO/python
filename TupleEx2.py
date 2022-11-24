# Tuple Examples

deptlist=("Sales","HR","Payroll","Finance","Accounts")
#print(type(deptlist))#tuples are static and can't be changed
mydept=list(deptlist)#changes tuple to list
mydept.append("IT")
mydept.append("CSO")
deptlist=tuple(mydept)#changes list to tuple 
print("Now Overall Depts Are :")
for x in deptlist:
    print(x)

print("Total Depts = " , len(deptlist))
