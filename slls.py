nam = str(input("enter the name"))
z = nam.split()
for name in z:
    newstr = name
    for i in newstr:
        if( not ((ord(i)>=65) and (ord(i)<=90) or (ord(i)>=97) and (ord(i)<=122) or ord(i)==32)):
            newstr = newstr.replace(i,"")
    print(newstr)
