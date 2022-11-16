ipaddress=input("Enter your IP Address:").strip()
octets=ipaddress.split(".")
for i in octets:
    print(i)
