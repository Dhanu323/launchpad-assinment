title = str(input("enter the title"))    
output = []             
output.append(title[0])       
for char in title[1::]:         
    if char.islower():
        output.append(char)
    if char.isupper():
        output.append( " ") 
        output.append(char)       
print("".join(output))  