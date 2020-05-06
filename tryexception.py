def test(a,b):
	try:        #try block
		c =a/b
	except:		# exception block
		print("division by ZERO")
	else: 
	 	print("the result %2f" %(c))
a = float(input("enter the value"))
b = float(input("enter the value")) 
test(a,b)	 	
