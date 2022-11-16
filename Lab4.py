#lab 4 Counting of words
#split always produces the output in the form of a list 
mysentence=input("Enter your sentence :").strip()
words= mysentence.split(" ")
print(words)
print("Total Number of Words are = ", len(words))

