#Working with Dictionaries
import pandas
myDictionary={"P190":("SAP Updation","Lisbon",24),"P123":("Voice Integration","Melbourne",12),
              "P445":("5G Implementation","Paris",20),"P214":("Bank Reconciliation","Colorado",15)}
myDictionary1={"P443":("Work Automation","Paris",20),
               "P216":("Cybersecurity","London",10)} #key values in a dictionary should always be unique
print(type(myDictionary))

myDictionary.update(myDictionary1) #update() is used to combine two dicts.
print("List Of All Projects")
print(myDictionary)
for x in sorted(myDictionary.keys()): #sort only happens on the key values 
    print(x+"\t\t" + str(myDictionary.get(x)))
print("Total No of Projects = ",len(myDictionary))
##for x in sorted(myDictionary.keys(),reverse=True)
##    print(x +

#How to search a Dictionary

pcode=input("Enter the Project Code :").strip().upper()
if(pcode in myDictionary.keys()):
    print("Project Code: ", pcode)
    print("Project Details:,", str(myDictionary.get(pcode)))
else:
    print("Project Code Not Found")


columns=myDictionary.dtypes.reset_index()
colums.colums=["Pcodes","values"]

print(columns)
