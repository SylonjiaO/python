# Working With Dictionary

mydic={"P190":("SAP Updation","Lisbon",24),"P123":("Voice Integration","Melbourne",12),
       "P445":("5G Implementation","Paris",20),
       "P214":("Bank Reconciliation","Colorado",15)}

mydict1={"P443":("Work Automation","Paris",20),
       "P216":("Work on Cybersecurity","London",10)}


mydic.update(mydict1)  # update() is used to combine two dictionaries
print("List of All Projects")
##for x in sorted(mydic.keys(),reverse=True):
##    print(x+"\t\t"+str(mydic.get(x)))
##
##print("Total No of Projects =", len(mydic))

for x in sorted(mydic.keys(),reverse=True):
    print(x+"\t\t"+str(mydic.get(x)[0]+"\t\t"+mydic.get(x)[1]))

print("Total No of Projects =", len(mydic))
   
#How To Search From a Dictionary ?
pcode=input("Enter the Project Code :").strip().upper()
if ( pcode in mydic.keys()):
    print("Project Code : ", pcode)
    print("Project Detail :", str(mydic.get(pcode)))
else:
    print("Project Code Not Found")
