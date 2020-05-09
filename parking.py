from datetime import datetime
two_wheeler = {}
four_wheeler = {}
class Park:
    def __init__(self):
        two_wheeler = {}
        four_wheeler = {}
#-----------------------------------------------------------------------        
    def wo(self,q):
        if q<4:
            now = datetime.now()
            current_time1 = now.strftime("%H:%M:%S")
            print(current_time1)
            kol = input("enter the vehicle number\n")
            two_wheeler[kol] = current_time1
            sd = 4-q
            print("slot remaining",sd)
            return two_wheeler
        else:
            print("slots filled")   
#-----------------------------------------------------------------------            
    def four(self,gg):
        if gg<5:
            now = datetime.now()
            current_time2 = now.strftime("%H:%M:%S")
            vol = input("enter the vehicle number\n")
            four_wheeler[vol] = current_time2
            print("slots remaining",5-gg)
            print("")
            return four_wheeler
        else:
            print("slots filled")   
#-----------------------------------------------------------------------            
p = Park()              
a=0
count = 0
mount = 0
print("total number of slots for two_wheeler is 5\ntotal number of slots for four_wheeleris 5")
while a<3:
    a = int(input("welcome to parking\n1.book a slot\n 2.unbook slot\n3.view aloted slots \n4.exit\n"))
#if selected option1----------------------------------------------------------------------------------- 
    if a==1:
        g = int(input("enter the the type of vehicle to book a slot \n1.two_wheeler\n2.fourwheeler\n"))
        if g==1:
            count = count+1
            p.wo(count)
        elif g==2:
            mount = mount+1
            p.four(mount)
#if selected option 2---------------------------------------------------------------------------------              
    elif a==2:
        l = int(input("enter the the type of vehicle to un book a slot \n1.two_wheeler\n2.fourwheeler\n"))
        if l==1:
            print(two_wheeler)
            #no = int(input("enter ur vehicle number  \n"))
            now = datetime.now()
            current_time3 = now.strftime("%H:%M:%S")
            print(current_time3)
            count = count-1
            no = input("enter vehiclenumber")
            for key, value in two_wheeler.items():
                if key==no:
                    print("vehiclenumber:",key, " time of cheak in ", value,"time of cheak out",current_time3)
            two_wheeler.pop(key)
        elif l==2:
            now = datetime.now()
            current_time4 = now.strftime("%H:%M:%S")
            print(current_time4)
            count = count-1
            no = input("enter vehiclenumber")
            for key, value in four_wheeler.items():
                if key==no:
                    print("vehiclenumber:",key, " time of cheak in ", value,"time of cheak out",current_time4)
                    print("\n")
            four_wheeler.pop(key)
            

#if selected option 3----------------------------------------------------------------------------------         
    elif a==3:
        b = int(input("press 1 to view alloted slots of two wheelers\n"))
        if b==1:
            for key, value in two_wheeler.items():
                print(key, ' : ', value)
        if b==2:
            for key, value in four_wheeler.items():
                print(key, ' : ', value)  
#if selected to exit-------------------------------------------------------------------------------------           
    elif a==4:
        exit()
            

