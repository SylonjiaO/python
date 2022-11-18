#Circuit ID Encryption

circuited="LON/LON/EN-123456"
cid=circuited.split("/") #['LON','LON','EN-123456']
circuitno=cid[2].split("-") #['EN','123456']
encryptedcircuitid=cid[0]+"/"+cid[1]+"/"+circuitno[0]+"xxx-"+circuitno[1]
print("Encrypted Circuit ID=", encryptedcircuitid)



test="LE-123456"
print(test[0:6]+"XXX")



