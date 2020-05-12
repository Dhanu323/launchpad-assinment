my_list= []
my_list = list(map(int, input("Enter a multiple value: ").split())) 
my_list.sort()		
print("______________________")	
n = int(input("enter the nth number"))
if len(my_list) > 1:
	print(my_list[n-1])
else:
	print(my_list)
