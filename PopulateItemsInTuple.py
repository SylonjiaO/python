# How To populate Items inside of Tuple

location=() #blank tuple
location=[] #blank list

choice= "Y"
while(choice =="Y"):
    values = input("Enter New Location :").strip().title()
    blanklist.append(values)
    choice=input("What To Add Another Location ?").strip().upper()
    if(choice =="Y"):
        continue
    else:
        break
location=tuple(blanklist)
print("The Selected Locations Are: ")
for x in location:
    prin(x)

del(blanklist)
