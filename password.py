def cheack(password):
	m = len(password)
	if m > 7 and m < 15:
		for i in password:
			if(((ord(i)>=65) and (ord(i)<=90) or (ord(i)>=97) and (ord(i)<=122) or (ord(i)>=48) and (ord(i)<=57) or (ord(i)==35) or (ord(i)==36) or ord(i)==64)):
				print("valide password")
				break
			else:
				print("invalid password")	
	else:
		print("doesn't reach the paramerter")			
id = input("enter the id")
password = input("enter the password")
cheack(password)	



