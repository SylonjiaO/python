
myword=input("Enter your word: ").strip().lower()
if myword == myword[::-1]:
    print(f"{myword} is a palindrome.")
else:
    print("The string is not a palindrome.")
