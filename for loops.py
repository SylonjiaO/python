#for loops

#range is a python funtion that tells python from a - b where to run, stops at the outer limit 
print("List of Numbers from 1 to 10") #runs 1-9
for x in range(1,10):
    print(x)
#x is an iterrator

print("List of Numbers from 1 to 10") #runs 1-9
for x in range(1,10,2): #x is incremented
    print(x)

print("List of Numbers from 1 to 10") #runs 1-10
for x in range(1,11):
    print(x)

    print("List of Numbers from 1 to 10") #runs 9-1 decreasing 
for x in range(9,0,-2): 
    print(x)


