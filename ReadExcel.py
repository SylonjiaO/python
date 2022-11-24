import pandas

mydata=pandas.read_excel("C:/YU Learn to Code/python/NameList.xlsx")
##print(mydata)
participants=set(mydata['Participants List'])
print(len(participants))
print(participants)
