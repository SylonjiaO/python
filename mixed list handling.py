#Another list example

#A List is a collection which is ordered and changeable.
#Allows  duplicate members. A List is defined by putting the values
#separated by , and enclosed by [ ].​

emaillist=["thomas.k@colt.net",34,"sylonjia.j@colt.net",27,"harry.p@siemens.com",
           "borris.t@colt.net","gregor.r@microsoft.com",40,"saida.m@here.com"]
coltlist=[]
outerlist=[] #A Blank List
for x in emaillist:
    if (str(x).endswith("colt.net")):
        coltlist.append(str(x))
    else:
        outerlist.append(str(x))
print("Persons from Colt : ")
print(coltlist)
print("Persons from Colt : ")
print(outerlist)

