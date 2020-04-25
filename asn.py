import pprint 
x = int(input("enter the value of array"))
y = int(input("enter the value of array"))
z = int(input("enter the value of array"))
lst = [[['#' for col in range(x)] for col in range(y)] for row in range(z)] 
pprint.pprint(lst) #pretty printed function
