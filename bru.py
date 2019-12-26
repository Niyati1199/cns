cipher="pm ol ohk hufaopun jvumpkluaphs av zhf,ol dyval pa pu jpwoly"
for key in range(1,26):
	for i in cipher:
		if i=="," or i==" ":
			print(i,end="")
		elif((ord(i)+key)>122):
			print(chr(97+((ord(i)+key)-97)%26),end="")
		else:
			print(chr(ord(i)+key),end="")	 		
	print("key:",key)
