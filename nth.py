my_list= []
def number(n):
	my_list = list(map(int, input("Enter a multiple value: ").split())) 
	my_list.sort()
	if len(my_list) > 1:
		#for i in range(-n,0):
		print(my_list[n-1])
	else:
		print(my_list)		
def main():
	print("______________________")	
	n = int(input("enter the nth number"))
	number(n)
main()