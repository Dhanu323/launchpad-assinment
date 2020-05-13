def rob():
    up = float(input("Enter the no of unit tha has to be moved up in a plain ="))
    if up >=0:
        pass
    else:
        print("please enter the value properly")
        rob()    
    down = float(input("Enter the no of unit tha has to be moved down in a plain ="))
    if down >=0:
        pass
    else:
        print("please enter the value properly")
        rob()
    right = float(input("Enter the no of unit tha has to be moved right in a plain ="))
    if right >=0:
        pass
    else:
        print("please enter the value properly")
        rob()
    left = float(input("Enter the no of unit tha has to be moved left in a plain ="))
    if left >=0:
        pass
    else:
        print("please enter the value properly")
        rob()
    x = up - down
    y = right - left
    print("coordinates of the robot in the plain",x,y)
    print("x-coordinates",round(x))
    print("y-coordinates",round(y))
    a = input("press any key to exit")
    if a.isalpha():
        exit()
rob()