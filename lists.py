# List Example

course1=["Oracle","Python","Ansible","AWS","Power BI","Java","Big Data","Excel"]
course2=["Soft Skills","Behavioural Approach","Crisis Management","German", "French"]
course3=course1+course2
print(type(course3))
print(course3)

course3.append("Linux Administration") #adding extra tasks 
course3.append("Java Microservices")
course3.remove("Excel")
course3.sort(reverse=True)#sorting tasks .sort() assending .sort(reverse=True) desending
print("List of All Courses")
for x in course3:
    print(x)

print("Total Num of Courses =", len(course3))

coursename=input("Enter Course To Search:").strip().upper()
subjectlist=[] #this is the way we create a blank list
for x in course3:
    subjectlist.append(x.upper())
if coursename in subjectlist:
    print(f"{coursename} is Availible")
else:
    print(f"{coursename} is Not Avalible")

del(subjectlist) # Remove some component from memory
#python does not have garbage collection


